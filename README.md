# IT Adventures – Nerdstown Chronicles

**Un’avventura testuale comica e tecnica in puro stile open source**

Vestirai i panni di Luca, un informatico smaliziato, e girerai per Nerdstown tra casa, ufficio, caffè e data center. Risolverai quiz Linux, riparerai hardware, assisterai clienti e guadagnerai XP, crediti e reputazione open-source.

---

## 📁 Struttura del progetto

```
it-adventures/
├── data/                # Contenuti di gioco (modificabili)
│   ├── world.json       # Stanze, descrizioni, uscite, eventi
│   ├── missions.json    # Elenco missioni (quiz, fetch, event)
│   ├── items.json       # Oggetti, descrizioni, contesti d’uso
│   └── npcs.json        # NPC, dialoghi, side-quests
│
├── save.json            # Salvataggio automatico
│
├── src/                 
│   ├── data.py          # Caricamento/salvataggio dati, stato di gioco
│   ├── ui.py            # Rendering a colori con Rich (HUD, stanze, tabelle)
│   ├── engine.py        # Menu iniziale e loop principale
│   ├── quests.py        # Logica di missioni (quiz, fetch, eventi)
│   └── npcs.py          # Dialoghi NPC e interazioni
│
├── requirements.txt     # `rich`  
├── Dockerfile           # Container minimal  
├── .gitignore           
└── README.md            # Questo file  
```

---

## 🚀 Installazione e avvio

1. **Clona il repository**  
   ```bash
   git clone https://tuo-repo/it-adventures.git
   cd it-adventures
   ```

2. **Crea un ambiente virtuale (opzionale ma consigliato)**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installa le dipendenze**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Avvia il gioco**  
   ```bash
   python3 src/engine.py
   ```

5. **In Docker**  
   ```bash
   docker build -t it-adventures .
   docker run -it it-adventures
   ```

---

## 🎮 Comandi principali

### Menu iniziale  
- `1` Nuova partita  
- `2` Carica partita  
- `3` Salva partita  
- `4` Aiuto  
- `5` Esci  

### In gioco  
- `vai <direzione>` (es. `vai nord`)  
- `prendi <oggetto>` (es. `prendi kit_saldatura`)  
- `usa <oggetto>` (se supportato)  
- `inventario` / `inv`  
- `missioni`  
- `inizia <id>` (avvia missione)  
- `parla <npc_id>` (dialoga con NPC)  
- `stato` (mostra HUD)  
- `guarda`  
- `salva`  
- `esci` (torna al menu o esci)

---

## 🌟 Caratteristiche chiave

- **Comico & Tecnico**: battute su Linux, sysadmin, open-source, “sudo”, “root”, “bug”, “RAM-RGB”  
- **Missioni ramificate**: quiz Linux, fetch item, puzzle sysadmin  
- **Side-Quests con NPC**: dialoghi umoristici, reputazione, badge  
- **HUD dinamico**: livelli, XP, crediti, OSS, reputazione sempre visibili  
- **Modulare**: aggiungi stanze, missioni, NPC o oggetti editando i JSON in `data/`  

---

## 🔧 Come estendere

- **Aggiungi nuove stanze**  
  Modifica `data/world.json` con oggetti, uscite, eventi.

- **Crea missioni**  
  Amplia `data/missions.json`: supporta tipi `quiz`, `fetch`, `event`.

- **Nuovi NPC**  
  Definisci dialoghi e side-quests in `data/npcs.json`.

- **Personalizza HUD**  
  Aggiorna `src/ui.py` per colori, layout e ascii art.

---

## 📜 Licenza

Distribuito sotto **GNU GPL v3**. Vedi `LICENSE` per dettagli.

---

Grazie per aver scelto IT Adventures! Preparati a ridere, imparare e celebrare il potere dell’open source in un’avventura testuale senza eguali. Buon divertimento!
