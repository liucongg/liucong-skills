#!/usr/bin/env python3
"""Audit a DOCX for personal metadata, hidden text and local-path leakage.

Read-only. Pass project-specific identity strings with --blocked-term.
Scientific correctness, image content and visual layout require separate review.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
LOCAL_PATH = re.compile(r'(?:/Users/[^/\s]+/|/home/[^/\s]+/|[A-Za-z]:\\Users\\)', re.I)


def audit(path, blocked_terms=()):
    path = Path(path)
    issues = []
    paragraphs = 0
    with zipfile.ZipFile(path) as package:
        if package.testzip():
            issues.append({'kind': 'invalid_zip'})
        if sum(p.file_size for p in package.infolist()) > 150 * 1024 * 1024:
            raise ValueError('DOCX decompressed size limit exceeded')
        for name in package.namelist():
            if not name.endswith('.xml') and not name.endswith('.rels'):
                continue
            root = ET.fromstring(package.read(name))
            if name == 'docProps/core.xml':
                for node in root:
                    key = node.tag.rsplit('}', 1)[-1]
                    if key in {'creator', 'lastModifiedBy', 'description', 'keywords'} and (node.text or '').strip():
                        issues.append({'part': name, 'kind': 'non_neutral_metadata', 'field': key})
            if name.startswith('word/'):
                for p in root.iter(W + 'p'):
                    text = ''.join(n.text or '' for n in p.iter() if n.tag in {W+'t', W+'delText', W+'instrText'})
                    paragraphs += 1
                    if LOCAL_PATH.search(text):
                        issues.append({'part': name, 'kind': 'personal_path_in_text'})
                    for term in blocked_terms:
                        if term and term.casefold() in text.casefold():
                            issues.append({'part': name, 'kind': 'blocked_identity_term'})
                for node in root.iter():
                    if node.tag in {W+'ins', W+'del', W+'moveFrom', W+'moveTo', W+'comment'}:
                        issues.append({'part': name, 'kind': 'unresolved_review_content'})
                    if node.tag == W+'vanish' and node.get(W+'val', 'true').lower() not in {'0','false','off'}:
                        issues.append({'part': name, 'kind': 'hidden_text'})
            if name.endswith('.rels'):
                for rel in root:
                    target = rel.get('Target', '')
                    if rel.get('TargetMode') == 'External' and (target.lower().startswith('file:') or LOCAL_PATH.search(target)):
                        issues.append({'part': name, 'kind': 'external_personal_path'})
            if name.startswith('docProps/'):
                text = ''.join(root.itertext())
                if LOCAL_PATH.search(text):
                    issues.append({'part': name, 'kind': 'personal_path_in_properties'})
                if any(t and t.casefold() in text.casefold() for t in blocked_terms):
                    issues.append({'part': name, 'kind': 'blocked_identity_in_properties'})
    return {'ok': not issues, 'file': path.name,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'paragraphs_checked': paragraphs, 'issues': issues,
            'scope': 'Metadata and XML text only; not scientific or visual certification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('docx')
    parser.add_argument('--blocked-term', action='append', default=[])
    parser.add_argument('--out')
    args = parser.parse_args()
    report = audit(args.docx, args.blocked_term)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text+'\n', encoding='utf-8')
    print(text)
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
