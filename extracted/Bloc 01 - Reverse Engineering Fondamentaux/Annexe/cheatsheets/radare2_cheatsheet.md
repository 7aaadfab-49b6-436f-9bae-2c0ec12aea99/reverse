# radare2 - Cheatsheet

## Ouverture
```
r2 ./binary                  # lecture seule
r2 -d ./binary               # mode debug
r2 -A ./binary               # analyse auto (=aaa)
r2 -w ./binary               # write mode (pour patcher)
```

## Analyse
| Cmd | Action |
|-----|--------|
| `aaa` | analyse agressive (à faire en 1er) |
| `afl` | list fonctions |
| `afvd` | variables locales fonction actuelle |
| `axt @ main` | xrefs vers main |

## Navigation
| Cmd | Action |
|-----|--------|
| `s main` | seek sur main |
| `s 0x400520` | seek address |
| `V` | mode visuel |
| `VV` | graph mode |
| `q` | quitter mode visuel |

## Disassembly & strings
| Cmd | Action |
|-----|--------|
| `pdf` | disas fonction |
| `pd 20` | 20 instructions |
| `pdc` | pseudo-C |
| `izz` | toutes strings (même data non-section) |
| `iz` | strings data section |
| `ii` | imports |
| `iS` | sections |
| `iI` | info binaire (arch, canary...) |

## Debug
| Cmd | Action |
|-----|--------|
| `ood` | reopen en debug |
| `dc` | continue |
| `ds` / `dso` | step / step over |
| `db 0x400520` | BP address |
| `dbl` | list BPs |
| `dr` | registres |
| `dm` | mappings mémoire |

## Patching
```
wa nop               # écrit NOP à l'offset
wx 9090              # écrit octets hex
wc                   # applique patches au disque
```

## Python scripting
```python
import r2pipe
r = r2pipe.open("./bin")
r.cmd("aaa")
print(r.cmdj("aflj"))     # JSON output
```
