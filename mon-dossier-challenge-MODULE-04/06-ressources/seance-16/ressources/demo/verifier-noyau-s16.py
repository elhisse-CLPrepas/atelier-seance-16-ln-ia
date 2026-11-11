"""Rejouer la démonstration S16 dans un nouveau noyau Jupyter local."""
from pathlib import Path
import hashlib
import tempfile

def main():
    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError:
        raise SystemExit("Ce test automatique utilise nbformat et nbclient. Vous pouvez aussi ouvrir le notebook dans Jupyter, redémarrer son noyau, puis exécuter toutes les cellules.") from None
    source = Path(__file__).resolve().with_name("communication-assistee-demonstration.ipynb")
    if not source.is_file():
        raise SystemExit("Placez communication-assistee-demonstration.ipynb à côté de ce script.")
    nb=nbformat.read(source,as_version=4)
    nbformat.validate(nb)
    cellules=[c for c in nb.cells if c.cell_type=="code"]
    if len(cellules)!=6:
        raise ValueError("La démonstration attend six cellules de travail.")
    for cellule in cellules:
        cellule.outputs=[]
        cellule.execution_count=None
    racine=Path(tempfile.mkdtemp(prefix="controle-jupyter-s16-",dir=Path.cwd()))
    travail=racine/"05-automatisation"
    travail.mkdir()
    NotebookClient(nb,timeout=120,kernel_name="python3",allow_errors=False).execute(cwd=str(travail))
    nbformat.write(nb,travail/"communication-assistee.ipynb")
    if [c.execution_count for c in cellules]!=list(range(1,7)):
        raise RuntimeError("Les six sorties du nouveau noyau doivent être contrôlées.")
    sortie=racine/"04-communication"/"variantes-communication-projet.md"
    donnees=sortie.read_bytes()
    relu=donnees.decode("utf-8").rsplit("\n## Message corrigé\n\n",1)[1].split("\n\n## Revue du pilote",1)[0]
    if "Le journal explique ce qui a changé et pourquoi." not in relu or len(relu)!=177:
        raise ValueError("La section relue diffère du cas de démonstration attendu.")
    print("6 cellules exécutées depuis un nouveau noyau Python 3.")
    print("Notebook enregistré :",travail/"communication-assistee.ipynb")
    print("Markdown rouvert :",sortie)
    print(relu)
    print("SHA-256 :",hashlib.sha256(donnees).hexdigest())

if __name__=="__main__":
    main()
