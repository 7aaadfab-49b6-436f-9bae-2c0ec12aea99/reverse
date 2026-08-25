# Crackmes - Reverse Engineering Fondamentaux

## Compilation
```bash
make                    # compile tous les crackmes
make clean              # clean
```

## Niveaux

| # | Binaire | Niveau | Technique | Outils suggérés |
|---|---------|--------|-----------|-----------------|
| 01 | crackme01_strings | Débutant | Strings statiques | `strings`, `rabin2 -zz` |
| 02 | crackme02_xor | Facile | XOR décodage | radare2, pwntools |
| 03 | crackme03_antidebug | Moyen | Anti-debug bypass | gdb, LD_PRELOAD |
| 04 | crackme04_packed | Moyen+ | Unpacking RAM | gdb, memory dump |
| 05 | crackme05_crypto | Difficile | Hash preimage | Z3 solver, bruteforce |

## Flags à récupérer

Chaque crackme affiche un flag au format `CYBERSUP{...}` à documenter dans le rapport.

## Extension UPX (optionnel)

Pour s'entraîner sur du vrai packing :
```bash
gcc -O0 -o crackme04_upx crackme01_strings.c
upx --best crackme04_upx
file crackme04_upx              # montre "packed by UPX"
upx -d crackme04_upx             # unpack standard
```

## Anti-triche

Ne pas diffuser les sources aux étudiants : ne leur donner que les binaires compilés.
Sur le Drive : mettre les binaires dans `binaries/` et les sources dans un dossier `SOLUTIONS_FORMATEUR/` caché (ou un Drive séparé).
