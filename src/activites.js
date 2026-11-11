export const keys=['projet','public','besoin','proposition','action','format']
export const formats=['court','accessible','professionnel']
export const criteres=['Je retrouve le passage source et la rédaction humaine de S14.','Mon notebook enregistré montre les six cellules et trois brouillons.','Je peux expliquer la prédiction et l’effet d’un seul changement.','Ma correction, mon motif et mon appui sont visibles.','Je retrouve le passage corrigé dans le Markdown rouvert sur mon poste.']
export const preuves=[
 ['S13','preuve-13-processus-communication-assistee','04-communication/comprendre-processus-communication.md'],
 ['S14','preuve-14-message-projet-et-variantes','04-communication/message-court-projet.md'],
 ['S15','preuve-15-regles-adaptation-automatisation','04-communication/comprendre-regles-automatisation.md'],
 ['S16','preuve-16-notebook-communication-assistee','05-automatisation/communication-assistee.ipynb et 04-communication/variantes-communication-projet.md']
]
export const txt=v=>typeof v==='string'?v.trim():''
export const rempli=v=>!!txt(v)&&!/à\s+(compléter|confirmer|renseigner|vérifier)/i.test(v)
export const compte=v=>Array.from(v).length
export function lireFiche(obj){
 if(obj?.schema!=='ln-ia-preparation-s16/v1'||!Array.isArray(obj.champs))throw Error('Choisissez le JSON exporté par le portfolio S15.')
 const res={};for(const row of obj.champs){if(!row||typeof row!=='object')throw Error('Ligne de données illisible.');if(!keys.includes(row.champ))continue;if(Object.hasOwn(res,row.champ))throw Error('Champ présent deux fois : '+row.champ);res[row.champ]=txt(row.valeur);res['ref_'+row.champ]=txt(row.source_ou_justification)}
 const vides=keys.filter(k=>!rempli(res[k])||!rempli(res['ref_'+k]));if(vides.length)throw Error('À compléter dans S15 (valeur et appui) : '+vides.join(', '))
 if(Object.values(res).some(v=>v.length>5000))throw Error('Réduisez les champs à 5 000 caractères avant la reprise dans le carnet Web.')
 return res
}
export function versions(d){return {court:d.proposition+' '+d.action,accessible:'Bonjour ! Votre besoin : '+d.besoin.replace(/[.!?]+$/,'')+'.\n'+d.proposition+' '+d.action,professionnel:'Objet : '+d.projet+'\nPublic : '+d.public+'\n'+d.proposition+' '+d.action}}
export function controle(t,a){return {n:compte(t),signal:!rempli(t)||!rempli(a)?'À compléter':compte(t)>400?'À raccourcir':'Longueur acceptable',occ:rempli(a)?t.split(a).length-1:0}}
export function comparer(f){
 const valeurs={},refs={};for(const k of keys){valeurs[k]=txt(f[k]);refs[k]=txt(f['ref_'+k]);if(!rempli(valeurs[k])||!rempli(refs[k]))throw Error('Complétez le champ '+k+' et son appui.')}
 if(!rempli(f.humaine))throw Error('Ajoutez votre rédaction humaine S14 ou utilisez le cas fictif.')
 if(!keys.slice(0,5).includes(f.champ))throw Error('Choisissez le champ qui va changer.')
 if(![f.nouvelle,f.origine,f.prediction].every(rempli))throw Error('Saisissez la nouvelle valeur, son appui et votre prédiction.')
 if(valeurs[f.champ]===txt(f.nouvelle))throw Error('Changez réellement la valeur du champ.')
 const d={...valeurs,[f.champ]:txt(f.nouvelle)},avant=versions(valeurs),apres=versions(d)
 return {d,avant,apres,modifies:formats.filter(n=>avant[n]!==apres[n]),refs}
}
export function relire(run,f){
 if(!run)throw Error('Calculez les brouillons après avoir écrit votre prédiction.')
 if(!formats.includes(f.choix)||![f.avant,f.apres,f.motif,f.appui,f.canal].every(rempli))throw Error('Renseignez le format, les deux passages, le motif, l’appui et le canal.')
 const brut=run.apres[f.choix],a=txt(f.avant),b=txt(f.apres)
 if(brut.split(a).length!==2)throw Error('Le passage avant doit apparaître une seule fois dans le brouillon choisi.')
 if(a.replace(/\s+/g,' ')===b.replace(/\s+/g,' '))throw Error('Écrivez un passage différent et expliquez la correction.')
 const t=brut.replace(a,()=>b),m=controle(t,run.d.action);if(m.signal!=='Longueur acceptable'||m.occ!==1)throw Error('Vérifiez la longueur et la présence exacte de l’action dans le texte final.')
 return {texte:t,mesure:m}
}
export function bilan(f,checks){
 const get=k=>txt(f[k])||'[À compléter]'
 return ['# Entrées à ajouter au portfolio du Module 04','','Réunion de clôture · 16 novembre 2026','Date réelle de la revue : '+get('dateRevue'),'Origine des données : '+get('typeDossier'),'','Les observations ci-dessous sont déclarées. Le pilote statue après examen.','',
 ...preuves.flatMap(([s,id,path])=>['## '+s+' · '+id,'Pièce(s) : '+path,'Observation : '+get('obs'+s),'Écart, reprise ou correction : '+get('reprise'+s),'Statut et décision datée du pilote : à renseigner.','']),
 '## Passage retrouvé dans le vrai Markdown Python',get('passageDisque'),'','## Autoévaluation préparatoire',...criteres.map((v,i)=>'- ['+(checks[i]?'x':' ')+'] '+v),'','Décision pédagogique de clôture : en attente.','Autorisation de diffusion : décision distincte.',''].join('\n')
}
export function relais(f){const g=k=>txt(f[k])||'[À compléter]';return ['# Extrait de travail pour le Module 05','','Titre : '+g('mTitre'),'','Paragraphe relu :',g('mPara'),'','Action : '+g('mAction'),'Source et rubrique : '+g('mSource'),'Statut de la version : '+g('mStatut'),'Autorisation de diffusion : à renseigner séparément.',''].join('\n')}
export function traceWeb(f,run,rev){return ['# Répétition Web S16','Simulation JavaScript locale · BROUILLON — À RELIRE','Cette fiche décrit la répétition dans le navigateur. La preuve S16 se présente avec le notebook exécuté et le Markdown rouvert.','', 'Source de travail : '+txt(f.typeDossier),'Rédaction humaine S14 : '+txt(f.humaine),'Champ : '+f.champ,'Avant : '+txt(f[f.champ]),'Après : '+txt(f.nouvelle),'Appui du changement : '+txt(f.origine),'Prédiction : '+txt(f.prediction),'Formats modifiés : '+(run.modifies.join(', ')||'aucun'),'',...formats.flatMap(k=>['## '+k,'Avant :',run.avant[k],'Après :',run.apres[k],'']),'## Ma correction',txt(f.avant),'→ '+txt(f.apres),'Motif : '+txt(f.motif),'Appui : '+txt(f.appui),'Canal : '+txt(f.canal),'','## Message corrigé',rev.texte,''].join('\n')}
