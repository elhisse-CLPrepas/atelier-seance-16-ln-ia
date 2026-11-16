from pathlib import Path
import contextlib
import io
import json
import runpy
root=Path('mon-dossier-challenge-module04').resolve()
out=root/'08-accompagnement-S15-S16'
public='Professionnels et formateurs débutant en production avancée IA'
appui='Public proposé par assistant puis explicitement accepté par le participant : je valide le public. Échange S16 du 16 novembre 2026.'
buffer=io.StringIO()
with contextlib.redirect_stdout(buffer):
    env=runpy.run_path(str(out/'demarrer-s16.py'))['namespace']
# Réutiliser la fonction de comparaison originale ; la prédiction requise est étiquetée assistant.
nb=json.loads((root/'05-automatisation/communication-assistee.ipynb').read_text(encoding='utf-8-sig'))
code=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code'][3]
code=code.replace('NOUVELLE = ""','NOUVELLE = '+repr(public))
code=code.replace('ORIGINE = ""','ORIGINE = '+repr(appui))
code=code.replace('PREDICTION = ""','PREDICTION = '+repr('Prédiction de l’assistant, non du participant : seul le format professionnel changera, car seul ce gabarit affiche le champ public.'))
result=io.StringIO()
with contextlib.redirect_stdout(result):
    print('S16 — cellule 4 exécutée avec Python. Public confirmé ; aucune prédiction personnelle recueillie. Prédiction technique de l’assistant explicitement identifiée.')
    exec(compile(code,'S16-cellule-4','exec'),env)
if env['essai'] is None:
    raise RuntimeError('Comparaison non produite')
data=env['essai']
data['prediction_participant']=None
data['provenance_prediction']='assistant'
(out/'06-COMPARAISON-PUBLIC-S16.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'06-COMPARAISON-PUBLIC-S16.txt').write_text(result.getvalue(),encoding='utf-8')
lines=['# S16 — public précisé et comparaison réelle','','Public confirmé : '+public+'.','Justification : '+appui,'Prédiction personnelle : non recueillie. La prédiction inscrite dans le test provient de l’assistant.','','| Variante | Résultat après modification | Longueur Python | Action exacte |','|---|---|---:|---:|']
for k in env['FORMATS']:
    m=data['controles'][k]
    lines.append(f"| {k} | {'Modifiée' if k in data['modifies'] else 'Identique'} | {m['longueur']} | {m['action_exacte']} |")
lines+=['','Seul le gabarit professionnel utilise le champ public. Les deux autres sorties ne changent pas. Les trois restent sous le seuil de 400.','Le besoin confirmé et l’action de consultation du mini-site restent identiques.','','## Brouillon professionnel après changement','',data['versions']['professionnel'],'','## Correction proposée pour LinkedIn','','Remplacer les lignes Objet et Public par le titre retenu « Comment produire avec méthode ? », puis intégrer le public dans une phrase destinée au lecteur. Cette adaptation éditoriale est une proposition de l’assistant, pas une correction humaine déjà validée.','Cellules 5 et 6 : pas encore exécutées. Décision du pilote : EN ATTENTE.']
(out/'06-COMPARAISON-PUBLIC-S16.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines))

