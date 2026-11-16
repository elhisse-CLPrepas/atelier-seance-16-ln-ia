from pathlib import Path
import contextlib
import io
import json
import sys
root=Path('mon-dossier-challenge-module04').resolve()
out=root/'08-accompagnement-S15-S16'
nb=json.loads((root/'05-automatisation/communication-assistee.ipynb').read_text(encoding='utf-8-sig'))
codes=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
ref='Comment produire avec méthode ? — Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle. Consultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/'
first=codes[0].replace('MODE_SOURCE = "exemple"','MODE_SOURCE = "fichier"').replace('RACINE_CANDIDAT = ""','RACINE_CANDIDAT = '+repr(str(root))).replace('TEXTE_HUMAIN_S14 = ""','TEXTE_HUMAIN_S14 = '+repr(ref))
second=codes[1].replace('VERSION HUMAINE S14','MESSAGE DE RÉFÉRENCE ACCEPTÉ (PROPOSITION IA VALIDÉE, PAS DE VERSION HUMAINE S14 ANTÉRIEURE)')
namespace={}
buffer=io.StringIO()
with contextlib.redirect_stdout(buffer):
    print('S16 : exécution Python des trois premières cellules de code ; aucun noyau Jupyter utilisé.')
    print('Adaptations en mémoire : mode fichier, racine locale, message de référence accepté et libellé de provenance. Notebook original préservé.')
    for i,code in enumerate([first,second,codes[2]],1):
        print('\nCELLULE DE CODE',i)
        exec(compile(code,f'S16-cellule-{i}','exec'),namespace)
if namespace['initiales'] is None:
    raise RuntimeError('Variantes non produites')
text=buffer.getvalue()
(out/'05-SORTIES-INITIALES-S16.txt').write_text(text,encoding='utf-8')
variants=namespace['initiales']
(out/'variantes-initiales-s16.json').write_text(json.dumps({'statut':'BROUILLON — À RELIRE','provenance':'Trois premières cellules S16 exécutées en Python, adaptations en mémoire documentées','variantes':variants,'mesures_python':{k:len(v) for k,v in variants.items()}},ensure_ascii=False,indent=2),encoding='utf-8')
print(text)
print('LONGUEURS', {k:len(v) for k,v in variants.items()})
assert (out/'05-SORTIES-INITIALES-S16.txt').read_text(encoding='utf-8') == text
print('Sorties enregistrées et relues techniquement. Cellules 4 à 6 non exécutées ; aucune correction humaine inventée.')
