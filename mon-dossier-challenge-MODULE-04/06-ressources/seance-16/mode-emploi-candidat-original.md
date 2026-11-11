# Ouvrir le kit candidat S16

1. Extrayez tout le kit dans votre dossier personnel. Gardez les trois dossiers 04-communication, 05-automatisation et 07-portfolio côte à côte.
2. Ouvrez 05-automatisation/communication-assistee.ipynb dans Jupyter ou VS Code. Choisissez le noyau Python 3 puis redémarrez-le. Le cahier utilise uniquement la bibliothèque standard Python.
3. Si vous arrivez avec votre projet, placez votre donnees-pour-s16.json de S15 et votre message-court-projet.md de S14 dans 04-communication. Dans la cellule 1, choisissez MODE_SOURCE = "fichier". Si votre version humaine ne se trouve pas dans une rubrique « Version humaine S14 », saisissez-la dans TEXTE_HUMAIN_S14.
4. Pour le cas de remplacement, gardez MODE_SOURCE = "exemple". La fiche fictive et la version humaine sont intégrées. Vous remplissez vous-même les zones de prédiction et de correction.
5. Exécutez dans l’ordre. Avant la cellule 4, choisissez un champ, sa nouvelle valeur, son appui et une prédiction. En cellule 5, choisissez l’un des trois formats, puis entrez le passage brut exact, sa correction, votre motif, la source et le canal. Utilisez des guillemets simples Python si votre texte contient des guillemets doubles.
6. Exécutez la cellule 6. Si elle indique un export en attente, reprenez les zones incomplètes. Quand le chemin du Markdown apparaît, ouvrez-le dans un éditeur et retrouvez votre phrase dans « Message corrigé ». Enregistrez le notebook avec ses sorties par Ctrl+S.

En cellule 1, le chemin affiché indique le dossier racine d’écriture. Si votre environnement démarre ailleurs, saisissez dans RACINE_CANDIDAT le chemin de votre dossier de travail (sous Windows, utilisez par exemple une chaîne brute Python r"C:\Atelier\MonDossier"). Tous les chemins de preuves partent de cette racine.

## Les deux fichiers à présenter

- 05-automatisation/communication-assistee.ipynb
- 04-communication/variantes-communication-projet.md

Ajoutez votre entrée S16 à 07-portfolio/preuves-module-04.md sans remplacer les entrées antérieures. Dans un nouveau kit, le fichier 07-portfolio/preuves-module-04.md sert de modèle vierge. Si vous avez déjà un portfolio, ajoutez-y seulement votre nouvelle entrée. La décision du pilote se consigne après observation.

Un second export identique garde la même version. Une correction différente conserve auparavant l’ancienne version dans 04-communication/historique/. En cas de fermeture brutale pendant l’écriture, vérifiez qu’aucun notebook ni script ne travaille encore avant de retirer l’éventuel verrou .export-s16.lock. Le Markdown initial est préservé tant que le remplacement complet n’est pas achevé.

### Autre cas fictif · Samira

Le dossier sources-fictives/samira/ contient un JSON S15 complet, la rédaction humaine S14 et la fiche de son mini-guide de révisions. Les instructions de ce dossier indiquent les deux fichiers à copier dans un nouveau kit.
