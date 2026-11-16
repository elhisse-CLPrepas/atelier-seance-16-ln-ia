import { readFile, writeFile } from 'node:fs/promises';
import { buildHandoff } from '../../src/portfolio.js';
const dir = new URL('../', import.meta.url);
const values = {
 projet: 'Situation-Actuelle-IA',
 public: 'Professionnels et formateurs',
 besoin: 'Production avancée IA avec méthode, tout en gardant le contrôle humain',
 proposition: 'Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle.',
 action: 'Consultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/',
 format: 'professionnel'
};
const refs = {
 projet: 'Projet demandé par le participant ; titre du guide V5, page 2. Titre court du projet pour le gabarit S16.',
 public: 'Professionnels et formateurs : public proposé puis explicitement confirmé par le participant le 16 novembre 2026 ; guide V5, page 28.',
 besoin: 'Formulation explicitement donnée par le participant le 16 novembre 2026 : production avancée IA avec méthode, tout en gardant le contrôle humain. Guide V5, page 2 (méthode), pages 9 et 10 (production avancée et pilotage humain).',
 proposition: 'Proposition du gabarit acceptée à étape 2 ; guide V5, pages 2 et 4.',
 action: 'Action du message accepté ; URL fournie par le participant.',
 format: 'Choix technique provisoire de variante par assistant pour amorcer S16 ; canal LinkedIn confirmé par la demande initiale. Ce format reste modifiable.'
};
const fields = {};
for (const k of Object.keys(values)) { fields['s16_'+k] = values[k]; fields['ref_'+k] = refs[k]; }
fields.limite = 'La longueur ne vérifie ni les faits ni la qualité du message.';
// Observations transmises après export : buildHandoff associe autrement ces sorties au navigateur.
const fiche = buildHandoff(fields);
fiche.seance = 'S15 · travail du 16 novembre 2026';
fiche.moteur_observe = 'Python 3.14.5 — tests réellement exécutés';
fiche.essais = [{longueur:400,prediction:null,observation:'Longueur acceptable'},{longueur:401,prediction:null,observation:'À raccourcir'}];
fiche.regle_decrite_par_le_candidat = null;
fiche.regle = 'Règle du support appliquée : vide ou espaces seuls → À compléter ; sinon longueur > 400 → À raccourcir ; sinon Longueur acceptable.';
fiche.canal = 'LinkedIn';
fiche.titre_message = 'Comment produire avec méthode ?';
fiche.provenance_export = 'Fonction officielle buildHandoff de src/portfolio.js exécutée en Node.js ; métadonnées adaptées explicitement à exécution Python réelle et à date du travail. Aucun clic navigateur prétendu.';
const target = new URL('04-communication/donnees-pour-s16.json', dir);
// Préserver un éventuel export existant différent.
const content = JSON.stringify(fiche,null,2)+'\n';
let ancien; try { ancien = await readFile(target,'utf8'); } catch(e) { if(e.code !== 'ENOENT') throw e; }
if(ancien && ancien !== content) throw new Error('Un export différent existe déjà : conservation exigée avant remplacement.');
await writeFile(target, content, 'utf8');
const relu = JSON.parse(await readFile(target,'utf8'));
if(relu.champs.length !== 6 || relu.essais.some(x=>x.prediction !== null)) throw new Error('Contrôle export échoué.');
console.log('Export S16 réel enregistré ; 6 champs avec appuis ; prédictions absentes préservées.');
