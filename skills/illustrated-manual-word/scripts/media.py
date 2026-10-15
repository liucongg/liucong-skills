#!/usr/bin/env python3
"""Plan, acquire and audit book images. No generation/API credentials in this helper."""
from __future__ import annotations
import argparse
import hashlib
import ipaddress
import json
import socket
import tempfile
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit, parse_qsl
from PIL import Image, ImageOps, ImageDraw, ImageFont

METHODS = {'svg', 'existing', 'generated', 'hybrid'}
ROLES = {'technical', 'context', 'reference'}
MAX_BYTES = 20 * 1024 * 1024
SECRET_KEYS = {'token', 'access_token', 'api_key', 'key', 'signature', 'sig', 'password', 'credential', 'auth'}

def emit(obj, out=None):
    text = json.dumps(obj, ensure_ascii=False, indent=2)
    if out:
        p = Path(out); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text+'\n', encoding='utf-8')
    print(text)
    return obj

def local(root, value):
    if not isinstance(value, str) or not value:
        raise ValueError('empty local asset path')
    p = (root / value).resolve()
    if not p.is_relative_to(root.resolve()):
        raise ValueError('asset escapes project')
    return p

def clean_url(url):
    u = urlsplit(url)
    if u.scheme != 'https' or not u.hostname or u.username or u.password:
        raise ValueError('only uncredentialed public HTTPS URLs allowed')
    if u.port not in (None, 443):
        raise ValueError('nonstandard port forbidden')
    for k, _ in parse_qsl(u.query):
        if k.lower() in SECRET_KEYS or k.lower().startswith(('x-amz-', 'x-goog-')):
            raise ValueError('secret-bearing/signed URL cannot enter the manifest')
    return u

def check_remote(url, hosts):
    u = clean_url(url)
    if u.hostname.lower() not in hosts:
        raise ValueError('host is not explicitly allowed')
    addresses = socket.getaddrinfo(u.hostname, 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError('private/local network target forbidden')

class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self, hosts): self.hosts = hosts
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_remote(newurl, self.hosts)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def fetch(url, out, hosts):
    hosts = {h.lower() for h in hosts}
    check_remote(url, hosts)
    op = urllib.request.build_opener(SafeRedirect(hosts))
    req = urllib.request.Request(url, headers={'User-Agent':'IllustratedManual/0.3'})
    with op.open(req, timeout=30) as response:
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES: raise ValueError('image exceeds 20 MB')
    out = Path(out).resolve(); out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=out.parent, suffix='.part', delete=False) as f:
        f.write(raw); tmp = Path(f.name)
    try:
        with Image.open(tmp) as im:
            if im.format not in {'PNG','JPEG','WEBP','GIF'}: raise ValueError('unsupported raster type')
            im.verify()
        # Decode before committing; transparent art must not be pasted onto black.
        with Image.open(tmp) as im:
            rgba = im.convert('RGBA'); bg = Image.new('RGBA', rgba.size, 'white'); bg.alpha_composite(rgba)
            bg.convert('RGB').save(out, format='PNG')
        return emit({'ok':True,'out':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
                     'source_sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    finally: tmp.unlink(missing_ok=True)

def plan(brief):
    req = brief.get('requirements', {})
    if req.get('exact_geometry') or req.get('state_sequence') or req.get('quantitative') or req.get('topology'):
        if req.get('official_image_available') and not req.get('state_sequence') and not req.get('new_annotations'):
            method = 'existing'; why = 'Exact object already has a verified source image; do not regenerate it.'
        else:
            method = 'svg'; why = 'Geometry, states, values or connections must remain deterministic.'
    elif req.get('real_product'):
        method = 'existing' if req.get('official_image_available') else 'svg'
        why = 'Identity and real construction need evidence; generation cannot supply missing product facts.'
    elif req.get('annotate_photo'):
        method = 'hybrid'; why = 'Preserve the verified image; put controlled labels/arrows in a separate overlay.'
    else:
        method = 'generated'; why = 'Context/material/organic scene without structural or quantitative claims.'
    return {'method':method,'reason':why,'role':'technical' if method != 'generated' else 'context',
            'notice':'Recommendation only. Agent must inspect evidence, rights, readability and tool availability.'}

def audit(manifest):
    manifest = Path(manifest).resolve(); root = manifest.parent
    data = json.loads(manifest.read_text(encoding='utf-8')); errors=[]; ids=set(); rows=[]
    for a in data.get('assets', []):
        aid = a.get('id','?')
        if aid in ids or not a.get('id'): errors.append(f'{aid}: missing/duplicate id')
        ids.add(aid)
        if a.get('method') not in METHODS: errors.append(f'{aid}: invalid method')
        if a.get('role') not in ROLES: errors.append(f'{aid}: invalid role')
        for field in ('purpose','alt_text','rights','decision_reason'):
            if not a.get(field): errors.append(f'{aid}: missing {field}')
        if a.get('method') in {'existing','hybrid'}:
            for field in ('source_page','source_url','retrieved_on','usage'):
                if not a.get(field): errors.append(f'{aid}: missing {field}')
        if a.get('method') == 'generated':
            if not a.get('generation',{}).get('prompt') or not a.get('generation',{}).get('model'):
                errors.append(f'{aid}: missing actual generation record')
            if a.get('role') == 'technical' and not (a.get('source_ids') and a.get('geometry_reviewed') is True):
                errors.append(f'{aid}: generated technical asset lacks evidence/geometry review')
        if a.get('role') == 'technical' and not a.get('source_ids'):
            errors.append(f'{aid}: technical asset has no evidence links')
        for name in ('source_page','source_url'):
            if a.get(name):
                try: clean_url(a[name])
                except ValueError as e: errors.append(f'{aid}: {e}')
        try:
            p = local(root, a.get('path')); digest = hashlib.sha256(p.read_bytes()).hexdigest()
            if digest != a.get('sha256'): errors.append(f'{aid}: asset hash mismatch')
            with Image.open(p) as im:
                im.load(); w,h = im.size
            width = float(a.get('width_mm',164))
            if width <= 0 or width > 174: raise ValueError('invalid print width')
            ppi=w/(width/25.4)
            if a.get('role') != 'reference' and ppi < (250 if a.get('role')=='technical' else 150):
                errors.append(f'{aid}: insufficient pixels at print size')
            if a.get('svg'):
                local(root, a['svg']).read_bytes()
            rows.append({'id':aid,'method':a.get('method'),'pixels':[w,h],'ppi':round(ppi,1)})
        except (OSError,ValueError,TypeError,Image.DecompressionBombError) as e: errors.append(f'{aid}: {e}')
    if not data.get('assets'): errors.append('empty image manifest')
    return {'ok':not errors,'errors':errors,'assets':rows,
            'scope':'file/provenance declarations only; not rights certification or visual approval'}

def contact(manifest, out):
    p=Path(manifest).resolve(); data=json.loads(p.read_text(encoding='utf-8')); assets=data.get('assets',[])
    size=(680,490); cols=2; rows=(len(assets)+1)//2
    sheet=Image.new('RGB',(cols*size[0],rows*size[1]),'#E9ECEF'); d=ImageDraw.Draw(sheet)
    font=ImageFont.load_default()
    for i,a in enumerate(assets):
        x=(i%cols)*size[0]; y=(i//cols)*size[1]
        im=Image.open(local(p.parent,a['path'])).convert('RGBA')
        bg=Image.new('RGBA',im.size,'white'); bg.alpha_composite(im)
        thumb=ImageOps.contain(bg.convert('RGB'),(size[0]-36,size[1]-70))
        sheet.paste(thumb,(x+(size[0]-thumb.width)//2,y+50+(size[1]-70-thumb.height)//2))
        d.text((x+18,y+18),a['id']+' / '+a['method']+' / '+a['role'],fill='#263338',font=font)
    out=Path(out); out.parent.mkdir(parents=True,exist_ok=True); sheet.save(out)
    return emit({'ok':True,'out':str(out),'assets':len(assets),'visual_reviewed':False})

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True)
    p=sub.add_parser('plan'); p.add_argument('brief'); p.add_argument('--out')
    p=sub.add_parser('check'); p.add_argument('manifest'); p.add_argument('--out')
    p=sub.add_parser('fetch'); p.add_argument('url'); p.add_argument('--out',required=True); p.add_argument('--allow-host',action='append',required=True)
    p=sub.add_parser('contact'); p.add_argument('manifest'); p.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.command=='plan': emit(plan(json.loads(Path(a.brief).read_text(encoding='utf-8'))),a.out)
    elif a.command=='check':
        report=audit(a.manifest); emit(report,a.out); return 0 if report['ok'] else 1
    elif a.command=='fetch': fetch(a.url,a.out,a.allow_host)
    else: contact(a.manifest,a.out)
    return 0
if __name__=='__main__':
    try: raise SystemExit(main())
    except (ValueError,OSError) as e: emit({'ok':False,'error':str(e)}); raise SystemExit(1)
