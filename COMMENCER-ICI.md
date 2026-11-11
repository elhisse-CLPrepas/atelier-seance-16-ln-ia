# Animer le lundi 16 novembre 2026

## Continuité du dossier commun du Module 04

Poursuivre dans le dossier existant `../atelier-seance-15-ln-ia/mon-dossier-challenge-module04`.
Le guide [Poursuivre S16](public/ressources/atelier/poursuivre-s16.md) indique les fichiers à reprendre et les preuves à ajouter.
Le script `scripts/completer-dossier-commun.ps1` ajoute les supports S16 et conserve chaque fichier déjà présent, notamment le notebook et le portfolio.
Les cinq affiches sont intégrées à l'accueil, à la rubrique Présentation et aux Ressources ; l'affiche S16 accompagne la première diapositive Web. Le PowerPoint et son PDF d'origine restent les supports de l'édition initiale.

Du notebook au message corrigé · Challenge 100 Jours Automne 2026 · Module 04, S16  
Prof. Abderrahman El Hisse · LAB-NUMÉRIQUE-IA · Édition pédagogique 1.0 à relire par le pilote.

## Ouvrir la séance

1. Extrayez le ZIP. Ouvrez le dossier atelier-seance-16-ln-ia puis le fichier OUVRIR-SEANCE-16.html par double-clic. Vous pouvez aussi copier ce HTML seul sur une clé USB. Il contient les onze rubriques et les ressources.
2. Cliquez sur « Projeter la séance ». Les flèches passent d’une diapositive à l’autre. Échap quitte la projection. Pour la démonstration, passez du diaporama au notebook puis à l’éditeur de texte.
3. Distribuez kit-candidat-s16.zip depuis la rubrique Ressources, ou copiez le dossier kit-candidat. Remettez également la fiche candidat en PDF remplissable ou en Word. Le cas fictif du guide S12 est intégré au notebook. Un deuxième cas complet, celui de Samira, se trouve dans le kit.
4. Le candidat ouvre 04-communication/variantes-communication-projet.md, puis enregistre 05-automatisation/communication-assistee.ipynb avec ses sorties. Ajoutez l’observation à 07-portfolio/preuves-module-04.md en conservant les entrées antérieures.

| Besoin | Fichier dans public/ressources |
|---|---|
| Animer 90 minutes, puis 30 minutes facultatives | documents/conducteur-formateur-s16.pdf et atelier/prolongement-guide-ete.md |
| Projeter et éditer | projection/seance-16-du-notebook-au-message-corrige.pdf et son PowerPoint avec notes |
| Distribuer | atelier/kit-candidat-s16.zip et documents/fiche-candidat-s16.pdf |
| Montrer le résultat | demo/communication-assistee-demonstration.ipynb, demo/variantes-exemple-rouvert.md et demo/sorties-demonstration.md |
| Corriger et clôturer | documents/corrige-demonstration-s16.pdf, documents/bilan-module-04.pdf et leurs Word |
| Confier une lecture à l’agent | demo/mandat-et-releve-agent.md et atelier/prompts-agents-module-04.md |
| Préparer la future page | atelier/relais-module-05.md |

## Rejouer le cas avant la séance

Dans Jupyter ou VS Code, choisissez un noyau Python 3, redémarrez-le et exécutez les six cellules du notebook du formateur dans une copie de travail. La cellule 6 doit retrouver « Le journal explique ce qui a changé et pourquoi. » sous « Message corrigé ». Un poste équipé de nbformat et nbclient peut aussi exécuter le script verifier-noyau-s16.py situé à côté du notebook de démonstration. Il crée un répertoire d’essai distinct et lance un nouveau noyau.

Depuis le dossier demo, la commande suivante rejoue le scénario avec Python standard. Sous Windows, la commande py -3 peut remplacer python. Le résultat se range dans dossier-demo-s16.

~~~bash
python demonstration-s16.py
~~~

Le relevé et le Markdown d’exemple permettent de poursuivre l’explication si un poste ne démarre pas. Inscrivez alors « exécution individuelle à démontrer » avant de reprendre avec le candidat.

## Travailler sur le projet personnel

Le mode « fichier » lit donnees-pour-s16.json exporté par le portfolio S15 et la rédaction humaine de message-court-projet.md. La racine d’écriture s’affiche dès la première cellule. Le carnet Web propose une répétition JavaScript et des modèles de bilan. Le notebook et la réouverture sur disque permettent d’établir la preuve S16.

## Modifier le projet Vite

Les sources sont dans src/ et les pièces téléchargeables dans public/ressources/. Bootstrap 5.3.8 et sa licence sont inclus. Le double-clic sur le HTML autonome ne demande aucune installation. Pour modifier les contenus, utilisez Node 24 ou une version compatible indiquée dans package.json. Depuis la racine du projet :

~~~bash
npm ci
npm run dev
~~~

Pour reconstruire le dossier dist/ et le HTML autonome puis les contrôler :

~~~bash
npm run build
npm run check
~~~

La commande npm run preview sert le dossier compilé en local. Pour une future publication, définissez ATELIER_PUBLIC_URL avec l’adresse publique réelle avant de compiler. Le script ajoute alors l’URL canonique et des liens absolus de partage. L’édition comprend les métadonnées de description, Open Graph, Twitter et LearningResource.

[Analyse des cinq archives](docs/SOURCES-ET-ADAPTATIONS.md) · [Contrôle de la livraison](docs/CONTROLE-S16.md)
