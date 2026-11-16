"""Rejoue le cas pédagogique dans un dossier temporaire isolé."""
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile

root = Path(__file__).resolve().parent.parent
notebook = json.loads((root / 'public/ressources/accompagnement-s15-s16/rejouer-exemple-s16.ipynb').read_text(encoding='utf-8'))
with tempfile.TemporaryDirectory() as tmp:
    previous = Path.cwd()
    os.chdir(tmp)
    try:
        personal = Path('04-communication/variantes-communication-projet.md')
        personal.parent.mkdir()
        personal.write_bytes(b'PROJET PERSONNEL A CONSERVER')
        namespace = {}
        with contextlib.redirect_stdout(io.StringIO()):
            for cell in notebook['cells']:
                if cell['cell_type'] == 'code':
                    exec(compile(''.join(cell['source']), 'rejouer-exemple-s16.ipynb', 'exec'), namespace)
        assert personal.read_bytes() == b'PROJET PERSONNEL A CONSERVER'
        output = Path('demo-situation-actuelle-ia/04-communication/variantes-communication-exemple.md')
        assert output.is_file()
        revision = namespace['revision']
        assert len(revision['texte']) == 284
        assert revision['texte'] in output.read_text(encoding='utf-8')
        assert namespace['essai']['modifies'] == ['professionnel']
    finally:
        os.chdir(previous)
print('Six cellules rejouées : 284 points de code, export fictif isolé, projet personnel intact.')
