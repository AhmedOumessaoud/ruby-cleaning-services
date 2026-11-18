"""Static integrity checks. Run: python verify.py"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from PIL import Image
import json

ROOT = Path(__file__).resolve().parent

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.assets, self.anchors, self.services = [], [], [], []
        self.images = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if 'src' in a: self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet': self.assets.append(a['href'])
        if tag == 'a' and a.get('href', '').startswith('#'): self.anchors.append(a['href'][1:])
        if tag == 'img':
            assert 'alt' in a, 'Image without alt attribute'
            if a.get('src'): self.images += 1
        if 'data-service' in a: self.services.append(a['data-service'])

page = Page()
page.feed((ROOT / 'index.html').read_text(encoding='utf-8'))
assert len(page.ids) == len(set(page.ids)), 'Duplicate IDs'
assert all(anchor in page.ids for anchor in page.anchors), 'Broken local navigation'
for asset in set(page.assets):
    assert (ROOT / unquote(asset)).is_file(), f'Missing asset: {asset}'
    if Path(asset).suffix in ('.png', '.jpg', '.webp'):
        with Image.open(ROOT / asset) as image: image.verify()
assert len(page.services) == 9 and len(set(page.services)) == 9
script = (ROOT / 'js/main.js').read_text(encoding='utf-8')
assert '212668192422' in script and 'encodeURIComponent(message)' in script
assert 'backTop.addEventListener' in script
print(json.dumps({'result': 'passed', 'local_assets': len(set(page.assets)), 'images': page.images, 'service_messages': len(page.services), 'navigation_targets': len(set(page.anchors)), 'browser_layout_verification': 'not available'}, indent=2))
