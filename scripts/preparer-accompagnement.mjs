import {readFile,writeFile,cp,mkdir} from 'node:fs/promises'
const dossier='mon-dossier-challenge-MODULE-04/08-accompagnement-S15-S16'
const web='public/ressources/accompagnement-s15-s16'
await mkdir(web,{recursive:true})
await cp(dossier,web,{recursive:true})
const carnet=JSON.parse(await readFile(dossier+'/communication-assistee-s16-situation-actuelle-ia.ipynb','utf8'))
for(const cell of carnet.cells){
 let text=cell.source.join('')
 if(cell.cell_type==='code' && text.includes('base = Path.cwd().resolve()')){
  const start=text.indexOf('base = Path.cwd().resolve()')
  const end=text.indexOf('fiche = ',start)
  text=text.slice(0,start)+'# Rejouer dans un espace dédié, sans toucher au projet personnel.\nracine = Path.cwd().resolve() / "demo-situation-actuelle-ia"\n'+text.slice(end)
 }
 text=text.replaceAll('variantes-communication-projet.md','variantes-communication-exemple.md').replaceAll('variantes-communication-projet-v','variantes-communication-exemple-v')
 if(cell.cell_type==='code'){cell.outputs=[];cell.execution_count=null}
 cell.source=text.split(/(?<=\n)/)
}
carnet.cells.unshift({cell_type:'markdown',metadata:{},source:['# Rejouer l’exemple pédagogique en sécurité\n','Copie de travail du parcours S15–S16. Les sorties historiques figurent dans le notebook original. Cette copie attend votre exécution.\n','L’export est réservé à `demo-situation-actuelle-ia/04-communication/variantes-communication-exemple.md`, sous le dossier courant. Vérifiez le chemin affiché avant l’export.\n','Les références documentaires sont celles des traces originales ; la décision pédagogique du pilote reste en attente.']})
await writeFile(web+'/rejouer-exemple-s16.ipynb',JSON.stringify(carnet,null,1)+'\n')
await writeFile(web+'/LIRE-AVANT-DE-REJOUER.md','# Exemple pédagogique Situation-Actuelle-IA\n\nLe dossier 08-accompagnement-S15-S16 est une copie des traces produites en S15. Pour le groupe, il sert de cas de démonstration, distinct du projet de chaque candidat.\n\nTéléchargez rejouer-exemple-s16.ipynb et exécutez ses six cellules dans l’ordre avec Python 3. Le répertoire demo-situation-actuelle-ia est réservé aux exports fictifs. Le notebook original conserve les sorties historiques ; les anciens scripts restent des traces de travail et peuvent dépendre du dossier S15.\n\nLe message de référence est une proposition IA acceptée, pas une rédaction humaine S14 antérieure. La prédiction historique vient de l’assistant. Recueillez votre propre prédiction avant de lancer la comparaison. Le message final compte 284 points de code ; une longueur acceptable ne vérifie pas les faits. Réouverture personnelle et décision du pilote restent à documenter. Aucun message LinkedIn n’est envoyé par cet atelier.\n')
