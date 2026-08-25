# GDB + pwndbg - Cheatsheet

## Lancer
```
gdb ./binary                 # classique
gdb --args ./binary arg1     # avec args
gdb -p <pid>                 # attach
```

## Breakpoints
| Cmd | Action |
|-----|--------|
| `b *main` | BP sur main |
| `b *0x400530` | BP adresse |
| `b file.c:42` | BP ligne source |
| `info b` | liste BPs |
| `delete 1` | supprime BP 1 |
| `tbreak main` | BP temporaire |
| `rbreak regex` | BP par regex nom |

## Exécution
| Cmd | Action |
|-----|--------|
| `r` | run |
| `c` | continue |
| `n` / `ni` | next (src/instr) |
| `s` / `si` | step in |
| `finish` | sort de la fonction |
| `until <addr>` | jusqu'à adresse |

## Inspection
| Cmd | Action |
|-----|--------|
| `info registers` / `i r` | registres |
| `x/20gx $rsp` | 20 qwords depuis rsp |
| `x/20i $pc` | 20 instructions |
| `x/s 0x...` | string à addr |
| `disas main` | disassembly |
| `backtrace` / `bt` | pile d'appels |
| `frame N` | saut dans frame |

## Modif
| Cmd | Action |
|-----|--------|
| `set $rax = 0` | modifier registre |
| `set *(int*)0x... = 0x41` | écrire en mémoire |
| `jump *0x400500` | saut arbitraire |

## pwndbg spécifique
| Cmd | Action |
|-----|--------|
| `checksec` | NX/PIE/RELRO/Canary |
| `vmmap` | mappings mémoire |
| `telescope 0x... 20` | 20 qwords tele |
| `heap` | tas glibc |
| `cyclic 200` | pattern BOF |
| `got` | GOT entries |
| `search -s "flag"` | chercher string |
