import {mkdir,copyFile,readFile} from 'node:fs/promises'
export const documentsPrompts=[
 ['01-INSTRUCTIONS-PARTICIPANT-S16.md','Instructions participant S16','Le parcours de 90 minutes : préparer, exécuter, corriger et présenter la preuve.'],
 ['02-PROMPT-MAÎTRE-S16.md','Prompt maître S16','Un accompagnement par l’assistant, étape par étape, à copier avec les pièces nécessaires.']
]
export async function preparerDocumentsPrompts(){
 const root=new URL('../',import.meta.url)
 await mkdir(new URL('public/ressources/prompts/',root),{recursive:true})
 return Promise.all(documentsPrompts.map(async([file,title,description])=>{
  await copyFile(new URL('02-PROMPT/'+file,root),new URL('public/ressources/prompts/'+file,root))
  return {file,title,description,texte:await readFile(new URL('02-PROMPT/'+file,root),'utf8')}
 }))
}
