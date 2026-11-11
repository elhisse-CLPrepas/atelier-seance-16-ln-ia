import './vendor/bootstrap.min.css'
import './style.css'
import content from './seance.json'
import {keys,formats,criteres,controle,comparer,relire,lireFiche,bilan,relais,traceWeb,txt} from './activites.js'
const $=s=>document.querySelector(s), $$=s=>Array.from(document.querySelectorAll(s))
const pad=n=>String(n).padStart(2,'0'), keyStore='lnia.s16.automne2026.1'
const esc=v=>String(v).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;')
const champs=$$('[id^="f-"]'), ids=champs.map(e=>e.name), caseData=content.cas
let memo={};try{memo=JSON.parse(localStorage.getItem(keyStore)||'{}')||{}}catch{}
let fields=Object.fromEntries(ids.map(k=>[k,typeof memo.fields?.[k]==='string'?memo.fields[k].slice(0,5000):'']))
let checks=criteres.map((_,i)=>memo.checks?.[i]===true), answers=content.quiz.map((q,i)=>Number.isInteger(memo.answers?.[i])&&memo.answers[i]>=0&&memo.answers[i]<q[1].length?memo.answers[i]:null)
let activeTest=null,revision=null,pending=null,ticket=0,step=0,card=0,flip=false,slide=0,notes=false
function persist(){try{localStorage.setItem(keyStore,JSON.stringify({fields,checks,answers}));$('#save-state').textContent='Brouillon conservé dans ce navigateur. Exportez votre travail avant de changer de poste.'}catch{$('#save-state').textContent='Stockage local indisponible. Copiez ou exportez avant de fermer.'}}
let toastTimer;function tell(s){$('#toast').textContent=s;clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('#toast').textContent='',2500)}
function downloadable(el,body,type='text/markdown'){el.href='data:'+type+';charset=utf-8,'+encodeURIComponent(body)}
function renderProof(){const raw=bilan(fields,checks);$('#proof-preview').textContent=raw;downloadable($('#index-export'),raw);downloadable($('#handoff-export'),relais(fields))}
function renderChecks(){$('#check-count').textContent=checks.filter(Boolean).length+' / '+criteres.length+' points déclarés. Décision du pilote en attente.'}
function clearReview(){revision=null;$('#review-result').textContent='';$('#export-rehearsal').hidden=true;$('#export-rehearsal').removeAttribute('href')}
function clearTest(){activeTest=null;$('#work-result').textContent='';clearReview()}
function renderCaseSummary(run){
 return '<div class="table-responsive my-3"><table class="table-s16"><thead><tr><th>Format</th><th>Avant</th><th>Après</th><th>Texte</th></tr></thead><tbody>'+formats.map(k=>{
 const a=controle(run.avant[k],fields.action||caseData.donnees.action),b=controle(run.apres[k],run.d.action)
 return '<tr><th>'+k+'</th><td>'+a.n+'</td><td>'+b.n+'</td><td>'+(run.modifies.includes(k)?'Modifié':'Identique')+' · '+esc(b.signal)+' · action exacte '+b.occ+'</td></tr>'}).join('')+'</tbody></table></div>'+formats.map(k=>'<details class="detail-note"><summary>Lire le brouillon '+k+' avant et après</summary><b>Avant</b><pre class="code-output">'+esc(run.avant[k])+'</pre><b>Après</b><pre class="code-output">'+esc(run.apres[k])+'</pre></details>').join('')
}
function route(first=false){const page=content.rubriques.find(v=>v[0]===location.hash.slice(1))||content.rubriques[0];$$('.page').forEach(el=>el.classList.toggle('is-active',el.id===page[0]));$$('[data-nav]').forEach(el=>el.dataset.nav===page[0]?el.setAttribute('aria-current','page'):el.removeAttribute('aria-current'));$('#crumb-page').textContent=page[1];$('#menu-toggle').setAttribute('aria-expanded','false');if(page[0]==='portfolio')renderProof();if(!first){window.scrollTo({top:0,behavior:'instant'});$('#contenu').focus({preventScroll:true})}}
$('#menu-toggle').onclick=e=>e.currentTarget.setAttribute('aria-expanded',String(e.currentTarget.getAttribute('aria-expanded')!=='true'))
window.addEventListener('hashchange',()=>route())
const dialog=$('#projection')
function drawSlide(){
 const d=content.slides[slide];$('#slide-no').textContent='DIAPOSITIVE '+pad(slide+1)+' / '+pad(content.slides.length);$('#slide-title').textContent=d.title;$('#slide-lead').textContent=d.lead
 const target=$('#slide-body')
 if(d.layout==='table'){target.innerHTML='<table><thead><tr>'+d.points[0].map(v=>'<th>'+esc(v)+'</th>').join('')+'</tr></thead><tbody>'+d.points.slice(1).map(r=>'<tr>'+r.map(t=>'<td>'+esc(t)+'</td>').join('')+'</tr>').join('')+'</tbody></table>'}
 else if(['pair','rows'].includes(d.layout)){target.innerHTML=d.points.map(([l,v])=>'<p class="presentation-pair"><b>'+esc(l)+'</b> '+esc(v)+'</p>').join('')}
 else{target.innerHTML=d.points.map(t=>'<p>'+esc(t)+'</p>').join('')}
 if(slide===0)target.prepend($('#affiche-projection').content.cloneNode(true))
 $('#slide-back').disabled=slide===0;$('#slide-forward').disabled=slide===content.slides.length-1
 $('#slide-notes').textContent='Pour le formateur · '+d.note;$('#slide-notes').hidden=!notes;$('#slide-note-toggle').setAttribute('aria-pressed',String(notes))
}
function shift(i){slide=Math.min(Math.max(i,0),content.slides.length-1);drawSlide()}
$$('[data-slide]').forEach(b=>b.onclick=()=>{notes=false;shift(Number(b.dataset.slide));dialog.showModal();$('#project-close').focus()})
$('#slide-back').onclick=()=>shift(slide-1);$('#slide-forward').onclick=()=>shift(slide+1);$('#slide-note-toggle').onclick=()=>{notes=!notes;drawSlide()};$('#project-close').onclick=()=>dialog.close()
$('#project-full').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else if(dialog.requestFullscreen)await dialog.requestFullscreen();else tell('Utilisez le plein écran de votre navigateur.')}catch{tell('La projection reste accessible dans cette fenêtre.')}}
dialog.addEventListener('close',()=>{if(document.fullscreenElement===dialog)document.exitFullscreen().catch(()=>{});notes=false})
document.addEventListener('keydown',e=>{if(!dialog.open)return;const k={ArrowLeft:slide-1,ArrowRight:slide+1,Home:0,End:content.slides.length-1};if(Object.hasOwn(k,e.key)){e.preventDefault();shift(k[e.key])}})
function showDemo(n){const items=$$('[data-panel]');step=Math.min(Math.max(n,0),items.length-1);items.forEach((el,i)=>el.classList.toggle('active',i===step));$$('[data-demo]').forEach((el,i)=>el.setAttribute('aria-pressed',String(i===step)));$('#demo-prev').disabled=step===0;$('#demo-next').disabled=step===items.length-1}
$$('[data-demo]').forEach(el=>el.onclick=()=>showDemo(+el.dataset.demo));$('#demo-prev').onclick=()=>showDemo(step-1);$('#demo-next').onclick=()=>showDemo(step+1)
$('#d-pred').onchange=()=>$('#d-result').replaceChildren()
$('#d-run').onclick=()=>{const q=$('#d-pred').value;if(!q){$('#d-result').textContent='Choisissez une prédiction avant de lancer la comparaison.';return}const e=caseData.essai;$('#d-result').innerHTML='<h4>'+(q==='professionnel'?'Votre prédiction correspond au résultat.':'Revenez aux champs utilisés par chaque gabarit.')+'</h4>'+renderCaseSummary({d:e.donnees,avant:e.avant,apres:e.versions,modifies:e.modifies})}
function sync(){for(const el of champs)el.value=fields[el.name]||''}
function fillEmpty(data){let n=0;for(const [k,v]of Object.entries(data)){if(ids.includes(k)&&v&&!txt(fields[k])){fields[k]=v;n++}}sync();clearTest();renderProof();persist();return n}
$('#load-case').onclick=()=>{if(keys.some(k=>(fields[k]&&fields[k]!==caseData.donnees[k])||(fields['ref_'+k]&&fields['ref_'+k]!==caseData.appuis[k]))){tell('Des données personnelles sont déjà présentes. Gardez-les ou utilisez un carnet vierge pour le cas fictif.');return}const c={...caseData.donnees,humaine:caseData.humaine,typeDossier:'Exemple fictif du guide S12'};keys.forEach(k=>c['ref_'+k]=caseData.appuis[k]);tell(fillEmpty(c)+' champs repris dans le carnet. La prédiction et la correction restent à renseigner.')}
function clearImport(){ticket++;pending=null;$('#s15-file').value='';$('#import-preview').hidden=true;$('#apply-import').hidden=true;$('#import-status').textContent=''}
$('#s15-file').onchange=async e=>{const idx=++ticket;pending=null;$('#apply-import').hidden=true;$('#import-preview').hidden=true;const f=e.target.files[0];if(!f)return;if(f.size>256000){$('#import-status').textContent='Choisissez un JSON S15 de moins de 250 Ko.';return}try{const parsed=lireFiche(JSON.parse((await f.text()).replace(/^\uFEFF/,'')));if(idx!==ticket)return;pending=parsed;$('#import-preview').textContent=keys.map(k=>k+' · '+parsed[k]+'\nAppui · '+parsed['ref_'+k]).join('\n\n');$('#import-preview').hidden=false;$('#apply-import').hidden=false;$('#import-status').textContent='Six valeurs et six appuis reconnus. Vérifiez-les avant de les reprendre.'}catch(err){if(idx===ticket)$('#import-status').textContent=err instanceof SyntaxError?'Ce fichier ne contient pas un JSON lisible.':err.message}}
$('#apply-import').onclick=()=>{if(!pending)return;const d=pending
 // Valeur et référence forment une paire. Une valeur personnelle existante garde son propre appui.
 const add={};for(const k of keys){if(!txt(fields[k])&&!txt(fields['ref_'+k])){add[k]=d[k];add['ref_'+k]=d['ref_'+k]}else if(fields[k]===d[k]&&!txt(fields['ref_'+k]))add['ref_'+k]=d['ref_'+k]}
 const n=fillEmpty(add);clearImport();$('#import-status').textContent=n+' champs repris. Ajoutez la version humaine S14 et indiquez l’origine de la fiche.'}
const reviewKeys=['choix','canal','avant','apres','motif','appui']
function fieldChanged(el){if(fields[el.name]===el.value)return;fields[el.name]=el.value;if(el.closest('#work')){if(reviewKeys.includes(el.name))clearReview();else clearTest()}renderProof();persist()}
for(const el of champs){el.addEventListener('input',()=>fieldChanged(el));el.addEventListener('change',()=>fieldChanged(el))}
for(const f of ['#work','#portfolio-form'])$(f).onsubmit=e=>e.preventDefault()
$('#try-change').onclick=()=>{clearTest();try{activeTest=comparer(fields);$('#work-result').innerHTML='<h4 class="mt-3">Résultats de la répétition JavaScript</h4>'+renderCaseSummary(activeTest)}catch(e){$('#work-result').textContent=e.message}}
$('#try-review').onclick=()=>{clearReview();try{revision=relire(activeTest,fields);$('#review-result').innerHTML='<p>La correction comporte '+revision.mesure.n+' caractères. Relisez son sens et l’action.</p><pre class="code-output">'+esc(revision.texte)+'</pre>';downloadable($('#export-rehearsal'),traceWeb(fields,activeTest,revision));$('#export-rehearsal').hidden=false}catch(e){$('#review-result').textContent=e.message}}
function showCard(){const [q,a]=content.cards[card];$('#flash-q').textContent=q;$('#flash-a').textContent=a;$('#flash-a').hidden=!flip;$('#flash-count').textContent='CARTE '+pad(card+1)+' / '+pad(content.cards.length);$('#flip').textContent=flip?'Masquer la réponse':'Révéler la réponse';$('#flip').setAttribute('aria-expanded',String(flip));$('#flash-prev').disabled=card===0;$('#flash-next').disabled=card===content.cards.length-1}
$('#flip').onclick=()=>{flip=!flip;showCard()};$('#flash-prev').onclick=()=>{card--;flip=false;showCard()};$('#flash-next').onclick=()=>{card++;flip=false;showCard()}
async function copy(text,el){try{await navigator.clipboard.writeText(text);tell('Texte copié.');return}catch{}const range=document.createRange();range.selectNodeContents(el);const sel=getSelection();sel.removeAllRanges();sel.addRange(range);if(document.execCommand('copy')){sel.removeAllRanges();tell('Texte copié.')}else tell('Texte sélectionné. Utilisez Ctrl+C.')}
$$('[data-copy]').forEach(b=>b.onclick=()=>copy(content.prompts[+b.dataset.copy][2],$('#prompt-'+b.dataset.copy)));$('#copy-proof').onclick=()=>{$('#proof-preview').closest('details').open=true;copy(bilan(fields,checks),$('#proof-preview'))}
function resetFeedback(){$$('.qfeedback').forEach(e=>e.hidden=true);$('#quiz-result').textContent='Chaque réponse reçoit une explication après correction.'}
$('#quiz-form').onchange=e=>{if(e.target.type==='radio'){answers[+e.target.name.slice(1)]=+e.target.value;resetFeedback();persist()}}
$('#quiz-form').onsubmit=e=>{e.preventDefault();let good=0;content.quiz.forEach(([,a,i,why],k)=>{const el=$('#feedback-'+k);el.hidden=false;el.className='qfeedback';if(answers[k]===null)el.textContent='Sans réponse.';else if(answers[k]===i){good++;el.classList.add('good');el.textContent='Réponse juste. '+why}else{el.classList.add('retry');el.textContent='Réponse attendue : '+a[i]+'. '+why}});$('#quiz-result').textContent=good+' / '+content.quiz.length+' réponses justes. Le pilote examinera les pièces de votre dossier.'}
$('#quiz-reset').onclick=()=>{answers.fill(null);$('#quiz-form').reset();resetFeedback();persist()}
$$('[data-criterion]').forEach((el,i)=>{el.checked=checks[i];el.onchange=()=>{checks[i]=el.checked;renderChecks();renderProof();persist()}})
$('#erase-first').onclick=()=>{$('#erase-confirm').hidden=false;$('#erase-no').focus()};$('#erase-no').onclick=()=>$('#erase-confirm').hidden=true
$('#erase-yes').onclick=()=>{fields={};checks.fill(false);answers.fill(null);sync();$('#quiz-form').reset();$$('[data-criterion]').forEach(e=>e.checked=false);clearImport();clearTest();resetFeedback();renderChecks();renderProof();try{localStorage.removeItem(keyStore)}catch{}$('#erase-confirm').hidden=true;$('#save-state').textContent='Les saisies S16 ont été effacées dans ce navigateur.'}
sync();answers.forEach((v,i)=>{if(v!==null)$('#quiz-form input[name="q'+i+'"][value="'+v+'"]').checked=true});route(true);showDemo(0);showCard();resetFeedback();renderChecks();renderProof()
