#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.align import Align
from rich.text import Text

console = Console()

def draw_hud(state):
    """
    Disegna l'HUD in alto con Livello, XP, Crediti, OSS e Reputazione.
    """
    hud = Table.grid(expand=True)
    hud.add_column(justify="center")
    hud.add_column(justify="center")
    hud.add_column(justify="center")
    hud.add_column(justify="center")
    hud.add_column(justify="center")
    
    hud.add_row(
        f"[bold green]Livello[/]: {state.level}",
        f"[bold cyan]XP[/]: {state.xp}/{state.level*100}",
        f"[bold yellow]Crediti[/]: {state.credits}",
        f"[bold magenta]OSS[/]: {state.oss}",
        f"[bold white]Reputazione[/]: {state.reputation}"
    )
    
    console.clear()
    console.rule("[bold blue]IT Adventures – Nerdstown Chronicles[/]")
    console.print(hud)
    console.rule()

def render_room(state, world):
    """
    Mostra titolo, descrizione, oggetti e uscite della stanza corrente.
    """
    room = world[state.current]
    title = Text(room["title"], style="bold magenta")
    desc  = Text(room["desc"], style="white")
    
    panel = Panel(
        Align.left(desc), 
        title=title, border_style="magenta", expand=False
    )
    console.print(panel)
    
    # Oggetti presenti
    items = room.get("items", [])
    if items:
        tbl = Table(title="Oggetti in vista", box=None, show_header=False)
        for it in items:
            tbl.add_row(f"• {it}")
        console.print(tbl)
    
    # Uscite
    exits = []
    for d, dest in room.get("exits", {}).items():
        req = world[dest].get("requires")
        if req and req not in state.inventory:
            exits.append(f"[red]{d}[/] (bloccata: serve {req})")
        else:
            exits.append(f"[green]{d}[/]")
    exits_txt = Text("  ".join(exits), style="bold")
    console.print(Panel(exits_txt, title="Uscite", border_style="green"))

def render_inventory(state, items_catalog):
    """
    Mostra una tabella con inventario: Nome oggetto e descrizione breve.
    """
    if not state.inventory:
        console.print(Panel("Inventario vuoto.", title="Inventario", border_style="yellow"))
        return
    
    tbl = Table(title="Inventario", show_header=True, header_style="bold cyan")
    tbl.add_column("OGGETTO", style="white")
    tbl.add_column("DESCRIZIONE", style="dim")
    for oid in state.inventory:
        item = items_catalog.get(oid, {})
        tbl.add_row(item.get("name", oid), item.get("description", ""))
    console.print(tbl)

def render_missions(state, missions):
    """
    Elenca missioni disponibili nella stanza corrente.
    """
    avail = [m for m in missions 
             if m['location'] == state.current 
             and m['id'] not in state.missions_done]
    
    if not avail:
        console.print(Panel("Nessuna missione qui.", title="Missioni", border_style="red"))
        return
    
    tbl = Table(title="Missioni disponibili", header_style="bold magenta")
    tbl.add_column("ID", style="cyan", width=4)
    tbl.add_column("TITOLO", style="white", overflow="fold")
    tbl.add_column("TIPO", style="yellow", width=8)
    for m in avail:
        tbl.add_row(str(m['id']), m['title'], m['type'])
    console.print(tbl)

def render_npc_list(state, npcs):
    """
    Elenca gli NPC presenti nella stanza corrente.
    """
    here = [n for n in npcs if n['location'] == state.current]
    if not here:
        return
    tbl = Table(title="Personaggi qui", header_style="bold green")
    tbl.add_column("ID", style="cyan", width=4)
    tbl.add_column("NOME", style="white")
    for n in here:
        tbl.add_row(n['id'], n['name'])
    console.print(tbl)

def prompt():
    """
    Stampa un prompt colorato e ritorna l'input utente.
    """
    console.print("\n[bold yellow]>[/] ", end="")
    return input().strip()

# Nota: importate le funzioni in engine.py così:
#   from src.ui import draw_hud, render_room, render_inventory, render_missions, render_npc_list, prompt
