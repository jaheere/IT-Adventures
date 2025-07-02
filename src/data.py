# src/data.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os, sys
from dataclasses import dataclass, field
from typing import List, Dict, Any

# --- Percorsi file ---
DATA_DIR       = os.path.join(os.path.dirname(__file__), '..', 'data')
WORLD_FILE     = os.path.join(DATA_DIR, 'world.json')
MISSIONS_FILE  = os.path.join(DATA_DIR, 'missions.json')
ITEMS_FILE     = os.path.join(DATA_DIR, 'items.json')
NPCS_FILE      = os.path.join(DATA_DIR, 'npcs.json')
SAVE_FILE      = os.path.join(os.path.dirname(__file__), '..', 'save.json')

# --- Struttura dello stato di gioco ---
@dataclass
class GameState:
    current: str = 'casa'
    inventory: List[str] = field(default_factory=list)
    flags: Dict[str, Any] = field(default_factory=dict)
    xp: int = 0
    credits: int = 0
    oss: int = 0
    reputation: int = 0
    level: int = 1
    missions_done: List[int] = field(default_factory=list)
    active_mission_id: int = None

    def level_up(self):
        """Controlla e applica salti di livello ogni 100*level XP."""
        while self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1
            print(f"\n*** Complimenti! Sei passato al Livello {self.level}! ***\n")

    def add_reputation(self, amount: int):
        """Aggiunge reputazione e stampa badge speciali."""
        self.reputation += amount
        if self.reputation >= 100:
            print("⭐️ Hai raggiunto la reputazione VIP di Nerdstown! ⭐️")
        elif self.reputation >= 50:
            print("👍 Reputation up! La tua fama cresce in città.")


# --- Caricamento dei JSON di contenuto ---
def load_json(path: str):
    if not os.path.isfile(path):
        print(f"Errore critico: file non trovato: {path}")
        sys.exit(1)
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def load_game_data():
    """Restituisce world, missions, items e npc caricati da JSON."""
    world    = load_json(WORLD_FILE).get('rooms', {})
    missions = load_json(MISSIONS_FILE).get('missions', [])
    items    = {o['id']: o for o in load_json(ITEMS_FILE).get('items', [])}
    npcs     = load_json(NPCS_FILE).get('npcs', [])
    return world, missions, items, npcs

# --- Nuova partita, salvataggio e caricamento stato ---
def new_game_state() -> GameState:
    """Crea uno stato di gioco fresco."""
    return GameState()

def save_state(state: GameState):
    data = {
        'current': state.current,
        'inventory': state.inventory,
        'flags': state.flags,
        'xp': state.xp,
        'credits': state.credits,
        'oss': state.oss,
        'reputation': state.reputation,
        'level': state.level,
        'missions_done': state.missions_done,
        'active_mission_id': state.active_mission_id
    }
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f">>> Partita salvata in '{SAVE_FILE}'")

def load_state() -> GameState:
    """Carica stato da SAVE_FILE, o restituisce None se mancante."""
    if not os.path.isfile(SAVE_FILE):
        print(f">>> Nessun salvataggio trovato ({SAVE_FILE}).")
        return None
    raw = load_json(SAVE_FILE)
    state = GameState(
        current=raw.get('current','casa'),
        inventory=raw.get('inventory',[]),
        flags=raw.get('flags',{}),
        xp=raw.get('xp',0),
        credits=raw.get('credits',0),
        oss=raw.get('oss',0),
        reputation=raw.get('reputation',0),
        level=raw.get('level',1),
        missions_done=raw.get('missions_done',[]),
        active_mission_id=raw.get('active_mission_id',None)
    )
    print(">>> Partita caricata con successo! Bentornato a Nerdstown.")
    return state

# --- Esempio di utilizzo rapido (per test) ---
if __name__ == '__main__':
    # demo di caricamento
    w, mq, items, npc = load_game_data()
    print("Rooms disponibili:", list(w.keys()))
    print("Numero missioni:", len(mq))
    print("Catalogo oggetti:", list(items.keys()))
    print("NPC caricati:", [n['id'] for n in npc])
