#!/usr/bin/env python3
"""Offline image-workflow regression tests; never substitutes fixtures for real research."""
import importlib.util, tempfile, hashlib, json, unittest, copy
from pathlib import Path
from unittest.mock import patch
from PIL import Image
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('media',HERE/'media.py');media=importlib.util.module_from_spec(s);s.loader.exec_module(media)
class MediaTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        Image.new('RGB',(2000,1100),'white').save(self.root/'photo.png')
        self.a={'id':'A1','path':'photo.png','method':'svg','role':'technical','purpose':'fixture','decision_reason':'fixture','alt_text':'fixture','rights':'fixture only','source_ids':['S1'],'sha256':hashlib.sha256((self.root/'photo.png').read_bytes()).hexdigest(),'width_mm':164}
    def tearDown(self):self.tmp.cleanup()
    def audit(self,a=None):
        p=self.root/'media.json';p.write_text(json.dumps({'assets':[a or self.a]}));return media.audit(p)
    def test_registry_fixture(self):self.assertTrue(self.audit()['ok'])
    def test_path_escape(self):
        a=copy.deepcopy(self.a);a['path']='../bad.png';self.assertFalse(self.audit(a)['ok'])
    def test_hash_change(self):
        a=copy.deepcopy(self.a);a['sha256']='wrong';self.assertFalse(self.audit(a)['ok'])
    def test_zero_width(self):
        a=copy.deepcopy(self.a);a['width_mm']=0;self.assertFalse(self.audit(a)['ok'])
    def test_missing_rights(self):
        a=copy.deepcopy(self.a);a.pop('rights');self.assertFalse(self.audit(a)['ok'])
    def test_existing_needs_provenance(self):
        a=copy.deepcopy(self.a);a['method']='existing';self.assertFalse(self.audit(a)['ok'])
    def test_generated_needs_real_record(self):
        a=copy.deepcopy(self.a);a['method']='generated';a['role']='context';self.assertFalse(self.audit(a)['ok'])
    def test_generated_context_allowed(self):
        a=copy.deepcopy(self.a);a.update(method='generated',role='context',source_ids=[],generation={'model':'fixture-not-live','prompt':'offline fixture'});self.assertTrue(self.audit(a)['ok'])
    def test_generated_structure_needs_geometry_review(self):
        a=copy.deepcopy(self.a);a.update(method='generated',generation={'model':'fixture-not-live','prompt':'fixture'});self.assertFalse(self.audit(a)['ok']);a['geometry_reviewed']=True;self.assertTrue(self.audit(a)['ok'])
    def test_state_sequence_routes_svg(self):self.assertEqual(media.plan({'requirements':{'state_sequence':True}})['method'],'svg')
    def test_real_product_not_generated(self):self.assertEqual(media.plan({'requirements':{'real_product':True}})['method'],'svg')
    def test_existing_official_image_preferred(self):self.assertEqual(media.plan({'requirements':{'real_product':True,'official_image_available':True}})['method'],'existing')
    def test_context_routes_generation(self):self.assertEqual(media.plan({'requirements':{'context_scene':True}})['method'],'generated')
    def test_overlay_routes_hybrid(self):self.assertEqual(media.plan({'requirements':{'annotate_photo':True}})['method'],'hybrid')
    def test_url_credentials_and_signatures_rejected(self):
        for url in ['http://example.org/a','https://a:b@example.org/a','https://example.org/a?token=x','https://example.org/a?X-Amz-Signature=x']:
            with self.assertRaises(ValueError):media.clean_url(url)
    def test_private_network_rejected(self):
        with patch('socket.getaddrinfo',return_value=[(2,1,6,'',('127.0.0.1',443))]):
            with self.assertRaises(ValueError):media.check_remote('https://example.org/a',{'example.org'})
    def test_redirect_host_not_approved(self):
        with self.assertRaises(ValueError):media.check_remote('https://other.example/a',{'example.org'})
    def test_transparency_contact_sheet(self):
        Image.new('RGBA',(2000,1100),(255,0,0,0)).save(self.root/'photo.png')
        p=self.root/'media.json';p.write_text(json.dumps({'assets':[self.a]}));out=self.root/'sheet.png';media.contact(p,out);self.assertTrue(out.is_file());self.assertEqual(Image.open(out).getpixel((340,260)),(255,255,255))
if __name__=='__main__':unittest.main(verbosity=2)
