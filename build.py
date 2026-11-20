#!/usr/bin/env python3
"""Lo studio di Alessio Granella — genera index.html dal catalogo qui sotto.

Uso:  python3 build.py
- I percorsi `file` sono relativi alla cartella Operativa: lo script controlla che esistano.
- In locale (apri index.html dal Finder) i link «Apri file» funzionano.
- Online (GitHub Pages) i file locali mostrano solo «Copia percorso».
Per aggiungere un lavoro: una riga nella lista ITEMS. Poi `python3 build.py` e `./deploy.sh`.
"""
import html, json, os, sys, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))  # .../Operativa
GH = "https://alessiogranella.github.io/"
L = "Alessio Granella/Learning e processi/"  # kit The Futur tradotti

# ---------------------------------------------------------------- categorie
CATS = [
    ("brand",     "Brand e design system", "Le regole visive: token, componenti, brandbook."),
    ("aibs",      "AI Brand System",       "Il servizio: landing, whitepaper, pitch, presentazioni."),
    ("vetrina",   "Portfolio e sito",      "Come mi presento: portfolio, sito, landing, CV."),
    ("proposte",  "Proposte e preventivi", "Offerte, preventivi e proposte creative ai clienti."),
    ("pm",        "Learning e processi",   "Il metodo di lavoro: kit The Futur tradotti con PDF e pagine operative."),
    ("business",  "Sviluppo clienti",      "Strategia, outreach e liste prospect."),
    ("web",       "Siti, landing e casi studio", "Pagine pubblicate per i clienti."),
    ("video",     "Video e storyboard",    "Storyboard, processi e strumenti video."),
    ("stampa",    "Stampa ed editoriale",  "Impaginati, company profile, esecutivi."),
    ("strumenti", "Strumenti e template",  "Cose costruite per lavorare più in fretta."),
    ("finanza",   "Amministrazione",       "Numeri della partita IVA."),
]

# ---------------------------------------------------------------- clienti
CLIENTS = [
    # id, nome, rapporto, stato, nota, cartella
    ("orisline",    "Orisline",            "Cliente diretto", "Attivo",     "Gestionali dentali (gruppo HSO). Rebuild sito e brand, 16/11–18/12/2026.", "Alessio Granella/Clienti/05_Clienti attivi/01_Orisline"),
    ("habitanova",  "Habitanova",          "Cliente diretto", "Attivo",     "Immobiliare di Iglesias. Brandbook v1.0 e mockup.", "Alessio Granella/Clienti/05_Clienti attivi/02_Habitanova"),
    ("datafied",    "Datafied",            "Cliente diretto", "Trattativa", "Proposta in preparazione.", "Alessio Granella/Clienti/04_Trattative/Datafied"),
    ("oe",          "OpenEconomics",       "Collaborazione",  "Continuativo", "Design system, casi studio, video, bilancio, strumenti. Anche Civiqa e T33.", "OpenEconomics"),
    ("pa",          "Produttori Arborea",  "Collaborazione",  "Continuativo", "Marchi Primoverde, Rossopregio, Meridoro: DS, sito, schede, video.", "Produttori Arborea"),
    ("drop",        "DROP",                "Agenzia",         "Continuativo", "Design system dell'agenzia e template social.", "Drop"),
    ("aresu",       "Formaggi Aresu",      "Via DROP",        "Attivo",     "Design system, home, moodboard shooting.", "Drop/Progetti/ARESU Formaggi"),
    ("senarrubia",  "Camping S'Ena Arrubia", "Via DROP",      "Attivo",     "Design system, bozza sito v1 e v2, mappa e flyer.", "Drop/Progetti/Camping S'Ena Arrubia"),
    ("vegenia",     "Vegenia",             "Via DROP",        "Attivo",     "Packaging busta 4ª gamma: consegna 3/12/2026.", "Drop/Progetti/Vegenia"),
    ("berau",       "Bespoke Berau",       "Via DROP",        "Brief",      "Sintesi del brief.", "Drop/Progetti/Bespoke Berau"),
    ("murgia",      "Progetto Murgia",     "Via DROP",        "Consegnato", "Strategia di identità e naming.", "Drop/Progetti/Progetto Murgia"),
    ("dap",         "DAP Riabilitazione",  "Via DROP",        "Consegnato", "Logo.", "Drop/Progetti/Logo_DAP_Riabilitazione"),
]

# ---------------------------------------------------------------- lavori
# (categoria, titolo, descrizione, cliente|None, url online|None, file locale|None)
ITEMS = [
    # Brand e design system
    ("brand", "Design system personale", "Token --ag-*, Pantone, componenti. Libreria Vite.", None, None, "Alessio Granella/design-system/index.html"),
    ("brand", "Brandbook Alessio Granella v1.0", "Il brandbook personale in PDF.", None, None, "Alessio Granella/design-system/brandbook/Alessio_Granella_Brandbook_v1.0.pdf"),
    ("brand", "OpenEconomics Design System", "UI kit consultabile: token, componenti, catalogo.", "oe", GH+"openeconomics-design-system/", "OpenEconomics/design-system"),
    ("brand", "DROP design system", "Colori, Sora, rubriche social, template.", "drop", GH+"drop-design-system/", "Drop/design-system"),
    ("brand", "DROP Brand Book v1.0", "Brand book dell'agenzia.", "drop", None, "Drop/DROP · Brand Book v1.0.pdf"),
    ("brand", "Procedura consegna design system DROP", "Come si passa il DS al team.", "drop", None, "Drop/Consegna"),
    ("brand", "Produttori Arborea design system", "4 marchi, 3 temi, token --pa-*.", "pa", GH+"produttori-arborea-design-system/", "Produttori Arborea/design-system"),
    ("brand", "S'Ena Arrubia design system", "DS del campeggio.", "senarrubia", GH+"senarrubia-design-system/", "Drop/Progetti/Camping S'Ena Arrubia/design-system"),
    ("brand", "Aresu design system", "DS e brandbook Formaggi Aresu.", "aresu", None, "Drop/Progetti/ARESU Formaggi/design-system"),
    ("brand", "Brandbook Formaggi Aresu", "PDF del brandbook esistente.", "aresu", None, "Drop/Progetti/ARESU Formaggi/Brandbook Aresu/FormaggiAresuBrandbook.pdf"),
    ("brand", "Habitanova brandbook v1.0", "Brandbook del cliente.", "habitanova", None, "Alessio Granella/Clienti/05_Clienti attivi/02_Habitanova/Brandbook/HabitaNova_Brandbook_v1.0.pdf"),
    ("brand", "Orisline · revisione del marchio", "Presentazione della revisione.", "orisline", GH+"orisline-revisione-marchio/", "Alessio Granella/Clienti/05_Clienti attivi/01_Orisline/01. Brand/Presentazione/index.html"),
    ("brand", "Brand AI System OpenEconomics", "Il sistema brand OE spiegato.", "oe", GH+"Brand-AI-System-OpenEconomics/", None),

    # AI Brand System
    ("aibs", "Sito AI Brand System", "Landing, whitepaper e case study online.", None, "https://aibrandsystem.alessiogranella.com/", "Alessio Granella/AI Brand System/04. Sito-pubblico"),
    ("aibs", "Strategia commerciale", "Come si vende il servizio.", None, None, "Alessio Granella/AI Brand System/00. Strategia commerciale/Strategia-commerciale-AI-Brand-System.pdf"),
    ("aibs", "Whitepaper", "Il documento lungo, in PDF.", None, None, "Alessio Granella/AI Brand System/02. Whitepaper-AI-Brand-System/AI-Brand-System-Whitepaper.pdf"),
    ("aibs", "Case study OpenEconomics", "Il caso studio in PDF.", "oe", None, "Alessio Granella/AI Brand System/03. Brand-AI-System-OpenEconomics/Case-Study-OpenEconomics.pdf"),
    ("aibs", "Pitch", "Pitch breve.", None, None, "Alessio Granella/AI Brand System/05. Pitch/AI-Brand-System-Pitch.pdf"),
    ("aibs", "Presentazione commerciale", "Deck per i clienti diretti.", None, None, "Alessio Granella/AI Brand System/06. Presentazione commerciale/AI-Brand-System-Presentazione-commerciale.pdf"),
    ("aibs", "Presentazione case study", "Il caso OE in slide.", "oe", None, "Alessio Granella/AI Brand System/07. Presentazione case study/Case-Study-OpenEconomics-Presentazione.pdf"),
    ("aibs", "Pitch agenzie", "Versione per le agenzie.", None, None, "Alessio Granella/AI Brand System/08. Pitch agenzie/AI-Brand-System-Pitch-Agenzie.pdf"),
    ("aibs", "Scheda servizio (one page)", "Una pagina che riassume l'offerta.", None, None, "Alessio Granella/AI Brand System/09. One page/AI-Brand-System-Scheda-servizio.pdf"),
    ("aibs", "Presentazione AI Brand System", "Deck completo, anche in versione live.", None, None, "Alessio Granella/AI Brand System/11. Presentazione AI Brand System/AI-Brand-System-Presentazione.pdf"),
    ("aibs", "Post LinkedIn", "Contenuti AI simili tra loro.", None, None, "Alessio Granella/AI Brand System/12. LinkedIn/post-01-contenuti-ai-simili"),

    # Portfolio e sito
    ("vetrina", "Portfolio AI", "Landing dei lavori fatti con l'AI.", None, GH+"portfolio-ia/", "Alessio Granella/Portfolio AI/index.html"),
    ("vetrina", "Redesign del sito", "Home e caso studio MidaTicket.", None, GH+"sito-redesign/", "Alessio Granella/Sito Redesign/index.html"),
    ("vetrina", "Atlante delle inquadrature", "Riferimento visivo per il video.", None, "https://atlante.alessiogranella.com/", None),
    ("vetrina", "Landing Cultura", "Landing per il settore culturale.", None, None, "Alessio Granella/Landing Cultura/index.html"),
    ("vetrina", "Landing Marketing Design", "Landing servizi di marketing design.", None, None, "Alessio Granella/Landing Marketing Design/index.html"),
    ("vetrina", "CV 2026", "Curriculum in PDF.", None, None, "CV/CV_Alessio_Granella_2026.pdf"),
    ("vetrina", "CV in HTML", "Versione web del CV.", None, None, "CV/cv.html"),

    # Proposte e preventivi
    ("proposte", "Template preventivo", "Modello A4 in 2 pagine, brand personale.", None, None, "Alessio Granella/Clienti/03_Materiali/Template_Preventivo/preventivo.html"),
    ("proposte", "Offerta servizi", "Cosa offro, in breve.", None, None, "Alessio Granella/Clienti/03_Materiali/Offerta_Servizi.md"),
    ("proposte", "Proposta tipo", "Struttura della proposta creativa.", None, None, "Alessio Granella/Clienti/03_Materiali/Proposta_Tipo.md"),
    ("proposte", "Struttura case study", "Come scrivere un caso studio.", None, None, "Alessio Granella/Clienti/03_Materiali/Struttura_Case_Study.md"),
    ("proposte", "Preventivo Orisline · brand e sito", "", "orisline", None, "Alessio Granella/Clienti/04_Trattative/Orisline/Preventivo_Orisline_Brand_Sito.pdf"),
    ("proposte", "Preventivo Orisline · completo", "", "orisline", None, "Alessio Granella/Clienti/04_Trattative/Orisline/Preventivo_Orisline_completo.pdf"),
    ("proposte", "Preventivo Orisline · v1", "", "orisline", None, "Alessio Granella/Clienti/04_Trattative/Orisline/Preventivo_Orisline_v1_3000.pdf"),
    ("proposte", "Proposta Datafied", "Materiali e modelli The Perfect Proposal.", "datafied", None, "Alessio Granella/Clienti/04_Trattative/Datafied/Proposta"),
    ("proposte", "Vegenia · strategia di brand e GDO", "Documento di strategia.", "vegenia", None, "Drop/Progetti/Vegenia/Concept packaging busta—(Numero commessa)/00_Documentazione interna/Vegenia - Strategia di brand e go-to-market GDO.pdf"),
    ("proposte", "Vegenia · brief creativo", "", "vegenia", None, "Drop/Progetti/Vegenia/Concept packaging busta—(Numero commessa)/03_Concept/00_Brief creativo/Vegenia - Brief creativo.pdf"),
    ("proposte", "Murgia · strategia di identità", "Tavole di strategia.", "murgia", None, "Drop/Progetti/Progetto Murgia/Strategia di identità.pdf"),
    ("proposte", "Bespoke Berau · sintesi brief", "", "berau", None, "Drop/Progetti/Bespoke Berau/02. Sintesi brief/Kena Muri - Sintesi brief.pdf"),

    # Learning e processi: kit The Futur tradotti (ogni kit: Italiano/ md + PDF, sito/index.html operativo)
    ("pm", "Kit project management", "The Futur tradotto per il team DROP: metodo, modelli, email, checklist.", "drop", GH+"project-management-kit/", L+"Project management/sito/index.html"),
    ("pm", "Il metodo", "", None, None, L+"Project management/Italiano/PDF/01_Il-metodo.pdf"),
    ("pm", "Checklist onboarding", "", None, None, L+"Project management/Italiano/PDF/02_Checklist-onboarding.pdf"),
    ("pm", "Brief creativo · modello", "", None, None, L+"Project management/Italiano/PDF/04_Brief-creativo-modello.pdf"),
    ("pm", "Calendario di produzione", "", None, None, L+"Project management/Italiano/PDF/06_Calendario-produzione.pdf"),
    ("pm", "Presentare il lavoro", "", None, None, L+"Project management/Italiano/PDF/07_Presentare-il-lavoro.pdf"),
    ("pm", "Modulo di approvazione", "", None, None, L+"Project management/Italiano/PDF/10_Modulo-approvazione.pdf"),
    ("pm", "After action review", "", None, None, L+"Project management/Italiano/PDF/12_After-action-review.pdf"),
    ("pm", "Struttura cartelle", "", None, None, L+"Project management/Italiano/PDF/13_Struttura-cartelle.pdf"),
    ("pm", "Kit style guide", "Come si fa, si vende e si consegna una style guide. Copy Arsenal, esempi Pebble e Hamilton.", None, None, L+"Style guide/sito/index.html"),
    ("pm", "Kit Perfect Proposal", "Proposte commerciali: guida, modelli completo e di una pagina, Copy Arsenal, esempi.", None, None, L+"Perfect_Proposal/sito/index.html"),
    ("pm", "Kit The Pitch Kit", "Gare e pitch: brief, scaletta del deck, 17 treatment reali tradotti.", None, None, L+"The Pitch Kit/sito/index.html"),
    ("pm", "Kit Core Discovery", "Sessione di discovery con il cliente in 9 moduli, fino al brief.", None, None, L+"Core Discovery/sito/index.html"),
    ("pm", "Kit Brand Messaging", "Workshop di messaging: workbook, scaletta, piattaforma dei messaggi.", None, None, L+"Brand Messaging/sito/index.html"),
    ("pm", "Kit Stylescapes", "Direzioni visive prima del logo: lezione, worksheet, esempi.", None, None, L+"Stylescapes/sito/index.html"),
    ("pm", "Kit Complete Case Study", "Scrivere e impaginare casi studio: guida, worksheet, deck Blind.", None, None, L+"Complete Case Study/sito/index.html"),
    ("pm", "Kit First Meeting Workbook", "Il primo incontro con il cliente, compilabile ed esportabile per Notion.", None, None, L+"First Meeting Workbook/sito/index.html"),
    ("pm", "Kit Colore", "Color For Creatives: glossario, risorse, verifica del valore, palette.", None, None, L+"Colore/sito/index.html"),
    ("pm", "Kit Illustrazione per designer", "Principi, stilizzazione, linguaggio visivo, presentazione.", None, None, L+"Illustrationn for Designers/sito/index.html"),
    ("pm", "Originali The Futur (EN)", "Tutti i kit originali in inglese.", None, None, L.rstrip('/')),
    ("pm", "Checklist nuova analisi OE", "", "oe", None, "OpenEconomics/Checklist nuova analisi/Checklist nuova analisi OE.pdf"),
    ("pm", "Marketing task board", "Bacheca attività marketing OE.", "oe", GH+"marketing-task-board/", None),

    # Sviluppo clienti
    ("business", "Guida al sistema clienti", "Come funziona la pipeline.", None, None, "Alessio Granella/Clienti/00_Guida_Sistema.md"),
    ("business", "Cliente ideale e target", "", None, None, "Alessio Granella/Clienti/01_Strategia/Cliente_Ideale_e_Target.md"),
    ("business", "Piano di comunicazione 90 giorni", "", None, None, "Alessio Granella/Clienti/01_Strategia/Piano_Comunicazione_90gg.md"),
    ("business", "Messaggio per canale", "", None, None, "Alessio Granella/Clienti/01_Strategia/Messaggio_per_Canale.md"),
    ("business", "Messaggi LinkedIn", "", None, None, "Alessio Granella/Clienti/02_Outreach/Messaggi_LinkedIn.md"),
    ("business", "Networking locale", "", None, None, "Alessio Granella/Clienti/02_Outreach/Networking_Locale.md"),
    ("business", "Referral e partner", "", None, None, "Alessio Granella/Clienti/02_Outreach/Referral_e_Partner.md"),
    ("business", "Prospect cultura Sardegna", "Musei, associazioni, calendario, fornitori.", None, None, "Alessio Granella/Clienti/Prospect_Cultura_Sardegna.html"),
    ("business", "Prospect aziende Sardegna", "258 aziende per provincia e settore.", None, None, "Alessio Granella/Clienti/Prospect_Aziende_Sardegna.html"),

    # Siti, landing e casi studio
    ("web", "Studies OpenEconomics · home", "Rifacimento della home studies.", "oe", GH+"oe-studies/", "OpenEconomics/progetti/Studies"),
    ("web", "Caso studio RFI 2025", "Investimenti RFI.", "oe", GH+"oe-caso-studio-rfi-2025/", "OpenEconomics/progetti/Caso studio - Analisi - RFI 2025"),
    ("web", "Caso studio Audiovisivo", "Impatto dell'audiovisivo italiano (APA).", "oe", GH+"oe-caso-studio-audiovisivo/", None),
    ("web", "Eni · impatto del procurato", "", "oe", GH+"eni-analisi/", "OpenEconomics/progetti/Eni Analisi v2"),
    ("web", "Minisito Difesa e Aerospazio", "", "oe", GH+"minisito-difesa-aerospazio/", "OpenEconomics/progetti/Minisito Difesa Aerospazio"),
    ("web", "Dashboard LinkedIn OE", "", "oe", GH+"dashboard-linkedin-openeconomics/", None),
    ("web", "Infografiche FITP e FIP Padel", "Impatto sociale e SROI.", "oe", None, "OpenEconomics/progetti/Infografiche FITP Industria"),
    ("web", "Pagine prodotto Primoverde e Meridoro", "Con il widget «Trova il punto vendita».", "pa", GH+"produttori-arborea-pagine-prodotto/", "Produttori Arborea/sito"),
    ("web", "S'Ena Arrubia · bozza sito", "v1 e v2 (/v2).", "senarrubia", GH+"senarrubia-sito-bozza/", "Drop/Progetti/Camping S'Ena Arrubia/Sito"),
    ("web", "Aresu · bozza home", "", "aresu", GH+"aresu-home-bozza/", None),
    ("web", "Aresu · moodboard shooting", "", "aresu", GH+"aresu-moodboard/", "Drop/Progetti/ARESU Formaggi/Moodboard shooting"),
    ("web", "Habitanova · mockup sito", "", "habitanova", None, "Alessio Granella/Clienti/05_Clienti attivi/02_Habitanova/Mockup/sito/home.html"),

    # Video e storyboard
    ("video", "Storyboard evento Rieti", "Video unico, luoghi animati.", "oe", GH+"oe-storyboard-rieti-evento/", "OpenEconomics/progetti/Video evento Rieti"),
    ("video", "Storyboard video Rieti", "", "oe", GH+"oe-storyboard-rieti/", "OpenEconomics/progetti/Video Rieti"),
    ("video", "Storyboard Viterbo · parti 1-3", "", "oe", GH+"oe-storyboard-viterbo/", "OpenEconomics/progetti/Viterbo Evento"),
    ("video", "Storyboard video APA", "17,5 s verticale.", "oe", GH+"oe-storyboard-apa/", "OpenEconomics/progetti/Video APA"),
    ("video", "Storyboard Audiovisivo", "", "oe", GH+"oe-storyboard-audiovisivo/", "OpenEconomics/progetti/Video Audiovisivo"),
    ("video", "Processo creativo video OE", "Come nasce un video OE.", "oe", GH+"oe-processo-video/", "OpenEconomics/Consegne/Processo creativo video"),
    ("video", "Storyboard video bambini", "10 scene, 21 novembre.", "pa", GH+"pa-storyboard-video-bambini/", "Produttori Arborea/Video_Azienda/Video Bambini 21 novembre"),
    ("video", "Storyboard punti vendita Meridoro", "8 scene con la mappa della Sardegna.", "pa", GH+"meridoro-storyboard-punti-vendita/", "Produttori Arborea/Meridoro/Video Punti Vendita"),

    # Stampa ed editoriale
    ("stampa", "Bilancio di sostenibilità OE 2025", "Versione digitale.", "oe", None, "OpenEconomics/progetti/Bilancio di Sostenibilità/01. Impaginato/BdS2025_OpenEconomics_digitale.pdf"),
    ("stampa", "Company profile 2026", "IT, EN, FR.", "pa", None, "Produttori Arborea/Company Profile/PRODUTTORIARBOREA_company profile 2026.pdf"),
    ("stampa", "Banner marchi 3×2", "", "pa", None, "Produttori Arborea/Banner Marchi 3x2"),
    ("stampa", "Banner azienda socia Meridoro", "", "pa", None, "Produttori Arborea/Meridoro/Banner Azienda Socia"),
    ("stampa", "Schede prodotto A5", "Master su Canva, una cartella per linea.", "pa", None, "Produttori Arborea/Schede prodotto A5"),
    ("stampa", "Stand fiera", "", "pa", None, "Produttori Arborea/Asset/FIERA"),
    ("stampa", "S'Ena Arrubia · mappa A3", "Esecutivo di stampa.", "senarrubia", None, "Drop/Progetti/Camping S'Ena Arrubia/S'EA_Mappa A3/S'EA_Mappa_A3_Esecutivo di Stampa.pdf"),
    ("stampa", "S'Ena Arrubia · flyer", "Esecutivo.", "senarrubia", None, "Drop/Progetti/Camping S'Ena Arrubia/Flyer/S'EA_Flyer_22-05-25_Esecutivo.pdf"),
    ("stampa", "DAP Riabilitazione · logo", "", "dap", None, "Drop/Progetti/Logo_DAP_Riabilitazione/DAP_Riabilitazione_logo_BN_v2.pdf"),
    ("stampa", "Linee guida caroselli DROP", "", "drop", None, "Drop/Templates/Social Templates"),

    # Strumenti e template
    ("strumenti", "OpenEconomics Layout Designer", "Dal Word al documento impaginato.", "oe", GH+"impaginatore-oe-prova/", "OpenEconomics/strumenti/impaginatore-prova"),
    ("strumenti", "Check DS", "Controllo automatico delle pagine OE.", "oe", None, "OpenEconomics/strumenti/check-ds"),
    ("strumenti", "Template caso studio OE", "10 fasce, hero normata.", "oe", None, "OpenEconomics/progetti/_template-caso-studio"),
    ("strumenti", "Template infografica KPI animata", "Si riempie contenuti/it|en.js, esce MP4.", "oe", None, "OpenEconomics/progetti/_template-infografica-kpi"),
    ("strumenti", "Template immagine blog OE", "Cover 1920×1080.", "oe", None, "OpenEconomics/progetti/_template-immagine-blog"),
    ("strumenti", "Guida colleghi · asset web OE", "Consegna del 28/10.", "oe", None, "OpenEconomics/Consegne/Consegna_colleghi_20261028"),

    # Amministrazione
    ("finanza", "Dashboard finanziaria", "Vista sul registro movimenti.", None, None, "Alessio Granella/Finanza/Dashboard_Finanziaria.html"),
    ("finanza", "Registro movimenti", "I dati della P.IVA.", None, None, "Alessio Granella/Finanza/Registro_Movimenti.xlsx"),
    ("finanza", "Budget mensile", "", None, None, "Alessio Granella/Finanza/budget_mensile.xlsx"),
]

# ---------------------------------------------------------------- agenti
AGENTS = [
    # nome, ruolo, quando, stato, cosa fa, dove guardare
    ("Luca", "Assistente Gmail", "Ogni mattina alle 8 (9 con l'ora legale)", "Attivo",
     "Legge la posta: mette l'etichetta «Da fatturare» alle mail con fatture e «Newsletter» alle newsletter.",
     ("Gmail · etichette", "https://mail.google.com/mail/u/0/#label/Da+fatturare"),
     "https://claude.ai/code/routines/trig_01KjyYCQDotjzAjN1yxN6DTY"),
    ("Emanuele", "Cercatore di bandi", "Ogni giorno alle 19:00", "Attivo",
     "Cerca bandi e annunci freelance da remoto per brand identity, logo, sito e packaging. Priorità a comuni e musei, tutta Italia.",
     ("Notion · Bandi & Opportunità", "https://app.notion.com/p/c549c67a969640fba0b75ca08536536a"),
     "https://claude.ai/code/routines/trig_01UtL7hmRquMbHDLALtz8uVR"),
    ("Riordino Download", "Ordina la cartella Download", "Ogni giorno alle 19:00", "In pausa",
     "Sposta i file sciolti della cartella Download nelle sottocartelle giuste.",
     None, "https://claude.ai/code/routines/trig_01XYvJDdJnoh7nvsTpGkYiJo"),
]
SKILLS = [
    ("schede-prodotto-a5", "Schede prodotto A5 di Produttori Arborea su Canva, dal master Meridoro, con verifica degli ingombri."),
    ("oe-frontend-brand", "Pagine e asset web con il design system OpenEconomics: prima domanda «che cosa devi fare?»."),
    ("Scrittura italiana", "anti-ai-writing, dumbify, storytelling, viral-hooks: filtri per testi social e newsletter."),
]

# ---------------------------------------------------------------- build
# Anteprime: niente immagini per le categorie con dati riservati (prezzi, conti, contatti).
NO_THUMB = {"proposte", "finanza", "business"}
HERE = os.path.dirname(os.path.abspath(__file__))
THUMBS = os.path.join(HERE, "thumbs")

def kind_of(path, url):
    if path:
        ext = os.path.splitext(path)[1].lower()
        return {".pdf": "PDF", ".html": "Pagina", ".xlsx": "Excel", ".md": "Testo",
                ".pptx": "PowerPoint", ".docx": "Word"}.get(ext, "Cartella" if os.path.isdir(os.path.join(ROOT, path)) else "File")
    return "Online"

def slug(s):
    import re, unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]

def mtime(path):
    full = os.path.join(ROOT, path)
    if os.path.isfile(full):
        return os.path.getmtime(full)
    newest = 0
    for dp, dn, fn in os.walk(full):
        dn[:] = [d for d in dn if d not in ("node_modules", ".git", "dist")]
        for f in fn:
            if not f.startswith("."):
                try: newest = max(newest, os.path.getmtime(os.path.join(dp, f)))
                except OSError: pass
    return newest

# Anteprime da una sorgente diversa dal file del lavoro (es. la build dist di un'app Vite)
THUMB_FROM = {
    "brand-design-system-personale": "Alessio Granella/design-system/dist/index.html",
    "brand-aresu-design-system": "Drop/Progetti/ARESU Formaggi/design-system/dist/index.html",
}

def thumb_source(it):
    """Cosa fotografare: url online, pagina html, pdf, o il primo html/pdf di una cartella."""
    if it["id"] in THUMB_FROM:
        return ("web", "http://127.0.0.1:8765/" + "/".join(__import__("urllib.parse").parse.quote(x) for x in THUMB_FROM[it["id"]].split("/")))
    if it["u"]:
        return ("web", it["u"])
    p = it["p"]
    full = os.path.join(ROOT, p)
    if os.path.isdir(full):
        cands = []
        for dp, dn, fn in os.walk(full):
            dn[:] = sorted(d for d in dn if d not in ("node_modules", ".git", "dist", "assets", "Old", "src"))
            if dp.count(os.sep) - full.count(os.sep) > 2: continue
            for f in sorted(fn):
                if f.lower().endswith((".pdf", ".html")) and not f.startswith("."):
                    cands.append(os.path.join(dp, f))
        cands.sort(key=lambda x: (0 if x.endswith("index.html") else 1 if x.endswith(".html") else 2, x.count(os.sep)))
        if not cands: return None
        full = cands[0]
    if full.lower().endswith(".pdf"): return ("pdf", full)
    if full.lower().endswith(".html"): return ("web", "file://" + full)
    return None

def make_thumbs(items, force=False):
    import subprocess, tempfile
    os.makedirs(THUMBS, exist_ok=True)
    tmp = tempfile.mkdtemp()
    web = []
    for it in items:
        if it["c"] in NO_THUMB: continue
        out = os.path.join(THUMBS, it["id"] + ".webp")
        if os.path.exists(out) and not force: continue
        src = thumb_source(it)
        if not src: continue
        png = os.path.join(tmp, it["id"] + ".png")
        if src[0] == "pdf":
            subprocess.run(["pdftoppm", "-f", "1", "-l", "1", "-singlefile", "-scale-to", "900", "-png", src[1], png[:-4]], capture_output=True)
        else:
            web.append({"id": it["id"], "src": src[1], "png": png})
    if web:
        srv = subprocess.Popen([sys.executable, "-m", "http.server", "8765", "--bind", "127.0.0.1"], cwd=ROOT,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        __import__("time").sleep(1)
        jobs = os.path.join(tmp, "jobs.json"); json.dump(web, open(jobs, "w"))
        subprocess.run(["node", os.path.join(HERE, "tools", "shot.mjs"), jobs], cwd=os.path.join(HERE, "tools"))
        srv.terminate()
    from PIL import Image, ImageStat
    for f in os.listdir(tmp):
        if not f.endswith(".png"): continue
        src = os.path.join(tmp, f)
        if ImageStat.Stat(Image.open(src).convert("L")).stddev[0] < 3:
            print("anteprima vuota, scartata:", f[:-4]); continue
        subprocess.run(["cwebp", "-quiet", "-q", "72", "-resize", "640", "0", src, "-o", os.path.join(THUMBS, f[:-4] + ".webp")])

missing, items, seen = [], [], set()
for cat, title, desc, client, url, path in ITEMS:
    if path and not os.path.exists(os.path.join(ROOT, path)):
        missing.append(path)
    iid = slug(cat + "-" + title)
    assert iid not in seen, iid; seen.add(iid)
    items.append({"id": iid, "c": cat, "t": title, "d": desc, "k": client, "u": url, "p": path,
                  "y": kind_of(path, url), "m": int(mtime(path)) if path else 0})
if missing:
    print("Percorsi mancanti:\n  " + "\n  ".join(missing)); sys.exit(1)

if "--thumbs" in sys.argv or "--force-thumbs" in sys.argv:
    make_thumbs(items, force="--force-thumbs" in sys.argv)
from PIL import Image
for it in items:
    f = os.path.join(THUMBS, it["id"] + ".webp")
    it["i"] = os.path.exists(f) and it["c"] not in NO_THUMB
    if it["i"]:
        w, h = Image.open(f).size
        it["v"] = h > w * 0.75   # pagina verticale (PDF A4): si mostra intera

clients = [{"id": i, "n": n, "r": r, "s": s, "d": d, "p": p} for i, n, r, s, d, p in CLIENTS]
for c in clients:
    c["count"] = sum(1 for it in items if it["k"] == c["id"])
cats = [{"id": i, "n": n, "d": d, "count": sum(1 for it in items if it["c"] == i)} for i, n, d in CATS]
agents = [{"n": n, "r": r, "w": w, "s": s, "d": d, "o": o, "u": u} for n, r, w, s, d, o, u in AGENTS]
skills = [{"n": n, "d": d} for n, d in SKILLS]

data = json.dumps({"items": items, "clients": clients, "cats": cats, "agents": agents, "skills": skills,
                   "online": sum(1 for it in items if it["u"])}, ensure_ascii=False)
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
out = tpl.replace("/*__DATA__*/null", data).replace("__DATE__", datetime.date.today().strftime("%d/%m/%Y"))
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(out)
print(f"OK: {len(items)} lavori ({sum(it['i'] for it in items)} con anteprima), {len(clients)} clienti, {len(agents)} agenti → index.html")
