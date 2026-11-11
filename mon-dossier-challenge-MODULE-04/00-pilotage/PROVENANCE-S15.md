# Provenance du dossier S15

Préparation locale du 9 novembre 2026.

## Origine

- Base : `atelier-seance-14-ln-ia/mon-dossier-challenge-module04`, commit `5f7bcbf`.
- Cette base contient les commits S13 `76b8a49` et `3f6b766`.
- Clone local avec `--no-hardlinks`, sans modification des dossiers S13/S14 ni reprise de leurs sauvegardes ignorées.
- Distant `origin` : `https://github.com/elhisse-CLPrepas/mon-dossier-challenge-module04.git` ; aucun push pendant cette préparation.

## Adaptations

- Accueil S15 ajouté ; `index.html` ouvre cet accueil. Les anciennes adresses avec ancre conservent l'accès à la présentation héritée du module.
- Fiche S15 remplacée par le modèle complet du pack S15 : prédictions vierges, deux variantes, interprétation, contre-exemple, six champs justifiés.
- Ajout du tableau de suivi, des objectifs, du relevé d'observations et de la préparation S16.
- Atelier autonome et 24 ressources copiés du pack S15 local.
- Notebook candidat S16 et mode d'emploi original copiés de `atelier-seance-16-ln-ia/public/ressources/`.
- Plan corrigé : le dossier est versionné, contrairement à l'ancienne mention « exclu du suivi Git ».
- Fiches source, traces S13/S14, présentation et PDF du module, portfolio et ressources historiques conservés.

La fiche S15 reprise de S14 était un modèle sans observations personnelles. Aucun résultat candidat ni décision humaine n'a été inventé. Le JSON S16 doit provenir du véritable export du carnet ; il n'est pas fabriqué lors de cette préparation.

## Portée

Contrôles exécutés avec succès le 9 novembre : 19 liens locaux de l'accueil et de l'index ; contenu de six fichiers historiques conservé (comparaison des textes indépendante des fins de ligne Git) ; 24 ressources et HTML autonome identiques aux originaux ; notebook identique à celui de S16 et syntaxe de ses six cellules Python valide. `npm.cmd run check` réussit dans le pack parent. `git diff --check` ne signale aucune erreur d'espacement. Les nouveaux fichiers et modifications restent non commités pour revue ; l'historique antérieur est conservé.

Le contrôle des copies peut être rejoué depuis le dossier atelier S15 avec `py -3 -X utf8 scripts/controler-suivi-s15.py`.

Les contrôles de préparation portent sur les fichiers, les liens de l'accueil, l'identité des copies, la syntaxe des cellules du notebook et les contrôles automatisés du pack S15. Ils ne constituent pas une répétition dans le navigateur ou Jupyter. Les cases de répétition et les validations du portfolio restent en attente.

Le rapport de mi-parcours du dossier parent indiquait que le support S16 n'était pas identifié dans S15. La présente exploration l'a retrouvé dans le dossier voisin S16 et en a intégré le carnet candidat.
