# pwndbg - commandes essentielles

- `context` : affiche regs + stack + code (fait à chaque stop)
- `telescope <addr>` : explorer la mémoire
- `vmmap` : mappings mémoire (RWX, segments)
- `checksec` : NX, PIE, RELRO, Canary, ASLR
- `got` / `plt` : tables GOT/PLT
- `heap` / `bins` : analyse tas glibc
- `search -s "string"` : cherche string en mémoire
- `cyclic 100` / `cyclic -l 0x61616166` : pattern offset pour BOF
- `ropper --file ./bin --search "pop rdi"` : chercher gadgets
