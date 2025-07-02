#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from data import SAVE_FILE
from ui import console
from dataclasses import asdict

def list_missions_at(current_location: str, missions: list, state) -> list:
    """
    Restituisce le missioni non ancora completate disponibili nella stanza.
    """
    return [
        m for m in missions
        if m['location'] == current_location
        and m['id'] not in state.missions_done
    ]


def start_mission(
    mission_id: int,
    state,
    world: dict,
    missions: list,
    items: dict,
    npcs: list
):
    """
    Avvia la missione con id=mission_id: quiz, fetch o event.
    Gestisce premi, reputazione e avanzamento di missione.
    """
    # trova la missione
    m_list = [m for m in missions if m['id'] == mission_id]
    if not m_list:
        console.print(f"[red]Missione {mission_id} non trovata.[/]")
        return
    m = m_list[0]
    console.print(f"\n[bold magenta]Missione '{m['title']}' in corso...[/]\n")

    m_type = m.get('type')
    if m_type == 'quiz':
        _handle_quiz(m, state)
    elif m_type == 'fetch':
        _handle_fetch(m, state, items)
    elif m_type == 'event':
        _handle_event(m, state, world)
    else:
        console.print("[red]Tipo di missione sconosciuto.[/]")

    # segna missione completata
    if m['id'] not in state.missions_done:
        state.missions_done.append(m['id'])


def _apply_rewards(rewards: dict, state):
    """
    Aggiunge XP, crediti, OSS e reputazione allo stato e gestisce level-up.
    """
    xp_gain      = rewards.get('xp', 0)
    credits_gain = rewards.get('credits', 0)
    oss_gain     = rewards.get('oss', 0)
    rep_gain     = rewards.get('reputation', 0)

    state.xp      += xp_gain
    state.credits += credits_gain
    state.oss     += oss_gain
    if rep_gain:
        state.add_reputation(rep_gain)

    console.print(
        f"[green]Ricompense:[/] +{xp_gain} XP, +{credits_gain} crediti, +{oss_gain} OSS"
        + (f", +{rep_gain} reputazione" if rep_gain else "")
    )
    state.level_up()


def _handle_quiz(mission: dict, state):
    """
    Mostra domanda e opzioni, verifica risposta e assegna premi.
    """
    console.print(f"{mission['desc']}\n")
    for idx, opt in enumerate(mission['options']):
        console.print(f"  [cyan]{idx}[/] {opt}")
    try:
        choice = int(input("\n> ").strip())
    except ValueError:
        choice = -1

    if choice == mission['answer']:
        console.print("\n[bold green]✅ Risposta corretta![/]")
        _apply_rewards(mission['rewards'], state)
    else:
        console.print("\n[bold red]❌ Risposta sbagliata.[/]")


def _handle_fetch(mission: dict, state, items: dict):
    """
    Controlla se l'oggetto richiesto è in inventario e assegna premi.
    """
    item_id = mission.get('item')
    if item_id in state.inventory:
        console.print(f"Hai già '{item_id}'. Missione completata.")
        _apply_rewards(mission['rewards'], state)
    else:
        console.print(
            f"[yellow]Devi prima raccogliere '{item_id}' "
            "e poi tornare qui per completare.[/]"
        )


def _handle_event(mission: dict, state, world: dict):
    """
    Gestisce missione di tipo 'event': usa il dizionario 'events' di world.json.
    """
    ev = mission.get('event')
    if not ev:
        console.print("[red]Nessun evento definito per questa missione.[/]")
        return

    # carica direttamente il blocco eventi da world.json
    with open(world_path := SAVE_FILE.replace('save.json','world.json'), encoding='utf-8') as f:
        events = json.load(f).get('events', {})
    event = events.get(ev)
    if not event:
        console.print(f"[red]Evento '{ev}' non trovato in world.json.[/]")
        return

    console.print(f"{event['question']}")
    risposta = input("\n> ").strip().lower()
    if risposta == event['answer']:
        console.print(f"\n[bold green]✅ {event['success']}[/]")
        _apply_rewards(mission['rewards'], state)
    else:
        console.print(f"\n[bold red]❌ {event['failure']}[/]")
