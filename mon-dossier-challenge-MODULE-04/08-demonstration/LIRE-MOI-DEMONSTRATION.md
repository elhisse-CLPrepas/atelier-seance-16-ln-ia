# Démonstration · un exemple séparé de mon projet

## Observer sans exécuter

Lire dans `guide/ressources/` :

1. `sorties-demonstration.md` : déroulé et résultats préparés.
2. `variantes-exemple-rouvert.md` : texte corrigé et rouvert.
3. `mandat-et-releve-agent.md` : mandat de lecture et exemple de réponse.

Les textes sources se trouvent dans `guide/sources/`. Le cas Samira se trouve dans `samira/`, avec sa fiche et ses instructions.

## Rejouer avec Python standard

Ouvrir un terminal **dans `08-demonstration/guide/ressources`**, puis lancer :

```powershell
py -3 -X utf8 demonstration-s16.py
```

Si Python est accessible sous `python`, utiliser `python -X utf8 demonstration-s16.py`.
Sous Windows, vous pouvez aussi double-cliquer sur `LANCER-DEMONSTRATION.cmd` dans `08-demonstration`. Ce lanceur se place dans le bon dossier et active UTF-8 pour les accents et symboles.
Les résultats sont créés sous `dossier-demo-s16/04-communication/` dans ce répertoire. Les productions personnelles de la racine ne sont pas utilisées par ce scénario fictif par défaut.

## Montrer le notebook

Ouvrir `guide/ressources/communication-assistee-demonstration.ipynb` dans Jupyter ou VS Code. Lire d'abord ses paramètres et vérifier la racine de sortie avant une nouvelle exécution.

## Faire expliquer

- Quel champ change et quels formats en dépendent ?
- Quel passage est corrigé et pour quel public ?
- Où retrouve-t-on la correction après réouverture ?

Pour le cas du guide fourni : longueurs avant changement 114, 166 et 174 ; après changement 114, 166 et 184 ; message corrigé final 177 caractères. Ces nombres concernent cet exemple précis.
