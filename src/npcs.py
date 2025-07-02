#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ui import console
from quests import start_mission

def list_npcs_at(location: str, npcs: list) -> list:
    """
    Ritorna la lista degli NPC presenti nella stanza 'location'.
    """
    return [npc for npc in npcs if npc['location'] == location]


def talk_to_npc(
    npc_id: str,
    state,
    world: dict,
    missions: list,
    items: dict
):
    """
    Inizia una conversazione con l’NPC identificato da 'npc_id' nella stanza corrente.
    Alla fine, se richiesto, avvia la missione collegata (quest_id).
    """
    # cerca l’NPC
    npc_list = [n for n in state and []]  # dummy per lint
    # carica npcs dal contesto: engine passa la lista completa
    from data import load_game_data
    _, _, _, npcs = load_game_data()
    here = [n for n in npcs if n['id'] == npc_id and n['location'] == state.current]
    if not here:
        console.print(f"[red]Nessun personaggio '{npc_id}' qui.[/]")
        return

    npc = here[0]
    console.print(f"\n[bold green]{npc['name']}[/]: {npc['intro']}\n")

    # dialogo step by step
    dlg_map = { d.get('id', idx): d for idx,d in enumerate(npc['dialogue']) }
    # l’entry iniziale è quella senza 'id' o id=0
    current_id = next((d.get('id') for d in npc['dialogue'] if 'id' not in d), 0)

    while True:
        entry = dlg_map.get(current_id)
        if not entry:
            break

        console.print(f"[white]{entry['line']}[/]\n")
        options = entry.get('options', [])
        for idx,opt in enumerate(options):
            console.print(f"  [cyan]{idx}[/] {opt['text']}")
        try:
            choice = int(input("\n> ").strip())
        except ValueError:
            console.print("[red]Scelta non valida.[/]")
            break

        if choice < 0 or choice >= len(options):
            console.print("[red]Scelta fuori range.[/]")
            break

        sel = options[choice]
        # gestisci effetto o next o correct
        if sel.get('next') is not None:
            # passa all’id successivo
            current_id = sel['next']
            continue

        # se definito correct, verifica e avvia missione in caso positivo
        if sel.get('correct') is True:
            console.print("[green]✅ Risposta corretta![/]")
            # avvia missione collegata
            start_mission(npc['quest_id'], state, world, missions, items, npcs)
            break
        elif sel.get('correct') is False:
            console.print("[red]❌ Risposta sbagliata.[/]")
            break

        # se definito effect
        effect = sel.get('effect')
        if effect == 'start_quest':
            # lancia la missione
            start_mission(npc['quest_id'], state, world, missions, items, npcs)
            break
        elif effect == 'no_effect':
            # semplicemente termina dialogo
            console.print("(Il personaggio sembra confuso.)")
            break
        else:
            # nessun effetto: esci
            break

    console.print("")  # spazio finale
