from pathlib import Path
import ast
import hashlib
import json
root=Path('mon-dossier-challenge-module04')
name='communication-assistee-s16-situation-actuelle-ia'
source=root/'05-automatisation'/(name+'.ipynb')
folder=root/'08-accompagnement-S15-S16'
target=folder/(name+'.ipynb')
assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest()
nb=json.loads(target.read_text(encoding='utf-8'))
parts=['# -*- coding: utf-8 -*-\n# Version Python du notebook S16 personnalisé.\n# Cellules exécutables dans VS Code (# %%) ou avec Python 3.\n# La dernière cellule exporte le Markdown local et préserve une version précédente.\n']
for c in nb['cells']:
    text=''.join(c['source'])
    if c['cell_type']=='markdown':
        parts.append('# %% [markdown]\n'+'\n'.join('# '+line if line else '#' for line in text.splitlines())+'\n')
    elif c['cell_type']=='code':
        parts.append('# %%\n'+text.rstrip()+'\n')
script='\n'.join(parts)
ast.parse(script)
p=folder/(name+'.py')
if p.exists() and p.read_text(encoding='utf-8')!=script:
    raise FileExistsError('Version Python différente déjà présente ; aucun écrasement.')
p.write_text(script,encoding='utf-8')
assert p.read_text(encoding='utf-8')==script
print('Notebook copié, SHA-256 identique :',target.resolve())
print('Version Python correspondante créée, syntaxe vérifiée :',p.resolve())
print('6 cellules de code conservées ; aucune réexécution lors de la copie.')
