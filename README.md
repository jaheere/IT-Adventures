# IT Adventures – Nerdstown Chronicles  
#### Author: Luca Bocaletto  
#### OS: Linux  

**A comedic, tech-heavy text adventure in pure open-source style**  

You step into the shoes of Luca, a savvy sysadmin roaming Nerdstown’s neon streets—from your hacker den to the open-space office, the Bean Overclock Café, and the humming data center. Along the way you’ll tackle Linux quizzes, repair broken hardware, assist quirky clients, and earn XP, credits and open-source reputation.

<p align="center">
  <a href="./index.html">
    <img src="https://img.shields.io/badge/View–English%20Site–index.html-blue?style=for-the-badge" alt="English Version" />
  </a>
  <a href="./index-ita.html">
    <img src="https://img.shields.io/badge/Visualizza–Versione%20Italiana–index-ita.html-blue?style=for-the-badge" alt="Versione Italiana" />
  </a>
</p>

---

## 📁 Project Structure

```
it-adventures/
├── data/                # Game content (editable)
│   ├── world.json       # Rooms, descriptions, exits, events
│   ├── missions.json    # Missions list (quiz, fetch, event)
│   ├── items.json       # Items, descriptions, usable contexts
│   └── npcs.json        # NPCs, dialogues, side-quests
│
├── save.json            # Auto-save state
│
├── src/                 
│   ├── data.py          # Load/save data, game state
│   ├── ui.py            # Colorful rendering with Rich (HUD, rooms, tables)
│   ├── engine.py        # Main menu and game loop
│   ├── quests.py        # Mission logic (quiz, fetch, events)
│   └── npcs.py          # NPC dialogues and interactions
│
├── requirements.txt     # Dependencies (rich)  
├── Dockerfile           # Minimal container  
├── .gitignore           
└── README.md            # This file  
```

---

## 🚀 Installation & Launch

1. **Clone the repository**  
   ```bash
   git clone https://github.com/bocaletto-luca/IT-Adventures.git
   cd IT-Adventures
   ```

2. **Create a virtual environment (recommended)**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the game**  
   ```bash
   python3 src/engine.py
   ```

5. **Using Docker**  
   ```bash
   docker build -t it-adventures .
   docker run -it it-adventures
   ```

---

## 🎮 Main Commands

### Main Menu  
- `1` New Game  
- `2` Load Game  
- `3` Save Game  
- `4` Help  
- `5` Exit  

### In-Game  
- `go <direction>` (e.g. `go north`)  
- `take <item>` (e.g. `take kit_soldering`)  
- `use <item>` (when supported)  
- `inventory` / `inv`  
- `missions`  
- `start <id>` (start a mission)  
- `talk <npc_id>` (interact with NPC)  
- `status` (show HUD)  
- `look`  
- `save`  
- `exit` (return to menu or quit)

---

## 🌟 Key Features

- **Comic & Technical**: witty lines about Linux, sysadmin life, open-source culture, “sudo”, “root”, “bugs”, “RGB RAM.”  
- **Branching Missions**: Linux quizzes, fetch quests, sysadmin puzzles.  
- **NPC Side-Quests**: humorous dialogues, reputation gains, collectible badges.  
- **Dynamic HUD**: levels, XP, credits, OSS tokens and reputation always visible.  
- **Modular Design**: add rooms, missions, NPCs or items simply by editing the JSON files in `data/`.

---

## 🔧 How to Extend

- **Add New Rooms**  
  Edit `data/world.json` to define titles, descriptions, exits, items and optional events.

- **Create Missions**  
  Expand `data/missions.json` with types `quiz`, `fetch` or `event`, specifying prompts, options and rewards.

- **Define NPCs**  
  Add dialogues and side-quests in `data/npcs.json`, complete with intros, dialogue trees and rewards.

- **Customize the HUD**  
  Tweak `src/ui.py` to change colors, layout or ASCII art.

---

## 📜 License

Distributed under **GNU GPL v3**. See `LICENSE` for details.

---

Thank you for choosing **IT Adventures**! Get ready to laugh, learn, and celebrate the power of open source in an unparalleled text-based journey. Have fun!  

---
