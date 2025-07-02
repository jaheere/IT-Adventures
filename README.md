# IT Adventures – Nerdstown Chronicles
#### Author: Bocaletto Luca
#### OS: Linux

Un’avventura testuale comica e tecnica in puro stile open source

In IT Adventures vestirai i panni di Luca, un informatico smaliziato con la passione per il kernel e il sarcasmo da riga di comando. La tua missione è esplorare Nerdstown, una metropoli al neon dove i cavi Ethernet crescono come liane in una giungla cyberpunk: dal caos ordinato della tua “Casa di Luca” – un covo pieno di monitor impilati, sticker Linux e un gatto programmatore –, all’ordine maniacale di TechCorp, fino ai rifugi calorosi del Bean Overclock Café e ai meandri meccanici del Data Center.

Mentre ti muovi tra stanze disegnate con l’ironia degli admin nottambuli, affronterai quiz studiati per mettere alla prova la tua conoscenza di comandi Linux, protocolli di rete e best practice open source. Ogni risposta esatta ti premia con XP e aumenta la tua reputazione nella comunità, sbloccando accessi “sudo” a aree riservate e rivelando scorci nascosti del mondo. Ma non è solo teoria: dovrai riparare hardware guasto, utilizzare kit di saldatura, consegnare oggetti chiave e persino contrattare con NPC dalle personalità stravaganti, dai venditori di RAM RGB ai guru del ping perfetto.

Tra un “kernel panic” e una battuta sul multitasking a 16 thread, guadagnerai crediti da spendere in potenziamenti – power bank, stick di RAM, microcontrollori Raspberry Pi – e in token open source che testimoniano il tuo impegno per la condivisione del sapere. Il gioco ti coinvolge con eventi imprevedibili (blackout, attacchi DDoS, quiz retrò) e side-quest che premiano l’esplorazione più curiosa. Preparati a un’esperienza che unisce la sfida tecnica di un lab di sysadmin con l’umorismo nerd più spinto: benvenuto in IT Adventures, dove l’open source è l’unica regola.

<p align="center">
  <a href="./index.html">
    <img src="https://img.shields.io/badge/View–English%20Site–index.html-blue?style=for-the-badge" alt="English Version" />
  </a>
  <a href="./index-ita.html">
    <img src="https://img.shields.io/badge/Visualizza–Versione%20Italiana–index-ita.html-blue?style=for-the-badge" alt="Versione Italiana" />
  </a>
</p>

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
   git clone https://github.com/bocaletto-luca/IT-Adventures.git
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
