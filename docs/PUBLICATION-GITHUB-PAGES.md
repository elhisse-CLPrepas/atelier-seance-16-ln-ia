# Publication GitHub Pages · Atelier S16

## Dépôt et adresse

- Dépôt : https://github.com/elhisse-CLPrepas/atelier-seance-16-ln-ia
- Adresse de publication prévue : https://elhisse-CLPrepas.github.io/atelier-seance-16-ln-ia/
- Branche de travail et publication : `main`.
- Source Pages dans les paramètres GitHub : **GitHub Actions**.

## Cycle de publication

Chaque push sur `main`, ou lancement manuel du workflow Pages, installe les dépendances verrouillées avec Node 24, reconstruit l'atelier, exécute les contrôles puis publie uniquement `dist/`.

Le workflow `.github/workflows/pages.yml` utilise les actions officielles de GitHub pour configurer Pages, charger l'artefact et le déployer. La génération définit `ATELIER_PUBLIC_URL` avec l'adresse Pages pour les métadonnées canoniques et de partage. Le chemin relatif Vite `./` permet de servir le site sous le nom du dépôt.

Les droits de publication `pages: write` et `id-token: write` sont limités au job de déploiement. Aucun secret supplémentaire n'est enregistré dans le dépôt.

## Fichiers suivis et fichiers générés

Git suit les sources, les affiches, les ressources pédagogiques, le dossier commun et les scripts. `node_modules/`, `dist/`, l'index racine généré et les HTML autonomes S16 sont exclus : ils sont reconstruits à partir des sources. La compilation actualise également la copie S16 du dossier commun.

Le volumineux HTML autonome S15 hérité reste conservé localement et exclu du nouveau dépôt. Il appartient à la séance précédente ; les autres fichiers de progression S15 sont conservés. Les environnements Python, fichiers temporaires, verrous et fichiers `.env` ne sont pas versionnés.

La publication de `dist/` expose l'atelier Web et ses ressources. Le dossier commun est disponible dans les sources du dépôt ; il n'est pas automatiquement copié dans le site public. Le kit candidat reste téléchargeable dans la rubrique Ressources.

## Vérifier avant un push

```powershell
$env:ATELIER_PUBLIC_URL = 'https://elhisse-CLPrepas.github.io/atelier-seance-16-ln-ia/'
npm.cmd run build
npm.cmd run check
node scripts/verifier-dossier-module04.mjs
git diff --check
git status --short
```

Après un clone, lancer la compilation pour disposer des HTML autonomes. Les anciens liens locaux vers l'archive HTML S15 nécessitent de reprendre le fichier dans le pack S15 local.

## Vérifier après publication

Dans GitHub, consulter **Actions**, puis le workflow de publication Pages du commit concerné. Vérifier la réussite des jobs de construction et de déploiement ainsi que l'adresse retournée par l'environnement `github-pages`.

Ouvrir l'adresse du site et contrôler l'accueil, les affiches et un téléchargement. Une réussite technique de publication ne remplace pas la validation des productions individuelles.

Documentation de référence : https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
