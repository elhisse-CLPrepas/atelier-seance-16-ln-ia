import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import {basename} from 'node:path'
import {Script} from 'node:vm'
import {affiches} from './affiches.mjs'
import {documentsPrompts} from './documents-prompts.mjs'
import {keys,formats,lireFiche,comparer,relire,controle,bilan,relais,traceWeb} from '../src/activites.js'
const root=new URL('../',import.meta.url),bytes=p=>fs.readFile(new URL(p,root)),read=async p=>(await bytes(p)).toString('utf8')
const d=JSON.parse(await read('src/seance.json')),c=d.cas,source=JSON.parse(await read('public/ressources/demo/donnees-s15-exemple.json'))
const f={...lireFiche(source),humaine:c.humaine,champ:c.champ,nouvelle:c.nouvelle,origine:c.origine,prediction:c.prediction,choix:c.choix,canal:c.canal,avant:c.avant,apres:c.apres,motif:c.motif,appui:c.appui}
const r=comparer(f),h=relire(r,f)
assert.deepEqual(r.avant,c.essai.avant);assert.deepEqual(r.apres,c.essai.versions);assert.deepEqual(r.modifies,['professionnel']);assert.equal(h.texte,c.revision.texte);assert.equal(h.mesure.n,177)
assert.deepEqual(formats.map(k=>controle(r.avant[k],f.action).n),[114,166,174]);assert.deepEqual(formats.map(k=>controle(r.apres[k],f.action).n),[114,166,184])
assert.equal(controle('7'.repeat(400),'7').signal,'Longueur acceptable');assert.equal(controle('7'.repeat(401),'7').signal,'À raccourcir');assert.equal(controle('x','').signal,'À compléter');assert.equal(controle('🙂é','é').n,2)
const blank=structuredClone(source);blank.champs[4].valeur=null;assert.throws(()=>lireFiche(blank),/action/);assert.throws(()=>lireFiche({schema:'autre'}));assert.throws(()=>comparer({...f,prediction:''}));assert.throws(()=>relire(r,{...f,apres:f.avant}));assert.throws(()=>relire(r,{...f,apres:'À compléter'}));assert.throws(()=>relire(r,{...f,avant:'Passage absent'}))
assert(bilan({obsS16:'Lu au poste',passageDisque:'Texte témoin'},[]).includes('Texte témoin'));assert(bilan({},[]).includes('Décision pédagogique de clôture : en attente.'));assert(relais({mTitre:'Préparer une semaine'}).includes('Préparer une semaine'));assert(traceWeb(f,r,h).includes('Répétition Web'))
const nav=['accueil','presentation','methode','demonstration','atelier','prompts','flashcards','quiz','validation','portfolio','ressources']
assert.deepEqual(d.rubriques.map(a=>a[0]),nav);assert.deepEqual([d.slides.length,d.cards.length,d.quiz.length,d.prompts.length],[18,8,6,4]);assert.equal(keys.length,6)
const files=[...d.groups.flatMap(([,g])=>g.map(([p])=>'ressources/'+p)),...affiches.map(([id])=>'ressources/affiches/'+id+'.png'),'ressources/atelier/poursuivre-s16.md',...documentsPrompts.map(([file])=>'ressources/prompts/'+file)];assert.equal(new Set(files).size,files.length)
const built=await read('dist/index.html'),offline=await read('OUVRIR-SEANCE-16.html')
for(const [index,[file]] of documentsPrompts.entries()){
 const original=await bytes('02-PROMPT/'+file)
 assert(original.equals(await bytes('public/ressources/prompts/'+file)),file)
 for(const html of [built,offline])assert(html.includes('id="document-prompt-'+index+'"')&&html.includes('data-copy-document="'+index+'"'),file)
}
for(const s of [built,offline]){for(const n of nav)assert(s.includes('id="'+n+'"')&&s.includes('href="#'+n+'"'));assert(s.includes('name="description"')&&s.includes('property="og:image"')&&s.includes('name="twitter:card"'));assert.equal(JSON.parse(s.match(/<script type="application\/ld\+json">([^<]+)</)[1]).timeRequired,'PT90M');const ids=[...s.matchAll(/\bid="([\w-]+)"/g)].map(m=>m[1]);assert.equal(new Set(ids).size,ids.length)}
for(const m of built.matchAll(/\b(?:href|src)="(\.\/[^"#]+)"/g))assert((await fs.stat(new URL('dist/'+m[1],root))).isFile(),m[1])
const embedded=new Map()
for(const m of offline.matchAll(/href="data:([a-z0-9+./-]+);base64,([A-Za-z0-9+/=]+)" data-resource="([^"]+)" download="([^"]+)"/g)){assert.equal(m[4],basename(m[3]));embedded.set(m[3],Buffer.from(m[2],'base64'))}
assert.equal(embedded.size,files.length)
for(const p of files){assert((await bytes('public/'+p)).equals(embedded.get(p)),p);assert((await bytes('dist/'+p)).equals(embedded.get(p)),p)}
assert(!/<script[^>]+src=|type="module"|<link[^>]+rel="stylesheet"|(?:href|src)="\.\/(?:assets|ressources)\//.test(offline));new Script([...offline.matchAll(/<script>([\s\S]*?)<\/script>/g)].at(-1)[1])
console.log('11 rubriques, 18 diapositives, 8 cartes, 6 questions, 4 prompts et '+files.length+' ressources autonomes identiques aux originaux.')
console.log('Import S15, formats, comptages, référence humaine, export de répétition, bilan et relais M05 contrôlés.')
