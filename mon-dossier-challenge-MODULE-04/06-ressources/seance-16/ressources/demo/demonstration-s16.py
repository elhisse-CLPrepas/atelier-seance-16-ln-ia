"""Démonstration fictive S16 · script Python autonome, sans dépendance externe.

Lancez python demonstration-s16.py depuis un répertoire de votre choix.
Les sorties vont dans dossier-demo-s16/04-communication. Cette exécution
du terminal est un exemple formateur, distinct du notebook d’un candidat.
"""
from pathlib import Path


def main():
    # 1. Réglez ces trois lignes si vous utilisez vos propres pièces.
    MODE_SOURCE = "exemple"         # ou "fichier" pour le véritable export S15
    RACINE_CANDIDAT = "dossier-demo-s16"            # vide si Jupyter est ouvert dans le kit
    TEXTE_HUMAIN_S14 = ""           # facultatif si le fichier S14 contient la rubrique attendue
    donnees = appuis = source_initiale = initiales = essai = revision = None

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


    racine = dossier_de_travail(RACINE_CANDIDAT)
    print("Dossier de travail :", racine)
    origine_fiche = "Cas fictif du formateur, à distinguer de la preuve du candidat."
    if MODE_SOURCE == "exemple":
        # Données embarquées : un JSON produit avec la fonction d’export de S15.
        fiche = {'schema': 'ln-ia-preparation-s16/v1',
         'seance': 'S15 · 13 novembre 2026',
         'statut': 'BROUILLON — À RELIRE',
         'champs': [{'champ': 'projet',
                     'valeur': 'Révision du guide S12',
                     'source_ou_justification': 'Guide S12, titre et étape 5. Titre court choisi pour le '
                                                'courriel.'},
                    {'champ': 'public',
                     'valeur': 'Formateurs débutants',
                     'source_ou_justification': 'Cas fictif S13/S14, public retenu par le formateur.'},
                    {'champ': 'besoin',
                     'valeur': 'comprendre une correction',
                     'source_ou_justification': 'Objectif de la trace fictive S13 et journal V1/V2.'},
                    {'champ': 'proposition',
                     'valeur': 'Le journal documente les modifications et leurs motifs.',
                     'source_ou_justification': 'Journal des corrections V1/V2, lignes de fond et de '
                                                'forme.'},
                    {'champ': 'action',
                     'valeur': 'Souhaitez-vous voir un extrait du journal de corrections ?',
                     'source_ou_justification': 'Trace S14, version humaine et variante professionnelle.'},
                    {'champ': 'format',
                     'valeur': 'professionnel',
                     'source_ou_justification': 'Courriel retenu dans le cas fictif S14.'}],
         'regle_decrite_par_le_candidat': 'Si un texte renseigné dépasse 400 caractères, le signaler.',
         'regle_etalon': {'precondition': 'texte renseigné',
                          'test': 'longueur > 400',
                          'si_vrai': 'À raccourcir',
                          'sinon': 'Longueur acceptable'},
         'moteur_observe': 'JavaScript local du navigateur',
         'essais': [{'longueur': 400,
                     'prediction': 'Longueur acceptable',
                     'observation': 'Longueur acceptable'},
                    {'longueur': 401, 'prediction': 'À raccourcir', 'observation': 'À raccourcir'}],
         'limite': 'La longueur ne vérifie pas les faits.',
         'decision_du_pilote': None}
        texte_s14 = 'J’ai gardé les deux versions du guide. Le journal dit ce que j’ai changé et pourquoi. Souhaitez-vous voir un extrait du journal de corrections ?'
    elif MODE_SOURCE == "fichier":
        chemin = racine / "04-communication" / "donnees-pour-s16.json"
        if not chemin.is_file():
            raise FileNotFoundError("Placez donnees-pour-s16.json dans 04-communication ou choisissez le cas fictif.")
        fiche = json.loads(chemin.read_text(encoding="utf-8-sig"))
        origine_fiche = "04-communication/donnees-pour-s16.json"
        nom_s14 = chemin.with_name("message-court-projet.md")
        texte_s14 = extraire_version_humaine(nom_s14.read_text(encoding="utf-8-sig")) if nom_s14.is_file() else ""
    else:
        raise ValueError("MODE_SOURCE doit être exemple ou fichier.")
    if TEXTE_HUMAIN_S14.strip():
        texte_s14 = TEXTE_HUMAIN_S14.strip()
    donnees, appuis = lire_fiche(fiche)
    regle_s15 = fiche.get("regle_decrite_par_le_candidat") or fiche.get("regle") or "Non renseignée dans la fiche."
    for champ in CHAMPS:
        print(f"{champ} : {donnees[champ]} | Appui : {appuis[champ]}")
    print("Règle rapportée de S15 :", regle_s15)

    # 2. Comparez le gabarit à votre version humaine.
    source_initiale = initiales = essai = revision = None
    def message_source(d):
        return f"{d['projet']} — {d['proposition']} {d['action']}"


    if donnees is None or not renseigne(texte_s14):
        print("À COMPLÉTER · vérifiez la cellule 1 et votre version humaine S14.")
    else:
        source_initiale = message_source(donnees)
        print("VERSION HUMAINE S14\n" + texte_s14)
        print("\nGABARIT S16 · BROUILLON — À RELIRE\n" + source_initiale)

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

    # 4. Avant de lancer : écrivez la prédiction, la valeur modifiée et sa source.
    CHAMP = "public"
    NOUVELLE = "Formateurs débutants en binôme"
    ORIGINE = "Choix pédagogique du formateur pour la relecture en binôme du 16 novembre."
    PREDICTION = "Seul le format professionnel nomme le public. Les deux autres textes devraient rester identiques."
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

    # 5. Choisissez le format et complétez la correction avec vos mots.
    CHOIX = "professionnel"
    AVANT = "Le journal documente les modifications et leurs motifs."
    APRES = "Le journal explique ce qui a changé et pourquoi."
    MOTIF = "Pour des formateurs débutants, « ce qui a changé et pourquoi » rend le rôle du journal plus facile à comprendre."
    APPUI = "Journal S12 V1/V2, correction « Forme — accessibilité » et colonne « Raison et contrôle à réaliser »."
    CANAL = "Courriel au groupe de formation."
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
        bloc += ["", "## Message humain S14", version_s14, "", "## Message source avant la modification", message_source(essai["initial"]),
                 "", "## Message source après la modification", message_source(d), "", "## Ma prédiction et le résultat",
                 f"Champ : {essai['champ']}", "Avant : "+essai["initial"][essai["champ"]], "Après : "+d[essai["champ"]],
                 "Justification : "+essai["origine"], "Prédiction : "+essai["prediction"],
                 "Formats modifiés : "+(", ".join(essai["modifies"]) or "aucun"),
                 "Règle indiquée en S15 : "+regle_s15, "Règle exécutée : texte renseigné, seuil de 400 caractères et une occurrence exacte de l’action."]
        for cle in FORMATS:
            m=essai["controles"][cle]
            bloc += ["", "## Brouillon "+cle, "Avant le changement du champ :", essai["avant"][cle],
                     "", "Après le changement du champ :", essai["versions"][cle],
                     f"Mesure : {m['longueur']} caractères · {m['signal']} · action exacte : {m['action_exacte']}."]
        bloc += ["","## Ma correction humaine", "Choix : "+correction["choix"], "Canal : "+correction["canal"],
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
        print("Enregistrez 05-automatisation/communication-assistee.ipynb avec ses sorties.")

if __name__ == "__main__":
    main()
