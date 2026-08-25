#!/usr/bin/env python3
"""
auto_analyze.py - Analyse statique automatique d'un binaire ELF
Usage: python3 auto_analyze.py <binary>
Dépendances: pip install r2pipe lief
"""
import sys
import os
import r2pipe
import lief

def analyze(path):
    print(f"[+] Analyzing {path}")
    if not os.path.isfile(path):
        print(f"[-] Not found"); sys.exit(1)

    # LIEF - métadonnées ELF
    try:
        binary = lief.parse(path)
        print(f"  Format       : {binary.format}")
        print(f"  Arch         : {binary.header.machine_type}")
        print(f"  Entrypoint   : 0x{binary.entrypoint:x}")
        print(f"  NX           : {binary.has_nx}")
        print(f"  PIE          : {binary.is_pie}")
        print(f"  RELRO        : {'FULL' if binary.has(lief.ELF.DYNAMIC_TAGS.BIND_NOW) else 'partial'}")
        print(f"  # Sections   : {len(binary.sections)}")
        print(f"  # Imports    : {len(list(binary.imported_functions))}")
    except Exception as e:
        print(f"[!] LIEF error: {e}")

    # radare2
    r = r2pipe.open(path)
    r.cmd("aaa")
    functions = r.cmdj("aflj")
    print(f"\n[+] Fonctions découvertes: {len(functions) if functions else 0}")
    if functions:
        main = [f for f in functions if f["name"] in ("main", "sym.main")]
        if main:
            print(f"\n[+] Disassembly main:")
            print(r.cmd(f"pdf @ {main[0]['offset']}"))
    strings = r.cmdj("izzj")
    interesting = [s for s in (strings or []) if s.get("size", 0) > 4 and s.get("size", 0) < 80]
    print(f"\n[+] Strings intéressantes ({len(interesting)}):")
    for s in interesting[:20]:
        print(f"  0x{s.get('vaddr',0):x}  {s.get('string','')}")
    r.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: auto_analyze.py <binary>")
        sys.exit(1)
    analyze(sys.argv[1])
