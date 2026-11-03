"""Validate the published native package against its release specification."""
from pathlib import Path
import hashlib
import json
import zipfile
from PIL import Image

root = Path(__file__).resolve().parent.parent
package = root / 'pet/deepseek-chan'
spec = json.loads((root / 'docs/animation-spec.json').read_text(encoding='utf-8'))
pet = json.loads((package / 'pet.json').read_text(encoding='utf-8'))
assert pet['id'] == 'deepseek-chan'
assert pet['spritesheetPath'] == 'spritesheet.webp'
encoded = (package / pet['spritesheetPath']).read_bytes()
assert hashlib.sha256(encoded).hexdigest() == spec['sha256'], 'Atlas checksum mismatch'
with Image.open(package / pet['spritesheetPath']) as image:
    assert image.size == (spec['width'], spec['height']), 'Unexpected atlas size'
    rgba = image.convert('RGBA')
    for state in spec['states']:
        assert len(state['durations_ms']) == state['frames']
        for column in range(8):
            x, y = column * 192, state['row'] * 208
            alpha = rgba.crop((x, y, x + 192, y + 208)).getchannel('A')
            occupied = alpha.getbbox() is not None
            assert occupied == (column < state['frames']), f'Invalid occupancy: row {state["row"]}, column {column}'
            if occupied:
                assert alpha.getextrema() == (0, 255), 'Expected transparency and opaque artwork'
with zipfile.ZipFile(root / 'releases/deepseek-chan-v1.0.0.zip') as archive:
    assert set(archive.namelist()) == {'deepseek-chan/pet.json', 'deepseek-chan/spritesheet.webp'}
    for filename in ['pet.json', 'spritesheet.webp']:
        assert archive.read('deepseek-chan/' + filename) == (package / filename).read_bytes()
print('PASS: package, atlas checksum, 57 frames, 15 empty cells, timings, and ZIP contents')
