#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from data      import (
    load_game_data, new_game_state,
    save_state, load_state
)
from ui        import (
    console, draw_hud, render_room, render_inventory,
    render_missions, render_npc_list, prompt
)
from quests    import (
    list_missions_at, start_mission
)
from npcs      import (
    list_npcs_at, talk_to_npc
)


def main_menu():
    """Menu iniziale: Nuova/Carica/Salva/Aiuto/Esci."""
    world, missions, items, npcs = load_game_data()
    state = None

    while True:
        console.clear()
        console.rule("[bold blue]IT Adventures – Nerdstown Chronicles[/]")
        console.print(
            "\n[bold]1)[/] Nuova partita    "
            "[bold]2)[/] Carica partita    "
            "[bold]3)[/] Salva partita    "
            "[bold]4)[/] Aiuto    "
            "[bold]5)[/] Esci\n"
        )

        scelta = prompt()
        if scelta == "1":
            state = new_game_state()
            game_loop(state, world, missions, items, npcs)

        elif scelta == "2":
            loaded = load_state()
            if loaded:
                state = loaded
                game_loop(state, world, missions, items, npcs)

        elif scelta == "3":
            if state:
                save_state(state)
            else:
                console.print("[red]Nessuna partita attiva da salvare.[/]")

        elif scelta == "4":
            console.print("""
[bold]Comandi Menu:[/]
  1 – Nuova partita
  2 – Carica partita
  3 – Salva partita
  4 – Aiuto
  5 – Esci

[bold]Comandi in Gioco:[/]
  vai <direzione>    – spostati
  prendi <oggetto>   – raccogli oggetto
  usa <oggetto>      – usa oggetto
  inventario         – mostra inventario
  missioni           – elenca missioni locali
  inizia <id>        – avvia missione
  parla <npc_id>     – interagisci con NPC
  stato              – mostra HUD
  aiuto              – questo testo
  salva              – salva in qualsiasi momento
  esci               – torna al menu iniziale
""")
            prompt()

        elif scelta == "5":
            console.print("\n[bold green]Grazie per aver giocato![/]")
            sys.exit(0)

        else:
            console.print("[red]Scelta non valida.[/]")
            prompt()


def game_loop(state, world, missions, items, npcs):
    """Loop principale di gioco."""
    while True:
        # render HUD e stanza
        draw_hud(state)
        render_room(state, world)
        render_npc_list(state, npcs)
        
        cmd = prompt().split()
        if not cmd:
            continue

        action = cmd[0].lower()

        # --- USCITA AL MENU ---
        if action in ("esci", "quit"):
            console.print("[yellow]Tornando al menu principale...[/]")
            break

        # --- HUD e info ---
        elif action == "stato":
            draw_hud(state)

        elif action == "guarda":
            render_room(state, world)

        elif action in ("inventario", "inv"):
            render_inventory(state, items)

        elif action == "missioni":
            render_missions(state, missions)

        # --- MOVIMENTO ---
        elif action == "vai" and len(cmd) == 2:
            direzione = cmd[1]
            current_room = world[state.current]
            dest = current_room["exits"].get(direzione)
            if not dest:
                console.print(f"[red]Non puoi andare '{direzione}'.[/]")
            else:
                req = world[dest].get("requires")
                if req and req not in state.inventory:
                    console.print(f"[red]Serve '{req}' per entrare.[/]")
                else:
                    state.current = dest

        # --- RACCOGLI OGGETTO ---
        elif action == "prendi" and len(cmd) == 2:
            oid = cmd[1]
            room = world[state.current]
            if oid in room.get("items", []):
                state.inventory.append(oid)
                room["items"].remove(oid)
                console.print(f"[green]Hai raccolto '{oid}'.[/]")
            else:
                console.print(f"[red]Oggetto '{oid}' non presente.[/]")

        # --- USA OGGETTO ---
        elif action == "usa" and len(cmd) == 2:
            oid = cmd[1]
            if oid in state.inventory and state.current in items[oid]["usable_in"]:
                console.print(f"[green]Hai usato '{oid}'.[/]")
                # eventuali effetti speciali in quest/eventi
            else:
                console.print(f"[red]Non puoi usare '{oid}' qui.[/]")

        # --- AVVIO MISSIONE ---
        elif action == "inizia" and len(cmd) == 2:
            try:
                mid = int(cmd[1])
                if mid in state.missions_done:
                    console.print("[yellow]Hai già completato questa missione.[/]")
                else:
                    start_mission(mid, state, world, missions, items, npcs)
            except ValueError:
                console.print("[red]ID missione non valido.[/]")

        # --- INTERAZIONE NPC ---
        elif action == "parla" and len(cmd) == 2:
            npc_id = cmd[1]
            talk_to_npc(npc_id, state, world, missions, items)

        # --- SALVA IN-GAME ---
        elif action == "salva":
            save_state(state)

        elif action == "aiuto":
            console.print("[cyan]Digita 'menu' per tornare al menu principale o 'esci'[/]")

        else:
            console.print("[red]Comando non riconosciuto. Digita 'aiuto' per aiuto.[/]")

        # Controllo vittoria: raggiunto il Cloud?
        if state.current == "cloud":
            console.print("\n[bold green]Hai conquistato il Cloud di Nerdstown![/]")
            save_state(state)
            sys.exit(0)


if __name__ == "__main__":
    main_menu()
