# Lo studio di Alessio Granella

Studio virtuale: tutti i lavori per categoria, i clienti e gli agenti.

- Online: https://alessiogranella.github.io/studio/ (noindex)
- In locale: apri `index.html` dal Finder, così i file sul Mac si aprono direttamente.

Aggiungere un lavoro: una riga in `ITEMS` dentro `build.py`, poi `./deploy.sh` (genera anche le anteprime mancanti in `thumbs/`).

Prima volta su un Mac nuovo: `cd tools && npm i` (serve per le anteprime, usa Chrome). Per rifare tutte le anteprime: `python3 build.py --force-thumbs`.
Le categorie Proposte, Amministrazione e Sviluppo clienti non hanno anteprime di proposito: contengono prezzi e dati riservati.
