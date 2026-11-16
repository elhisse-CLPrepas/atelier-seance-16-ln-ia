from pathlib import Path
import importlib.util
import json
import platform
import sys

out = Path(__file__).resolve().parent
root = out.parent
original = root / '06-ressources/seance-15/ressources/demo/tester-regles-s15.py'
spec = importlib.util.spec_from_file_location('regles_s15', original)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
cas = json.loads(original.with_name('cas-regles-s15.json').read_text(encoding='utf-8-sig'))
assert cas['seuil'] == 400
url = 'https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/'
a = 'Comment produire avec l’IA tout en gardant le pilotage humain ? Le guide Situation-Actuelle-IA propose une démarche : comprendre, produire, contrôler et transmettre. Découvrez la démarche sur le mini-site :\n' + url
b = 'Produire vite avec l’IA demande aussi de vérifier. Le guide Situation-Actuelle-IA rappelle que la vitesse ne prouve pas la qualité. Découvrez une démarche de production avec méthode et contrôle humain :\n' + url
retenu = 'Comment produire avec méthode ? — Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle. Consultez le mini-site : ' + url
samples = [('Vide', ''), ('Espaces seuls', '   '), ('400 lettres a', 'a'*400), ('401 lettres a', 'a'*401), ('Étalon original 400', cas['etalon']*40), ('Étalon original 401', cas['etalon']*40+cas['suffixe']), ('Variante A acceptée', a), ('Variante B acceptée', b), ('Message retenu', retenu)]
rows = []
for name, value in samples:
    verdict = 'À compléter' if not value.strip() else module.verdict_longueur(value, cas)
    rows.append({'cas': name, 'texte': value, 'longueur_python': len(value), 'prediction': 'NON RECUEILLIE — exécution directe demandée', 'observation': verdict, 'outil': 'Python 3 / fonctions du script S15 fourni'})
(out/'resultats-tests-s15.json').write_text(json.dumps({'date_seance':'2026-11-16', 'python':sys.version,'plateforme':platform.platform(),'seuil':cas['seuil'],'resultats':rows}, ensure_ascii=False, indent=2),encoding='utf-8')
lines = ['# Tests S15 réellement exécutés', '', 'Date de séance : 16 novembre 2026.', 'Outil : Python '+platform.python_version()+'. Fonctions importées du script S15 original, non modifié.', 'Le cas fictif retiré à la demande du participant est exclu du script de suivi ; les fonctions originales restent utilisées.', '', 'Prédictions personnelles : NON RECUEILLIES. Le participant a demandé explicitement de procéder directement aux tests. Aucune prédiction rétrospective ne lui est attribuée.', '', '| Cas | Longueur len(texte) | Observation réelle |', '|---|---:|---|']
lines += [f"| {r['cas']} | {r['longueur_python']} | {r['observation']} |" for r in rows]
lines += ['', '## Interprétation proposée par l’assistant', '', 'La condition est strictement supérieure à 400 : 400 est accepté ; 401 déclenche le raccourcissement. La présence est contrôlée avant la longueur : les espaces seuls donnent À compléter.', 'La répétition réutilise la même règle pour chaque texte. Elle ne vérifie pas les faits ; une donnée fausse peut être répétée dans toutes les sorties.', 'Les variantes A et B proviennent des propositions IA acceptées pendant cet échange ; ce ne sont pas des productions personnelles S14 retrouvées dans les anciens modèles.', '', '## Relais S16', '', 'Le message retenu et ses appuis sont disponibles dans 01-SOURCES-ET-CADRAGE.md. Le public prioritaire et les six champs S16 restent à confirmer. Aucun JSON d’export S16 ni résultat de notebook S16 n’est fabriqué ici.', 'Décision du pilote sur la preuve complète : EN ATTENTE.', 'Réouverture par le participant et observation d’un tiers : NON RECUEILLIES.', '', '## Rejouer', '', 'Depuis la racine de l’atelier :', '`py -3 -X utf8 mon-dossier-challenge-module04/08-accompagnement-S15-S16/executer-tests-s15.py`', 'Résultats détaillés : resultats-tests-s15.json. Extrait de démonstration sans le cas retiré : sortie-demonstration-originale-s15.txt.']
report = '\n'.join(lines)+'\n'
(out/'04-RESULTATS-REELS-S15.md').write_text(report,encoding='utf-8')
assert json.loads((out/'resultats-tests-s15.json').read_text(encoding='utf-8'))['resultats'] == rows
assert (out/'04-RESULTATS-REELS-S15.md').read_text(encoding='utf-8') == report
print(report)
print('Relecture technique des fichiers JSON et Markdown : réussie. Aucun constat humain de réouverture déduit.')
