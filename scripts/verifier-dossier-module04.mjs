import {readFile,stat,readdir} from 'node:fs/promises'
import assert from 'node:assert/strict'
const root=new URL('../mon-dossier-challenge-MODULE-04/',import.meta.url)
const html=await readFile(new URL('ACCUEIL-MODULE-04.html',root),'utf8')
const liens=[...html.matchAll(/(?:href|src)="([^"#]+)"/g)].map(match=>match[1])
for(const lien of liens)assert((await stat(new URL(lien,root))).isFile(),lien)
for(const nom of ['05-automatisation/communication-assistee.ipynb','08-demonstration/guide/ressources/communication-assistee-demonstration.ipynb']){
 const carnet=JSON.parse(await readFile(new URL(nom,root),'utf8'))
 assert.equal(carnet.nbformat,4)
 assert(carnet.cells.some(cell=>cell.cell_type==='code'))
}
assert(!(await readdir(root)).includes('.git'))
console.log(liens.length+' liens et images disponibles ; deux notebooks lisibles ; historique Git non dupliqué.')
