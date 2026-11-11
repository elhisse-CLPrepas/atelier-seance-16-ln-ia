# Atelier LN-IA · Séance 16

## Du notebook au message corrigé

**Cahier des charges pédagogique et opérationnel** · Challenge 100 Jours, automne 2026 · Module 04, communication assistée · Lundi 16 novembre 2026.

Pilotage : **Prof. Abderrahman El Hisse · LAB-NUMÉRIQUE-IA**. Durée : **90 minutes**, avec un prolongement facultatif de **30 minutes**. Posture de la séance : **Produire**.

**Site GitHub Pages :** https://elhisse-CLPrepas.github.io/atelier-seance-16-ln-ia/ · [Configuration et publication](docs/PUBLICATION-GITHUB-PAGES.md).

Après un clone Git, lancer `npm ci` puis `npm run build` pour générer les HTML autonomes et `dist/`. Les sources sont versionnées ; les fichiers compilés sont construits par GitHub Actions avant publication.

La séance 16 transforme les acquis S13, S14 et S15 en une production locale vérifiable : le participant exécute un notebook Python, compare trois brouillons, décide d'une correction humaine, exporte son message et retrouve cette correction dans le fichier rouvert. Elle clôt le parcours du Module 04 et prépare une matière relue pour le Module 05.

## 1. Accéder à la séance et choisir son dossier

| Besoin | Entrée à ouvrir |
|---|---|
| Animer ou projeter l'atelier hors connexion | [OUVRIR-SEANCE-16.html](OUVRIR-SEANCE-16.html) |
| Poursuivre son travail dans le dossier commun actuel | [Accueil du Module 04](mon-dossier-challenge-MODULE-04/ACCUEIL-MODULE-04.html) |
| Suivre les consignes du participant | [Instructions participant S16](02-PROMPT/01-INSTRUCTIONS-PARTICIPANT-S16.md) |
| Se faire accompagner étape par étape | [Prompt maître S16](02-PROMPT/02-PROMPT-MAÎTRE-S16.md) |
| Préparer l'animation | [COMMENCER-ICI.md](COMMENCER-ICI.md) |
| Comprendre les étapes S13 à S16 | [Parcours du Module 04](mon-dossier-challenge-MODULE-04/00-pilotage/PARCOURS-MODULE-04.md) |

Le **dossier de progression actuel** est `mon-dossier-challenge-MODULE-04/`, dans cet atelier S16. Il reprend le dossier commun de S15 ; celui-ci reste conservé comme point de reprise. Enregistrer les nouvelles productions dans le dossier actuel pour éviter des versions concurrentes. Les anciennes consignes conservées peuvent encore mentionner le chemin S15 : pour la poursuite S16, utiliser les entrées ci-dessus.

Le HTML autonome s'ouvre par double-clic. Le notebook demande Jupyter ou VS Code avec un noyau Python 3. Les fichiers Markdown s'ouvrent dans un éditeur de texte ; le navigateur peut proposer de les télécharger.

## 2. Finalité et résultats attendus

À l'issue de la séance, le participant doit pouvoir :

1. Relier les données utilisées à leurs sources ou à des choix éditoriaux explicités.
2. Distinguer sa rédaction humaine, un brouillon de gabarit et une correction décidée.
3. Prédire l'effet d'un changement de donnée avant de l'exécuter.
4. Comparer les sorties et expliquer ce que les contrôles automatiques établissent.
5. Corriger un passage, justifier son choix et retrouver le résultat sur disque.
6. Présenter deux fichiers exploitables, documenter la preuve S16 et préparer le relais M05.

La production attendue est un message fidèle à sa source, adapté à un public et à un canal, accompagné d'une trace permettant de comprendre sa fabrication.

## 3. Continuité du Module 04

| Séance | Posture | Acquis mobilisé en S16 |
|---|---|---|
| S13 · Du guide au message | Comprendre | Un fait sourcé, un public et une action |
| S14 · Un message, trois variantes | Manipuler | Une version humaine et des formulations comparées |
| S15 · Vérifier une règle | Approfondir | Une prédiction, des essais, une limite et six champs justifiés |
| S16 · Du notebook au message corrigé | Produire | Une exécution, une correction humaine et un fichier rouvert |

### Entrées nécessaires

Les chemins suivants sont relatifs à `mon-dossier-challenge-MODULE-04/` :

- Les sources du projet, avec leur version et leur statut connus.
- `04-communication/message-court-projet.md`, notamment la rubrique « Version humaine S14 ».
- `04-communication/donnees-pour-s16.json`, véritable export S15 comportant **projet, public, besoin, proposition, action, format**, avec leurs appuis.
- `05-automatisation/communication-assistee.ipynb`, carnet de travail du participant.
- Le portfolio existant `07-portfolio/preuves-module-04.md`.

Une entrée absente reste à compléter. Le mode `exemple` du notebook et les cas fictifs permettent de s'entraîner en identifiant cette origine. Ils ne remplacent pas une preuve personnelle manquante.

## 4. Méthode LN-IA appliquée à la production

Dans cet atelier, la méthode LN-IA se concrétise par une chaîne de travail observable :

**Situer le besoin → retrouver les sources → formuler → prédire → exécuter et comparer → corriger humainement → enregistrer et rouvrir → documenter la preuve → préparer la réutilisation.**

| Dimension | Exigence concrète |
|---|---|
| Intention | Nommer le projet, le public, le besoin, l'action et le canal |
| Ancrage documentaire | Relier les faits à des pièces accessibles et laisser visibles les incertitudes |
| Assistance | Utiliser l'assistant pour repérer, comparer ou relire, avec une mission délimitée |
| Automatisation | Exécuter des opérations explicites et reproductibles sur les données de travail |
| Décision humaine | Choisir la formulation, expliquer la correction et examiner le sens complet |
| Traçabilité | Conserver les sources, les versions, les résultats et les observations réelles |
| Supervision | Faire statuer le pilote sur les éléments effectivement présentés |

Python applique les gabarits et les contrôles écrits dans le notebook. Jupyter organise les cellules et affiche les sorties. L'assistant peut accompagner la lecture et le raisonnement. Le participant reste auteur de ses choix et le pilote conserve la décision pédagogique. Le notebook fourni ne nécessite pas d'appel à un service d'IA pour produire ses brouillons.

## 5. Périmètre et exigences de réalisation

| Référence | Exigence | Élément à vérifier |
|---|---|---|
| EX-01 | Identifier le projet personnel ou le cas fictif | Origine explicitée dans la trace |
| EX-02 | Vérifier les six champs et leurs appuis | Données lisibles et références accessibles |
| EX-03 | Produire les formats court, accessible et professionnel | Trois textes complets comparables |
| EX-04 | Recueillir la prédiction avant le test d'une seule valeur | Prédiction distinguée du résultat |
| EX-05 | Examiner les effets réels du changement | Avant/après, formats modifiés, longueurs et action |
| EX-06 | Décider d'une correction motivée et sourcée | AVANT / APRÈS / POURQUOI / APPUI et canal |
| EX-07 | Exporter et rouvrir le Markdown, enregistrer le carnet | Correction retrouvée et sorties conservées |
| EX-08 | Ajouter la preuve S16 sans effacer les précédentes | Entrée datée et observation attribuée |
| EX-09 | Préparer le relais M05 avec son statut | Extrait relu, source, action et décision de diffusion si accordée |

Le périmètre comprend la production et la préparation locale. Une publication ou un envoi exige une décision distincte. Les contrôles de longueur ne suffisent pas à établir la vérité, l'adaptation au public ou la qualité éditoriale.

## 6. Déroulement de référence · 90 minutes

| Temps | Activité | Résultat observable |
|---|---|---|
| 0–10 min | Retrouver S13/S14/S15 et choisir le mode de travail | Fait, action, sources et origine des données situés |
| 10–25 min | Observer les six cellules et la démonstration | Différence comprise entre affichage et fichier |
| 25–55 min | Renseigner les paramètres et exécuter les cellules 1 à 3 | Version humaine et trois brouillons lisibles |
| 55–70 min | Prédire, changer une donnée et exécuter la cellule 4 | Comparaison avant/après expliquée |
| 70–85 min | Corriger, exécuter les cellules 5 et 6, exporter et rouvrir | Correction retrouvée sur disque, notebook enregistré |
| 85–90 min | Présenter les fichiers, consigner l'observation et préparer M05 | Preuve S16 et relais amorcés |

Le prolongement facultatif de 30 minutes s'appuie sur [le guide d'été](public/ressources/atelier/prolongement-guide-ete.md). Les **8 flashcards** et les **6 questions du quiz S16** soutiennent la révision ; leur résultat ne remplace pas la preuve pratique.

## 7. Livrables et critères de réception

Tous les chemins du tableau partent du dossier commun actuel.

| Livrable | Critère de réception |
|---|---|
| `05-automatisation/communication-assistee.ipynb` | Paramètres renseignés, cellules exécutées dans l'ordre et sorties enregistrées |
| `04-communication/variantes-communication-projet.md` | Export réel ; correction retrouvée sous « Message corrigé » après réouverture |
| `07-portfolio/entree-preuve-16.md` | Origine, changement, prédiction, résultat, correction, appui et observation renseignés selon les faits |
| `07-portfolio/preuves-module-04.md` | Entrée S16 ajoutée ; contributions S13/S14/S15 conservées |
| `07-portfolio/relais-module-05.md` | Titre, paragraphe relu, action, chemin source, version ou empreinte disponible et statut |

Identifiant de preuve : **`preuve-16-notebook-communication-assistee`**.

Le participant présente les deux fichiers principaux et explique sa correction. Le pilote consigne le constat réel, la date, le périmètre de sa décision et les reprises éventuelles. Une absence d'observation reste visible : « À COMPLÉTER » ou « exécution individuelle à démontrer », selon la situation. La validation visuelle du support d'atelier ne vaut pas validation automatique des productions individuelles.

## 8. Organisation des dossiers

```text
atelier-seance-16-ln-ia/
├── README.md                         Cahier des charges de la séance
├── COMMENCER-ICI.md                   Guide d'animation et préparation
├── OUVRIR-SEANCE-16.html              Atelier autonome avec ressources
├── Affiches-module04/                Images originales du parcours
├── 02-PROMPT/                        Instructions et prompts S13 à S16
├── mon-dossier-challenge-MODULE-04/   Dossier actuel de progression
│   ├── ACCUEIL-MODULE-04.html         Entrée pratique du participant
│   ├── 00-pilotage/                   Parcours, suivi et contrôles
│   ├── 03-sources/                    Sources du projet
│   ├── 04-communication/              Messages, données et exports
│   ├── 05-automatisation/             Notebook et guides d'exécution
│   ├── 06-ressources/                 Affiches, fiches et supports
│   ├── 07-portfolio/                  Preuves et relais M05
│   └── 08-demonstration/              Cas fictifs séparés du travail personnel
├── kit-candidat/                     Kit de démarrage distinct de la progression
├── public/ressources/                Ressources de l'atelier Web
├── src/                              Sources de l'application
├── scripts/                          Préparation, compilation et vérification
├── dist/                             Version Web compilée
└── docs/                             Contrôles et provenance pédagogique
```

Le kit de démarrage est destiné à une nouvelle installation. Dans un dossier déjà utilisé, ajouter les éléments nécessaires en conservant les productions et les preuves existantes.

## 9. Démonstration et exploitation locale

Pour montrer le résultat sans Python, ouvrir le [guide de démonstration](mon-dossier-challenge-MODULE-04/08-demonstration/LIRE-MOI-DEMONSTRATION.md), le relevé des sorties et le Markdown préparé.

Sous Windows, le lanceur [LANCER-DEMONSTRATION.cmd](mon-dossier-challenge-MODULE-04/08-demonstration/LANCER-DEMONSTRATION.cmd) se place dans le répertoire de démonstration et active UTF-8. Python 3 et le lanceur `py` doivent être disponibles.

Pour exécuter manuellement, ouvrir un terminal dans `mon-dossier-challenge-MODULE-04/08-demonstration/guide/ressources/`, puis lancer :

```powershell
py -3 -X utf8 demonstration-s16.py
```

Les résultats fictifs sont écrits dans `dossier-demo-s16/04-communication/`, sous ce répertoire. Pour le cas fourni, le message corrigé compte **177 caractères**. Cette mesure est un repère de démonstration, pas une longueur imposée aux projets personnels.

Pour le travail du participant, suivre les consignes S16 : vérifier `MODE_SOURCE`, la racine d'écriture et les entrées avant exécution. Un environnement Python indisponible permet de poursuivre l'explication avec les supports hors ligne ; l'exécution individuelle reste alors à observer ultérieurement.

## 10. Ouverture vers une production avec la méthode LN-IA

La sortie de S16 constitue une matière de production réutilisable : un message relu, un public identifié, une action et des sources retrouvables. Elle peut alimenter une page du Module 05, un courriel ou un autre support adapté au projet.

La poursuite suit quatre décisions :

1. **Choisir la matière** : prélever un passage effectivement relu dans le Markdown final et conserver son repère source.
2. **Adapter au support** : définir le lecteur, le canal, le titre, l'action et les contraintes de présentation. Toute nouvelle promesse demande un appui.
3. **Recontrôler la production** : vérifier les faits, le sens, la lisibilité et le statut après adaptation ; consigner la correction et la version retenue.
4. **Décider de l'usage** : distinguer exercice local, preuve pédagogique et diffusion autorisée, avec la date et le périmètre de la décision.

Le point de passage vers M05 est [la fiche relais](mon-dossier-challenge-MODULE-04/07-portfolio/relais-module-05.md). Elle conserve le lien entre la source, la correction humaine et la future production. L'assistance et l'automatisation restent explicables tout au long de cette transformation.

## 11. Maintenir et vérifier l'atelier

Le HTML autonome ne nécessite aucune installation Node. Pour modifier l'application, utiliser une version Node compatible avec [package.json](package.json) et installer les dépendances du projet.

```powershell
npm.cmd ci
npm.cmd run dev
```

Pour reconstruire et contrôler :

```powershell
npm.cmd run build
npm.cmd run check
node scripts/verifier-dossier-module04.mjs
```

La compilation régénère `index.html`, `dist/` et le HTML autonome à la racine. Elle ne synchronise pas automatiquement la copie du HTML déjà présente dans le dossier commun. Les scripts de reprise conservent les fichiers existants ; comparer les versions avant une mise à jour explicite.

## 12. État des contrôles et documents de référence

Le pilote a déclaré validés le contrôle visuel et pédagogique de S15 ainsi que le déploiement local S16. Les vérifications techniques consignées couvrent les 11 rubriques, les 18 diapositives Web, les 38 ressources autonomes, les liens de l'accueil commun et l'exécution du script de démonstration. Elles ne certifient pas l'exécution du notebook candidat dans Jupyter.

Les affiches sont intégrées à la présentation Web et à sa version autonome. Le PowerPoint et le PDF de projection de l'édition initiale sont conservés sans cette modification.

- [Contrôle local du 11 novembre 2026](docs/CONTROLE-LOCAL-2026-11-11.md).
- [Contrôle de préparation du dossier commun](mon-dossier-challenge-MODULE-04/00-pilotage/CONTROLE-PREPARATION-S16.md).
- [Provenance des supports et adaptations](docs/SOURCES-ET-ADAPTATIONS.md).
- [Contrôle initial de livraison](docs/CONTROLE-S16.md), à lire avec les contrôles locaux plus récents.

La réception pédagogique finale porte sur les productions montrées par chaque participant et la décision explicite du pilote.
