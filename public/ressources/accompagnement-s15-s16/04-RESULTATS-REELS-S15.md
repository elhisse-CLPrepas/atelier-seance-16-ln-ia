# Tests S15 réellement exécutés

Date de séance : 16 novembre 2026.
Outil : Python 3.14.5. Fonctions importées du script S15 original, non modifié.
Le cas fictif retiré à la demande du participant est exclu du script de suivi ; les fonctions originales restent utilisées.

Prédictions personnelles : NON RECUEILLIES. Le participant a demandé explicitement de procéder directement aux tests. Aucune prédiction rétrospective ne lui est attribuée.

| Cas | Longueur len(texte) | Observation réelle |
|---|---:|---|
| Vide | 0 | À compléter |
| Espaces seuls | 3 | À compléter |
| 400 lettres a | 400 | Longueur acceptable |
| 401 lettres a | 401 | À raccourcir |
| Étalon original 400 | 400 | Longueur acceptable |
| Étalon original 401 | 401 | À raccourcir |
| Variante A acceptée | 274 | Longueur acceptable |
| Variante B acceptée | 270 | Longueur acceptable |
| Message retenu | 208 | Longueur acceptable |

## Interprétation proposée par l’assistant

La condition est strictement supérieure à 400 : 400 est accepté ; 401 déclenche le raccourcissement. La présence est contrôlée avant la longueur : les espaces seuls donnent À compléter.
La répétition réutilise la même règle pour chaque texte. Elle ne vérifie pas les faits ; une donnée fausse peut être répétée dans toutes les sorties.
Les variantes A et B proviennent des propositions IA acceptées pendant cet échange ; ce ne sont pas des productions personnelles S14 retrouvées dans les anciens modèles.

## Relais S16

Le message retenu et ses appuis sont disponibles dans 01-SOURCES-ET-CADRAGE.md. Le public prioritaire et les six champs S16 restent à confirmer. Aucun JSON d’export S16 ni résultat de notebook S16 n’est fabriqué ici.
Décision du pilote sur la preuve complète : EN ATTENTE.
Réouverture par le participant et observation d’un tiers : NON RECUEILLIES.

## Rejouer

Depuis la racine de l’atelier :
`py -3 -X utf8 mon-dossier-challenge-module04/08-accompagnement-S15-S16/executer-tests-s15.py`
Résultats détaillés : resultats-tests-s15.json. Extrait de démonstration sans le cas retiré : sortie-demonstration-originale-s15.txt.
