# Instructions participant · Séance 16

**Du notebook au message corrigé** · Lundi 16 novembre 2026 · Module 04 · Produire · 90 minutes, avec 30 minutes facultatives.

Pilotage pédagogique : Prof. Abderrahman El Hisse · LAB-NUMÉRIQUE-IA.

## Mon objectif

Reprendre mes données S15 et ma rédaction S14, produire trois brouillons avec Python, prévoir l'effet d'un changement, corriger un passage et retrouver ma correction dans le fichier enregistré. Je dois pouvoir expliquer ce que le programme fait et ce que j'ai décidé moi-même.

## 1. Préparer mon dossier · 0–10 minutes

Le dossier actif est `atelier-seance-16-ln-ia/mon-dossier-challenge-MODULE-04/`. Tous les chemins ci-dessous partent de cette racine.

1. Ouvrir [l'accueil du Module 04](../ACCUEIL-MODULE-04.html), puis [l'atelier S16](../OUVRIR-SEANCE-16.html).
2. Retrouver mes sources, leur version et leur statut, ma trace S13 et ma rédaction `04-communication/message-court-projet.md`.
3. Retrouver mon véritable export S15 : `04-communication/donnees-pour-s16.json`. Vérifier les six champs **projet, public, besoin, proposition, action, format**, chacun avec sa source ou sa justification.
4. Conserver les productions antérieures. Si une pièce manque, reprendre S14/S15 ou choisir explicitement un cas fictif pour s'exercer. Ne pas présenter ce cas comme mon projet personnel.

Le Markdown final `04-communication/variantes-communication-projet.md` sera produit par le notebook. Ne pas le remplacer par une sortie de démonstration.

## 2. Observer la démonstration · 10–25 minutes

Suivre la rubrique Démonstration de l'atelier ou [le guide de démonstration](../08-demonstration/LIRE-MOI-DEMONSTRATION.md).

- Annoncer quel format devrait changer avant de lire le résultat.
- Distinguer l'affichage d'un brouillon, l'enregistrement sur disque et la réouverture du fichier.
- Dans le cas fictif fourni, seul le professionnel dépend du public. Ce constat concerne les gabarits du notebook ; une prédiction pour mon essai reste à formuler.

Le script de démonstration et son notebook avec sorties sont des exemples du formateur. La répétition Web s'exécute en JavaScript ; elle ne constitue pas mon exécution Python.

## 3. Exécuter les cellules 1 à 3 · 25–55 minutes

Ouvrir [le notebook candidat](../05-automatisation/communication-assistee.ipynb) dans Jupyter ou VS Code avec un noyau Python 3. Redémarrer le noyau avant une reprise complète, puis exécuter les cellules dans l'ordre. Le notebook utilise la bibliothèque standard Python.

Dans la cellule 1 :

- Pour mon projet, choisir `MODE_SOURCE = "fichier"`.
- Vérifier la racine d'écriture affichée. Si nécessaire, renseigner `RACINE_CANDIDAT` avec le chemin absolu de ce dossier Module 04, sous forme de chaîne brute Python `r"D:\...\mon-dossier-challenge-MODULE-04"` ; remplacer les points de suspension par le véritable chemin.
- Vérifier la lecture du JSON S15 et de la rubrique « Version humaine S14 » de mon message. Si nécessaire, renseigner `TEXTE_HUMAIN_S14` avec ma propre rédaction.
- Pour l'entraînement fictif, choisir `MODE_SOURCE = "exemple"` et noter cette origine dans la preuve.

Après les cellules 2 et 3, lire les formats **court, accessible et professionnel**. Retrouver le fait commun et l'action. Comparer avec mes mots de S14 : une sortie de gabarit reste un **BROUILLON — À RELIRE**.

## 4. Prédire puis changer une valeur · 55–70 minutes

Avant d'exécuter la cellule 4, renseigner moi-même :

| Paramètre | Ce que je saisis |
|---|---|
| `CHAMP` | Le champ à faire varier parmi ceux admis par le notebook |
| `NOUVELLE` | Une nouvelle valeur réellement différente |
| `ORIGINE` | Sa source ou la justification du choix |
| `PREDICTION` | Les formats qui devraient changer et mon raisonnement |

Exécuter la cellule 4, puis comparer **les textes complets avant/après**, les longueurs et l'action. Noter les formats effectivement modifiés, l'outil utilisé et l'écart éventuel avec ma prédiction. Si je change une entrée antérieure, relancer les cellules qui en dépendent.

Une longueur acceptable ne prouve ni la vérité du message, ni son adaptation au public. Le seuil de 400 caractères est un repère pédagogique du notebook.

## 5. Corriger, exporter et rouvrir · 70–85 minutes

Dans la cellule 5, choisir le brouillon et renseigner :

| Paramètre | Ce que je saisis |
|---|---|
| `CHOIX` | `court`, `accessible` ou `professionnel` |
| `AVANT` | Un passage exact du brouillon après changement |
| `APRES` | Ma reformulation, différente du passage brut |
| `MOTIF` | La raison concrète de ma correction |
| `APPUI` | La source et le repère qui justifient le sens conservé |
| `CANAL` | Le canal de communication envisagé |

Exécuter les cellules 5 et 6. Si l'export reste en attente, lire le message et compléter ce qui manque. Ne pas contourner les contrôles.

1. Ouvrir réellement `04-communication/variantes-communication-projet.md` dans un éditeur.
2. Retrouver mes mots sous **« Message corrigé »**, puis expliquer le passage brut, ma correction et son appui.
3. Enregistrer `05-automatisation/communication-assistee.ipynb` avec ses sorties, par exemple avec `Ctrl+S`.

Un nouvel export identique conserve le fichier existant ; une modification conserve la version précédente dans `04-communication/historique/`. Garder les sources et les preuves antérieures.

## 6. Présenter la preuve et préparer M05 · 85–90 minutes

Présenter les deux fichiers :

- `05-automatisation/communication-assistee.ipynb`, avec les sorties de mon exécution.
- `04-communication/variantes-communication-projet.md`, rouvert avec ma correction.

Renseigner [l'entrée S16](../07-portfolio/entree-preuve-16.md), puis ajouter cette contribution à `07-portfolio/preuves-module-04.md` sans remplacer S13/S14/S15.

Identifiant : **`preuve-16-notebook-communication-assistee`**. Inscrire la date réelle, l'origine des données, le champ changé, la prédiction, les résultats, la correction, les chemins et le constat effectivement observé. Une observation manquante reste « À COMPLÉTER ». La décision du pilote reste en attente jusqu'à sa décision explicite, datée et délimitée.

Préparer [le relais M05](../07-portfolio/relais-module-05.md) : titre, court paragraphe relu, action unique, chemin et rubrique source, version ou empreinte disponible, statut. La validation d'une preuve ne vaut pas autorisation de diffusion.

## Réviser ou prolonger

Utiliser les **8 flashcards** et les **6 questions** du quiz S16 pour expliquer les notions encore fragiles. Le score ne remplace pas la preuve pratique. Si 30 minutes restent, suivre le prolongement du guide d'été dans les ressources de l'atelier.

En cas de panne Python, lire le relevé hors ligne et noter « exécution individuelle à démontrer ». Programmer la reprise avec le pilote ; ne pas déclarer l'exécution accomplie.

Pour une aide pas à pas, copier [le prompt maître S16](02-PROMPT-MAÎTRE-S16.md) dans l'assistant avec les seules pièces nécessaires et accessibles. Garder les données personnelles sur son poste ; utiliser un cas fictif pour une démonstration partagée. Aucun envoi ni publication n'est demandé.
