from pathlib import Path
import ast
import contextlib
import copy
import hashlib
import io
import json
import os
import sys

root=Path('mon-dossier-challenge-module04').resolve()
out=root/'08-accompagnement-S15-S16'
original=root/'05-automatisation/communication-assistee.ipynb'
original_hash=hashlib.sha256(original.read_bytes()).hexdigest()
nb=json.loads(original.read_text(encoding='utf-8-sig'))
codes=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
fiche=json.loads((root/'04-communication/donnees-pour-s16.json').read_text(encoding='utf-8'))
comparison=json.loads((out/'06-COMPARAISON-PUBLIC-S16.json').read_text(encoding='utf-8'))
validated=json.loads((out/'07-EXPORT-FINAL-S16.json').read_text(encoding='utf-8'))
reference=(out/'message-linkedin-valide.txt').read_text(encoding='utf-8').strip()
# La référence avant correction est le message accepté de S15, déjà enregistré.
reference_s15='Comment produire avec méthode ? — Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle. Consultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/'
helper=codes[0][codes[0].index('from pathlib import Path'):codes[0].index('racine = dossier_de_travail')]
code1='''# 1. Données réelles de S15 et appuis, embarqués pour rendre le carnet portable.
# Aucun cas fictif, clé API ou accès réseau requis. Python 3, bibliothèque standard.
MODE_SOURCE = "export S15 embarqué"
TEXTE_REFERENCE_S15 = REFERENCE
'''.replace('REFERENCE\n',repr(reference_s15)+'\n')+helper+'''
# Racine : dossier candidat si détecté, sinon dossier courant.
# Vous pouvez remplacer cette recherche par Path("chemin/du/dossier").resolve().
base = Path.cwd().resolve()
candidats = [base, *base.parents]
racine = next((p for p in candidats if (p / "04-communication").is_dir()), None)
if racine is None:
    racine = next((p / "mon-dossier-challenge-module04" for p in candidats
                   if (p / "mon-dossier-challenge-module04" / "04-communication").is_dir()), base)
fiche = FICHE
origine_fiche = "Export S15 réel embarqué ; fonction buildHandoff, métadonnées Python documentées."
texte_s14 = TEXTE_REFERENCE_S15  # Nom technique hérité ; ce texte est une proposition IA acceptée.
donnees, appuis = lire_fiche(fiche)
source_initiale = initiales = essai = revision = None
regle_s15 = fiche.get("regle") or "Règle du support S15."
print("Dossier de travail :", racine)
print("Source : export réel S15 embarqué ; message de référence IA accepté.")
for champ in CHAMPS:
    print(f"{champ} : {donnees[champ]} | Appui : {appuis[champ]}")
print("Règle reprise de S15 :", regle_s15)
'''.replace('fiche = FICHE', 'fiche = '+repr(fiche))
code2=codes[1].replace('VERSION HUMAINE S14','RÉFÉRENCE S15 — PROPOSITION IA ACCEPTÉE').replace('votre version humaine S14','le message de référence S15')
code3=codes[2]
code4=codes[3]
params={'NOUVELLE':comparison['donnees']['public'],'ORIGINE':comparison['origine'],'PREDICTION':comparison['prediction']}
for key,value in params.items():
    code4=code4.replace(key+' = ""',key+' = '+repr(value),1)
code5=codes[4]
for key,value in {'AVANT':validated['revision']['avant'],'APRES':validated['revision']['apres'],'MOTIF':validated['revision']['motif'],'APPUI':validated['revision']['appui'],'CANAL':validated['revision']['canal']}.items():
    code5=code5.replace(key+' = ""',key+' = '+repr(value),1)
code6=codes[5].replace('## Message humain S14','## Référence S15 — proposition IA acceptée').replace('## Ma correction humaine','## Correction proposée par assistant et validée par participant').replace('## Ma prédiction et le résultat','## Prédiction assistant et résultat — prédiction participant non recueillie').replace('Enregistrez 05-automatisation/communication-assistee.ipynb avec ses sorties.','Enregistrez ce carnet avec ses sorties. Le message reste non publié.')
texts=[
'''# S16 — Production avancée IA avec méthode

**Projet : Situation-Actuelle-IA · Canal : LinkedIn · Travail du 16 novembre 2026.**

Carnet personnalisé à six cellules de code, fondé sur le support S16 original. Les cellules sont exécutées de haut en bas sous Python et leurs sorties sont enregistrées. Aucun noyau Jupyter n’a été utilisé lors de la génération.

**Résultats :** seule la variante professionnelle change lorsque le public est précisé ; le message LinkedIn corrigé compte **284 points de code** et conserve une occurrence exacte de l’action.

Les textes et la correction ont été proposés par l’assistant puis acceptés par le participant. La prédiction technique est celle de l’assistant ; aucune prédiction personnelle ni rédaction humaine S14 antérieure n’est inventée. La décision du pilote sur la preuve et la réouverture personnelle restent en attente. Aucun message publié.

## Utilisation
Ouvrir ce fichier dans Jupyter ou VS Code, choisir un noyau Python 3 et exécuter les cellules dans l’ordre. Seule la bibliothèque standard est nécessaire. Les données sont embarquées ; aucune connexion réseau n’est requise. La dernière cellule écrit un Markdown local et conserve une ancienne version si nécessaire.

## Sources
Guide V5 local : `../01-exemple-sa-ia/guide-situation-actuelle-IA-publication-V5.pdf`, pages 2 et 4 ; statut page 28 : « Prêt pour relecture humaine finale ». Public, besoin et correction confirmés dans le chat ; export S15 : `../04-communication/donnees-pour-s16.json`.
''',
'## 1. Charger les six champs et leurs appuis\n\nLes données initiales conservent le public général pour permettre une comparaison réelle avant/après. Le public précisé accepté sera appliqué en cellule 4. Le champ `format` désigne la variante professionnelle ; le canal est LinkedIn.',
'## 2. Comparer le message de référence et le gabarit\n\nLe message de référence provient des propositions IA acceptées pendant S15.',
'## 3. Produire les trois variantes\n\nLes gabarits court, accessible et professionnel utilisent des champs différents. Tous les textes sont des brouillons.',
'## 4. Modifier le public et contrôler\n\nPublic confirmé : **Professionnels et formateurs débutant en production avancée IA**. Prédiction fournie par l’assistant et explicitement étiquetée. Une prédiction personnelle n’a pas été recueillie avant ce test.',
'## 5. Appliquer la correction LinkedIn validée\n\nLe participant a accepté cette adaptation dans le chat. Le code conserve AVANT / APRÈS / MOTIF / APPUI et vérifie la longueur et une occurrence exacte de l’action. Ces contrôles ne prouvent pas la vérité du contenu.',
'## 6. Exporter et relire le Markdown\n\nLa dernière cellule écrit `04-communication/variantes-communication-projet.md` dans la racine détectée, conserve une ancienne version si nécessaire, relit le résultat et calcule son SHA-256. Il s’agit d’une relecture technique, distincte d’une réouverture par le participant.'
]
def cell(kind,text,ident):
    d={'cell_type':kind,'id':ident,'metadata':{},'source':text.splitlines(keepends=True)}
    if kind=='code': d.update(execution_count=None,outputs=[])
    return d
cells=[cell('markdown',texts[0],'s16-introduction')]
for i,code in enumerate([code1,code2,code3,code4,code5,code6],1):
    ast.parse(code)
    cells.extend([cell('markdown',texts[i],f's16-etape-{i}'),cell('code',code,f's16-code-{i}')])
namespace={'__name__':'__main__'}
previous=Path.cwd()
os.chdir(root/'05-automatisation')
try:
    count=0
    for c in cells:
        if c['cell_type']!='code': continue
        count+=1
        stdout=io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exec(compile(''.join(c['source']),f's16-cellule-{count}','exec'),namespace)
        c['execution_count']=count
        c['outputs']=[{'output_type':'stream','name':'stdout','text':stdout.getvalue().splitlines(keepends=True)}]
finally:
    os.chdir(previous)
assert namespace['revision']['texte']==reference
assert namespace['revision']['controle']['longueur']==284
assert namespace['essai']['modifies']==['professionnel']
notebook={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':sys.version.split()[0]},'ln_ia':{'execution':'Python exec top-to-bottom, stdout réel ; pas de noyau Jupyter','prediction_participant':None,'provenance':'Support S16 adapté au projet et aux validations du chat'}},'nbformat':4,'nbformat_minor':5}
target=root/'05-automatisation/communication-assistee-s16-situation-actuelle-ia.ipynb'
if target.exists(): raise FileExistsError('Carnet déjà présent : ne pas écraser sans comparaison.')
target.write_text(json.dumps(notebook,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
# Vérification structurelle explicite en absence de nbformat et de Jupyter.
loaded=json.loads(target.read_text(encoding='utf-8'))
assert loaded['nbformat']==4 and loaded['nbformat_minor']==5
assert len({c['id'] for c in loaded['cells']})==len(loaded['cells'])
cc=[c for c in loaded['cells'] if c['cell_type']=='code']
assert [c['execution_count'] for c in cc]==list(range(1,7))
for c in loaded['cells']:
    assert isinstance(c['metadata'],dict) and all(isinstance(s,str) for s in c['source'])
    if c['cell_type']=='code':
        ast.parse(''.join(c['source']))
        assert c['outputs'] and all(o['output_type']=='stream' for o in c['outputs'])
assert hashlib.sha256(original.read_bytes()).hexdigest()==original_hash
(out/'08-VERIFICATION-NOTEBOOK-S16.txt').write_text('Notebook : '+str(target)+'\nSix cellules exécutées en ordre avec Python '+sys.version.split()[0]+'.\nJSON, structure nbformat 4.5, identifiants, syntaxe et sorties vérifiés ; bibliothèque nbformat absente.\nMessage final : 284 points de code ; identique au texte validé. Original conservé.\nAperçu visuel Jupyter non vérifié : aucun noyau/visualiseur Jupyter installé. Pour contrôle visuel : ouvrir le fichier dans Jupyter ou VS Code, sélectionner Python 3 puis Exécuter tout.\n',encoding='utf-8')
print('CRÉÉ :',target)
print('Cellules :',len(cells),'dont',len(cc),'cellules de code exécutées ; sorties sauvegardées.')
print('Message final :',namespace['revision']['controle'])
print('Original intact. Aperçu visuel Jupyter non vérifié.')
