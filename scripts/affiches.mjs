import {mkdir,copyFile,readdir} from 'node:fs/promises'
const root=new URL('../',import.meta.url)
export const affiches=[['module-04','Module 04 · Communication assistée'],['seance-13','Séance 13 · Du guide au message'],['seance-14','Séance 14 · Un message, trois variantes'],['seance-15','Séance 15 · Vérifier une règle'],['seance-16','Séance 16 · Du notebook au message corrigé']]
export async function preparerAffiches(){
 const sources=await readdir(new URL('Affiches-module04/',root))
 await mkdir(new URL('public/ressources/affiches/',root),{recursive:true})
 for(const [id] of affiches){
  const numero=id.slice(-2)
  const source=sources.find(name=>id==='module-04'?name.startsWith('Module 04'):name.startsWith('Séance '+numero))
  if(!source)throw Error('Affiche manquante : '+id)
  await copyFile(new URL('Affiches-module04/'+source,root),new URL('public/ressources/affiches/'+id+'.png',root))
 }
}
export const figure=(id,titre)=>'<figure class="affiche"><img src="./ressources/affiches/'+id+'.png" alt="'+titre+'" loading="lazy"><figcaption>'+titre+'</figcaption></figure>'
