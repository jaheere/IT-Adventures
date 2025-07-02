# IT Adventures – Nerdstown Chronicles  
#### Author: Luca Bocaletto  
#### OS: Linux  

**A comedic, tech-heavy text adventure in pure open-source style**

In **IT Adventures**, you slip into the well-worn hoodie of Luca, a quick-witted sysadmin armed with nothing but a trusty laptop and a healthy dose of sarcasm. Your playground is **Nerdstown**, a neon-soaked metropolis where Ethernet cables snake through alleyways, cafés pour “Espresso at 5 GHz,” and every corridor hums with server fans. From your cluttered basement hack-den—monitor towers, Linux stickers, and a cat coding in the corner—to the sleek open-space desks at TechCorp, the cozy chaos of Bean Overclock Café, and the cavernous aisles of the Data Center, each location brims with puzzles, NPCs and secrets waiting to be unlocked.

As you traverse these digital frontiers, you’ll face:
- **Linux quizzes** testing your mastery of commands, file permissions, network ports and shell tricks.  
- **Hardware repair missions**: solder bad traces, swap out failing disks, and wrangle stubborn power supplies.  
- **Fetch quests** to retrieve rare gadgets—RAM sticks, power banks or Raspberry Pi modules—from hidden corners.  
- **Dynamic events** like DDoS alerts, retro museum quizzes on the Apple I and surprise blackouts that demand split-second terminal hacks.  
- **NPC interactions** with eccentric characters: from an RGB-obsessed memory vendor to a crusty “SuperHackers” veteran who’s seen every exploit under the sun.

Every success earns you **XP**, in-game **credits**, community **tokens** and coveted **reputation**. Level up to unlock `sudo` privileges, open restricted rooms, and negotiate high-stakes side-quests. Whether you’re debugging a runaway cron job or outsmarting a firewall with clever iptables rules, **IT Adventures** turns every shell command into a step toward hacker legend—one witty one-liner at a time.

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
