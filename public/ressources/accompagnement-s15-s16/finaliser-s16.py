from pathlib import Path
import contextlib
import io
import json
import runpy
import re
root=Path('mon-dossier-challenge-module04').resolve()
out=root/'08-accompagnement-S15-S16'
buffer=io.StringIO()
with contextlib.redirect_stdout(buffer):
    state=runpy.run_path(str(out/'comparer-public-s16.py'))
env=state['env']
nb=json.loads((root/'05-automatisation/communication-assistee.ipynb').read_text(encoding='utf-8-sig'))
codes=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
final='Comment produire avec méthode ?\n\nVous débutez en production avancée IA ? Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle, tout en gardant le pilotage humain.\n\nConsultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/'
params={
'AVANT':env['essai']['versions']['professionnel'],
'APRES':final,
'MOTIF':'Adaptation LinkedIn proposée par l’assistant puis explicitement validée par le participant : oui je valide. Remplacer les étiquettes Objet et Public par le titre retenu et une adresse directe au lecteur ; rappeler le pilotage humain.',
'APPUI':'Guide Situation-Actuelle-IA V5, page 2 : sous-titre mentionnant pilotage humain et production avec méthode ; page 4 : produire et contrôler. Public précisé et adaptation finale acceptés dans le chat.',
'CANAL':'LinkedIn'}
code5=codes[4]
for key,value in params.items():
    code5=code5.replace(key+' = ""',key+' = '+repr(value),1)
# Ne pas attribuer de rédaction personnelle S14 ou de prédiction personnelle inexistante.
code6=codes[5].replace('## Message humain S14','## Message de référence S15 — proposition IA acceptée').replace('## Ma correction humaine','## Correction proposée par assistant puis validée par participant').replace('## Ma prédiction et le résultat','## Prédiction de assistant et résultat — prédiction participant non recueillie')
result=io.StringIO()
with contextlib.redirect_stdout(result):
    print('S16 : cellules 5 et 6 réellement exécutées avec Python ; notebook original conservé. Libellés de provenance adaptés explicitement.')
    exec(compile(code5,'S16-cellule-5','exec'),env)
    if env['revision'] is None:
        raise RuntimeError('Correction non produite')
    exec(compile(code6,'S16-cellule-6','exec'),env)
if env['revision']['texte'] != final:
    raise RuntimeError('Texte exporté différent de la correction validée')
target=root/'04-communication/variantes-communication-projet.md'
assert final in target.read_text(encoding='utf-8')
(out/'07-EXPORT-FINAL-S16.txt').write_text(result.getvalue(),encoding='utf-8')
(out/'message-linkedin-valide.txt').write_text(final+'\n',encoding='utf-8')
metadata={'statut':'BROUILLON — À RELIRE ; adaptation validée dans le chat, non publiée','provenance':'Proposition assistant acceptée par participant le 16 novembre 2026','revision':env['revision'],'sha256':env['empreinte'],'reouverture_technique':True,'reouverture_participant':None,'prediction_participant':None,'decision_pilote_preuve':None}
(out/'07-EXPORT-FINAL-S16.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
# Actualiser uniquement entrée S16 du portfolio.
p=root/'07-portfolio/preuves-module-04.md'
s=p.read_text(encoding='utf-8-sig')
entry='''## S16

Preuve : preuve-16-notebook-communication-assistee
Fichier : ../04-communication/variantes-communication-projet.md
Date du relevé technique : 16 novembre 2026
Observation vérifiable : six cellules de code S16 exécutées en Python, avec adaptations en mémoire documentées ; aucune session Jupyter. Public précisé : seule la variante professionnelle est modifiée. Correction LinkedIn proposée par assistant puis explicitement validée par participant.
Export : Markdown écrit puis relu techniquement ; version antérieure conservée dans 04-communication/historique par la fonction originale.
Message final : LONGUEUR points de code ; Longueur acceptable ; une occurrence exacte de action.
Sortie de vérification : ../08-accompagnement-S15-S16/07-EXPORT-FINAL-S16.txt ; SHA-256 et provenance : 07-EXPORT-FINAL-S16.json dans le même dossier.
Prédiction personnelle et rédaction humaine S14 antérieure : non recueillies ; les propositions assistant sont identifiées.
Réouverture par participant et observation de tiers : À COMPLÉTER.
Statut : EXPORT RÉEL VÉRIFIÉ TECHNIQUEMENT — MESSAGE NON PUBLIÉ
Décision du pilote sur la preuve : EN ATTENTE

'''.replace('LONGUEUR',str(len(final)))
s=re.sub(r'## S16\n.*?(?=## Complément de suivi S15)',lambda m:entry,s,flags=re.S)
p.write_text(s,encoding='utf-8')
print(result.getvalue())
print('MESSAGE FINAL :',len(final),'points de code ;',env['revision']['controle'])
