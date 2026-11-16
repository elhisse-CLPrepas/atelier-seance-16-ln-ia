# -*- coding: utf-8 -*-
# Version Python du notebook S16 personnalisé.
# Cellules exécutables dans VS Code (# %%) ou avec Python 3.
# La dernière cellule exporte le Markdown local et préserve une version précédente.

# %% [markdown]
# # S16 — Production avancée IA avec méthode
#
# **Projet : Situation-Actuelle-IA · Canal : LinkedIn · Travail du 16 novembre 2026.**
#
# Carnet personnalisé à six cellules de code, fondé sur le support S16 original. Les cellules sont exécutées de haut en bas sous Python et leurs sorties sont enregistrées. Aucun noyau Jupyter n’a été utilisé lors de la génération.
#
# **Résultats :** seule la variante professionnelle change lorsque le public est précisé ; le message LinkedIn corrigé compte **284 points de code** et conserve une occurrence exacte de l’action.
#
# Les textes et la correction ont été proposés par l’assistant puis acceptés par le participant. La prédiction technique est celle de l’assistant ; aucune prédiction personnelle ni rédaction humaine S14 antérieure n’est inventée. La décision du pilote sur la preuve et la réouverture personnelle restent en attente. Aucun message publié.
#
# ## Utilisation
# Ouvrir ce fichier dans Jupyter ou VS Code, choisir un noyau Python 3 et exécuter les cellules dans l’ordre. Seule la bibliothèque standard est nécessaire. Les données sont embarquées ; aucune connexion réseau n’est requise. La dernière cellule écrit un Markdown local et conserve une ancienne version si nécessaire.
#
# ## Sources
# Guide V5 local : `../01-exemple-sa-ia/guide-situation-actuelle-IA-publication-V5.pdf`, pages 2 et 4 ; statut page 28 : « Prêt pour relecture humaine finale ». Public, besoin et correction confirmés dans le chat ; export S15 : `../04-communication/donnees-pour-s16.json`.

# %% [markdown]
# ## 1. Charger les six champs et leurs appuis
#
# Les données initiales conservent le public général pour permettre une comparaison réelle avant/après. Le public précisé accepté sera appliqué en cellule 4. Le champ `format` désigne la variante professionnelle ; le canal est LinkedIn.

# %%
# 1. Données réelles de S15 et appuis, embarqués pour rendre le carnet portable.
# Aucun cas fictif, clé API ou accès réseau requis. Python 3, bibliothèque standard.
MODE_SOURCE = "export S15 embarqué"
TEXTE_REFERENCE_S15 = 'Comment produire avec méthode ? — Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle. Consultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/'
from pathlib import Path
import json, re

CHAMPS = ("projet", "public", "besoin", "proposition", "action", "format")
FORMATS = ("court", "accessible", "professionnel")
SEUIL = 400

def renseigne(valeur):
    return (isinstance(valeur, str) and bool(valeur.strip())
            and not re.search(r"à\s+(?:compléter|confirmer|renseigner|vérifier)", valeur, re.I))

def dossier_de_travail(emplacement=""):
    base = Path(emplacement).expanduser().resolve() if emplacement else Path.cwd().resolve()
    return base.parent if base.name == "05-automatisation" else base

def lire_fiche(document):
    if not isinstance(document, dict) or document.get("schema") != "ln-ia-preparation-s16/v1":
        raise ValueError("Choisissez le JSON « données S16 » exporté depuis le portfolio S15.")
    lignes = document.get("champs")
    if not isinstance(lignes, list):
        raise ValueError("La liste des champs S15 manque.")
    valeurs, appuis = {}, {}
    for ligne in lignes:
        if not isinstance(ligne, dict):
            raise ValueError("Chaque ligne doit contenir un champ, une valeur et sa source.")
        champ = ligne.get("champ")
        if champ not in CHAMPS:
            continue
        if champ in valeurs:
            raise ValueError("Champ présent deux fois dans la fiche : " + champ)
        valeurs[champ] = ligne.get("valeur")
        appuis[champ] = ligne.get("source_ou_justification")
    manques = [c for c in CHAMPS if not renseigne(valeurs.get(c)) or not renseigne(appuis.get(c))]
    if manques:
        raise ValueError("À compléter dans S15 (valeur et source) : " + ", ".join(manques))
    return ({k: v.strip() for k, v in valeurs.items()},
            {k: v.strip() for k, v in appuis.items()})

def extraire_version_humaine(texte):
    bloc = re.search(r"^##[ \t]+Version humaine S14[ \t]*\n(.*?)(?=^##[ \t]+|\Z)",
                     texte.replace("\r\n", "\n"), flags=re.M | re.S)
    return bloc.group(1).strip() if bloc else ""



# Racine : dossier candidat si détecté, sinon dossier courant.
# Vous pouvez remplacer cette recherche par Path("chemin/du/dossier").resolve().
base = Path.cwd().resolve()
candidats = [base, *base.parents]
racine = next((p for p in candidats if (p / "04-communication").is_dir()), None)
if racine is None:
    racine = next((p / "mon-dossier-challenge-module04" for p in candidats
                   if (p / "mon-dossier-challenge-module04" / "04-communication").is_dir()), base)
fiche = {'schema': 'ln-ia-preparation-s16/v1', 'seance': 'S15 · travail du 16 novembre 2026', 'statut': 'BROUILLON — À RELIRE', 'champs': [{'champ': 'projet', 'valeur': 'Situation-Actuelle-IA', 'source_ou_justification': 'Projet demandé par le participant ; titre du guide V5, page 2. Titre court du projet pour le gabarit S16.'}, {'champ': 'public', 'valeur': 'Professionnels et formateurs', 'source_ou_justification': 'Professionnels et formateurs : public proposé puis explicitement confirmé par le participant le 16 novembre 2026 ; guide V5, page 28.'}, {'champ': 'besoin', 'valeur': 'Production avancée IA avec méthode, tout en gardant le contrôle humain', 'source_ou_justification': 'Formulation explicitement donnée par le participant le 16 novembre 2026 : production avancée IA avec méthode, tout en gardant le contrôle humain. Guide V5, page 2 (méthode), pages 9 et 10 (production avancée et pilotage humain).'}, {'champ': 'proposition', 'valeur': 'Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle.', 'source_ou_justification': 'Proposition du gabarit acceptée à étape 2 ; guide V5, pages 2 et 4.'}, {'champ': 'action', 'valeur': 'Consultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/', 'source_ou_justification': 'Action du message accepté ; URL fournie par le participant.'}, {'champ': 'format', 'valeur': 'professionnel', 'source_ou_justification': 'Choix technique provisoire de variante par assistant pour amorcer S16 ; canal LinkedIn confirmé par la demande initiale. Ce format reste modifiable.'}], 'regle_decrite_par_le_candidat': None, 'regle_etalon': {'precondition': 'texte renseigné', 'test': 'longueur > 400', 'si_vrai': 'À raccourcir', 'sinon': 'Longueur acceptable'}, 'moteur_observe': 'Python 3.14.5 — tests réellement exécutés', 'essais': [{'longueur': 400, 'prediction': None, 'observation': 'Longueur acceptable'}, {'longueur': 401, 'prediction': None, 'observation': 'À raccourcir'}], 'limite': 'La longueur ne vérifie ni les faits ni la qualité du message.', 'decision_du_pilote': None, 'regle': 'Règle du support appliquée : vide ou espaces seuls → À compléter ; sinon longueur > 400 → À raccourcir ; sinon Longueur acceptable.', 'canal': 'LinkedIn', 'titre_message': 'Comment produire avec méthode ?', 'provenance_export': 'Fonction officielle buildHandoff de src/portfolio.js exécutée en Node.js ; métadonnées adaptées explicitement à exécution Python réelle et à date du travail. Aucun clic navigateur prétendu.'}
origine_fiche = "Export S15 réel embarqué ; fonction buildHandoff, métadonnées Python documentées."
texte_s14 = TEXTE_REFERENCE_S15  # Nom technique hérité ; ce texte est une proposition IA acceptée.
donnees, appuis = lire_fiche(fiche)
source_initiale = initiales = essai = revision = None
regle_s15 = fiche.get("regle") or "Règle du support S15."
print("Dossier de travail :", racine)
print("Source : export réel S15 embarqué ; message de référence IA accepté.")
for champ in CHAMPS:
    print(f"{champ} : {donnees[champ]} | Appui : {appuis[champ]}")
print("Règle reprise de S15 :", regle_s15)

# %% [markdown]
# ## 2. Comparer le message de référence et le gabarit
#
# Le message de référence provient des propositions IA acceptées pendant S15.

# %%
# 2. Comparez le gabarit à votre version humaine.
source_initiale = initiales = essai = revision = None
def message_source(d):
    return f"{d['projet']} — {d['proposition']} {d['action']}"


if donnees is None or not renseigne(texte_s14):
    print("À COMPLÉTER · vérifiez la cellule 1 et le message de référence S15.")
else:
    source_initiale = message_source(donnees)
    print("RÉFÉRENCE S15 — PROPOSITION IA ACCEPTÉE\n" + texte_s14)
    print("\nGABARIT S16 · BROUILLON — À RELIRE\n" + source_initiale)

# %% [markdown]
# ## 3. Produire les trois variantes
#
# Les gabarits court, accessible et professionnel utilisent des champs différents. Tous les textes sont des brouillons.

# %%
# 3. Affichez les trois premiers brouillons.
initiales = essai = revision = None
def variantes(d):
    return {
        "court": f"{d['proposition']} {d['action']}",
        "accessible": f"Bonjour ! Votre besoin : {d['besoin'].rstrip('.!?')}.\n{d['proposition']} {d['action']}",
        "professionnel": f"Objet : {d['projet']}\nPublic : {d['public']}\n{d['proposition']} {d['action']}",
    }


if source_initiale is None:
    print("Reprenez la comparaison en cellule 2.")
else:
    initiales = variantes(donnees)
    for nom, texte in initiales.items():
        print(f"\n{nom.upper()} · BROUILLON — À RELIRE\n{texte}")

# %% [markdown]
# ## 4. Modifier le public et contrôler
#
# Public confirmé : **Professionnels et formateurs débutant en production avancée IA**. Prédiction fournie par l’assistant et explicitement étiquetée. Une prédiction personnelle n’a pas été recueillie avant ce test.

# %%
# 4. Avant de lancer : écrivez la prédiction, la valeur modifiée et sa source.
CHAMP = "public"
NOUVELLE = 'Professionnels et formateurs débutant en production avancée IA'
ORIGINE = 'Public proposé par assistant puis explicitement accepté par le participant : je valide le public. Échange S16 du 16 novembre 2026.'
PREDICTION = 'Prédiction de l’assistant, non du participant : seul le format professionnel changera, car seul ce gabarit affiche le champ public.'
essai = revision = None
def mesurer(texte, action):
    present = renseigne(texte) and renseigne(action)
    return {"longueur": len(texte), "presence": bool(present),
            "signal": "À compléter" if not present else ("À raccourcir" if len(texte) > SEUIL else "Longueur acceptable"),
            "action_exacte": texte.count(action) if renseigne(action) else 0}

def comparer(valeurs, champ, nouvelle, origine, prediction):
    if champ not in CHAMPS or champ == "format":
        raise ValueError("Choisissez projet, public, besoin, proposition ou action. Le format est un choix éditorial.")
    if not all(renseigne(x) for x in [nouvelle, origine, prediction]):
        raise ValueError("Écrivez votre prédiction, la nouvelle valeur et sa justification avant de relancer.")
    if valeurs[champ] == nouvelle.strip():
        raise ValueError("La nouvelle valeur doit permettre une comparaison.")
    apres = dict(valeurs)
    apres[champ] = nouvelle.strip()
    avant, versions = variantes(valeurs), variantes(apres)
    return dict(initial=dict(valeurs), donnees=apres, champ=champ, origine=origine.strip(),
                prediction=prediction.strip(), avant=avant, versions=versions,
                modifies=[k for k in FORMATS if avant[k] != versions[k]],
                controles={k: mesurer(t, apres["action"]) for k, t in versions.items()})


action = donnees["action"] if donnees else ""
for n in (400, 401):
    etalon = "0123456789" * 40 + ("X" if n == 401 else "")
    print("Étalon", n, "·", mesurer(etalon, action)["signal"])
print("Action vide ·", mesurer("Un brouillon.", "")["signal"])
if initiales is None:
    print("Exécutez d’abord les cellules 1 à 3.")
else:
    try:
        essai = comparer(donnees, CHAMP, NOUVELLE, ORIGINE, PREDICTION)
    except ValueError as erreur:
        print("À COMPLÉTER ·", erreur)
if essai is not None:
    print("Prédiction :", essai["prediction"])
    print("Champ modifié :", CHAMP, "|", donnees[CHAMP], "→", essai["donnees"][CHAMP])
    print("Gabarit source relancé :", message_source(essai["donnees"]))
    for nom in FORMATS:
        print("\n"+nom.upper(), "MODIFIÉ" if nom in essai["modifies"] else "IDENTIQUE")
        print("Avant :", essai["avant"][nom], "\nAprès :", essai["versions"][nom])
        print("Contrôle :", essai["controles"][nom])

# %% [markdown]
# ## 5. Appliquer la correction LinkedIn validée
#
# Le participant a accepté cette adaptation dans le chat. Le code conserve AVANT / APRÈS / MOTIF / APPUI et vérifie la longueur et une occurrence exacte de l’action. Ces contrôles ne prouvent pas la vérité du contenu.

# %%
# 5. Choisissez le format et complétez la correction avec vos mots.
CHOIX = "professionnel"
AVANT = 'Objet : Situation-Actuelle-IA\nPublic : Professionnels et formateurs débutant en production avancée IA\nLe guide Situation-Actuelle-IA propose une démarche de production et de contrôle. Consultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/'
APRES = 'Comment produire avec méthode ?\n\nVous débutez en production avancée IA ? Le guide Situation-Actuelle-IA propose une démarche de production et de contrôle, tout en gardant le pilotage humain.\n\nConsultez le mini-site : https://elhisse-clprepas.github.io/mini-site-situation-actuelle-ia/'
MOTIF = 'Adaptation LinkedIn proposée par l’assistant puis explicitement validée par le participant : oui je valide. Remplacer les étiquettes Objet et Public par le titre retenu et une adresse directe au lecteur ; rappeler le pilotage humain.'
APPUI = 'Guide Situation-Actuelle-IA V5, page 2 : sous-titre mentionnant pilotage humain et production avec méthode ; page 4 : produire et contrôler. Public précisé et adaptation finale acceptés dans le chat.'
CANAL = 'LinkedIn'
revision = None
def corriger(essai, choix, avant, apres, motif, appui, canal):
    if choix not in FORMATS:
        raise ValueError("Choisissez court, accessible ou professionnel.")
    if not all(renseigne(x) for x in [avant, apres, motif, appui, canal]):
        raise ValueError("Renseignez le passage avant, sa correction, le motif, l’appui et le canal.")
    avant, apres = avant.strip(), apres.strip()
    brut = essai["versions"][choix]
    if brut.count(avant) != 1:
        raise ValueError("Le passage avant doit apparaître exactement une fois dans le brouillon choisi.")
    if ' '.join(avant.split()) == ' '.join(apres.split()):
        raise ValueError("Saisissez une correction qui change réellement le passage.")
    texte = brut.replace(avant, apres, 1)
    controle = mesurer(texte, essai["donnees"]["action"])
    if controle["signal"] != "Longueur acceptable" or controle["action_exacte"] != 1:
        raise ValueError("Reprenez la correction. Le texte final doit respecter le seuil et conserver une occurrence de l’action.")
    return dict(choix=choix, brut=brut, avant=avant, apres=apres, texte=texte,
                motif=motif.strip(), appui=appui.strip(), canal=canal.strip(), controle=controle)


if essai is None:
    print("Reprenez le changement de donnée en cellule 4.")
else:
    try:
        revision = corriger(essai, CHOIX, AVANT, APRES, MOTIF, APPUI, CANAL)
        print("Avant :", revision["avant"], "\nAprès :", revision["apres"])
        print("Brouillon corrigé :\n"+revision["texte"]+"\nMotif : "+revision["motif"])
        print("Contrôle du texte corrigé :", revision["controle"])
    except ValueError as erreur:
        print("À COMPLÉTER ·", erreur)

# %% [markdown]
# ## 6. Exporter et relire le Markdown
#
# La dernière cellule écrit `04-communication/variantes-communication-projet.md` dans la racine détectée, conserve une ancienne version si nécessaire, relit le résultat et calcule son SHA-256. Il s’agit d’une relecture technique, distincte d’une réouverture par le participant.

# %%
# 6. Exécutez, puis ouvrez le fichier annoncé. Conservez le notebook avec ses sorties.
import hashlib
import os
import tempfile
from contextlib import contextmanager

def composer_trace(essai, correction, refs, version_s14, mode, source_fiche, regle_s15):
    d = essai["donnees"]
    bloc = ["# Variantes de communication de mon projet", "", "S16 · 16 novembre 2026",
            "BROUILLON — À RELIRE", "Preuve à examiner : preuve-16-notebook-communication-assistee",
            "Origine des données : " + mode + " · " + source_fiche,
            "Décision du pilote : en attente.", "", "## Mes données et leurs sources"]
    for cle in CHAMPS:
        repere = essai["origine"] if cle == essai["champ"] else refs[cle]
        bloc.extend([f"- {cle} : {d[cle]} · Appui : {repere}"])
    bloc += ["", "## Référence S15 — proposition IA acceptée", version_s14, "", "## Message source avant la modification", message_source(essai["initial"]),
             "", "## Message source après la modification", message_source(d), "", "## Prédiction assistant et résultat — prédiction participant non recueillie",
             f"Champ : {essai['champ']}", "Avant : "+essai["initial"][essai["champ"]], "Après : "+d[essai["champ"]],
             "Justification : "+essai["origine"], "Prédiction : "+essai["prediction"],
             "Formats modifiés : "+(", ".join(essai["modifies"]) or "aucun"),
             "Règle indiquée en S15 : "+regle_s15, "Règle exécutée : texte renseigné, seuil de 400 caractères et une occurrence exacte de l’action."]
    for cle in FORMATS:
        m=essai["controles"][cle]
        bloc += ["", "## Brouillon "+cle, "Avant le changement du champ :", essai["avant"][cle],
                 "", "Après le changement du champ :", essai["versions"][cle],
                 f"Mesure : {m['longueur']} caractères · {m['signal']} · action exacte : {m['action_exacte']}."]
    bloc += ["","## Correction proposée par assistant et validée par participant", "Choix : "+correction["choix"], "Canal : "+correction["canal"],
             "Passage avant : "+correction["avant"], "Passage après : "+correction["apres"],
             "Motif : "+correction["motif"], "Appui : "+correction["appui"],
             "", "## Message corrigé", "", correction["texte"], "",
             "## Revue du pilote", "Fait observé, date et décision : en attente.", ""]
    return "\n".join(bloc)

@contextmanager
def verrou_export(dossier):
    verrou=dossier/".export-s16.lock"
    try:
        fd=os.open(verrou,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:
        raise RuntimeError("Un export est déjà en cours. Après une interruption, fermez les autres processus avant de retirer .export-s16.lock.") from None
    try:
        os.close(fd)
        yield
    finally:
        verrou.unlink(missing_ok=True)

def enregistrer_et_rouvrir(racine, contenu, correction):
    dossier=racine/"04-communication"
    dossier.mkdir(parents=True,exist_ok=True)
    cible=dossier/"variantes-communication-projet.md"
    brut=contenu.encode("utf-8")
    archive=None
    with verrou_export(dossier):
        ancien=cible.read_bytes() if cible.exists() else None
        if ancien != brut:
            with tempfile.NamedTemporaryFile(dir=dossier,delete=False) as t:
                tmp=Path(t.name)
                try:
                    t.write(brut); t.flush(); os.fsync(t.fileno())
                except BaseException:
                    t.close(); tmp.unlink(missing_ok=True); raise
            try:
                if ancien is not None:
                    historique=dossier/"historique"
                    historique.mkdir(exist_ok=True)
                    numero=1
                    while True:
                        nom=historique/f"variantes-communication-projet-v{numero:03d}.md"
                        try:
                            with nom.open("xb") as f:
                                try:
                                    f.write(ancien); f.flush(); os.fsync(f.fileno())
                                except BaseException:
                                    f.close(); nom.unlink(missing_ok=True); raise
                            archive=nom
                            break
                        except FileExistsError:
                            numero+=1
                os.replace(tmp,cible)
            finally:
                tmp.unlink(missing_ok=True)
        relu=cible.read_bytes()
        if relu!=brut:
            raise IOError("Le fichier relu diffère du contenu exporté.")
        texte=relu.decode("utf-8").rsplit("\n## Message corrigé\n\n",1)[-1].rsplit("\n\n## Revue du pilote\n",1)[0]
        if texte!=correction["texte"] or correction["apres"] not in texte:
            raise IOError("La correction manque dans la section « Message corrigé » du fichier rouvert.")
    return cible,archive,texte,hashlib.sha256(relu).hexdigest()

if revision is None or essai is None or donnees is None:
    print("EXPORT EN ATTENTE · terminez les cellules 1 à 5. Aucun nouveau Markdown créé.")
elif donnees != essai["initial"] or variantes(donnees) != initiales:
    print("Les entrées ont changé. Relancez les cellules 2 à 5 avant l’export.")
else:
    contenu = composer_trace(essai, revision, appuis, texte_s14, MODE_SOURCE, origine_fiche, regle_s15)
    chemin, archive, relu, empreinte = enregistrer_et_rouvrir(racine, contenu, revision)
    print("Fichier rouvert :", chemin.relative_to(racine))
    if archive:
        print("Version précédente conservée :", archive.relative_to(racine))
    print("Section Message corrigé relue sur disque :\n" + relu)
    print("SHA-256 des octets relus :", empreinte)
    print("Enregistrez ce carnet avec ses sorties. Le message reste non publié.")
