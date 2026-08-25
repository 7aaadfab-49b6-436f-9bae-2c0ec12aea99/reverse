# Rapport d'Analyse — Reverse Engineering

## 1. Identification du binaire

| Champ | Valeur |
|-------|--------|
| Nom fichier | ... |
| Hash SHA256 | ... |
| Format | ELF64 / PE32+ / Mach-O |
| Taille | ... octets |
| Compilateur | gcc X.X / MSVC / ... |
| Packed | Oui/Non (quel packer ?) |

## 2. Protections

| Protection | État |
|------------|------|
| NX | ... |
| PIE | ... |
| Stack Canary | ... |
| RELRO | ... |
| Fortify | ... |

## 3. Analyse statique

### Graphe d'appels
*insérer capture radare2/Ghidra*

### Fonctions clés

#### main()
```
Pseudocode ou disassembly
```

#### sub_XXXX()
...

### Strings intéressantes
- `...`
- `...`

## 4. Analyse dynamique

### Breakpoints posés
- ...

### Trace d'exécution
```
...
```

### Observations
- ...

## 5. Solution

### Reasoning
Expliquer le raisonnement (comment identifier l'algo, la clé, le bypass...)

### Script de solution
```python
# solve.py
...
```

### Flag / Password
`...`

## 6. IoC & YARA

```yara
rule ...
```

## 7. Recommandations (si applicable)
- ...

## Annexes

- Hashes, screenshots, traces complètes
