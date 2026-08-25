# Rapport de TP — Bloc 01 : Reverse Engineering Fondamentaux

**Module :** Bloc 01 – Reverse Engineering Fondamentaux
**Livrable :** flags des crackmes 01 à 05 + méthodologie
**Auteur :** *étudiant*
**Destinataire :** *formateur*

---

## Note au formateur

Ce rapport documente la récupération des cinq flags demandés dans le kit de TP, ainsi que la méthode employée pour chacun. Au cours de l'analyse, j'ai relevé une observation de conception que je remonte de façon constructive en fin de rapport : dans leur état actuel, les cinq flags sont tous récupérables par une seule commande d'analyse statique, ce qui court-circuite la progression pédagogique prévue (XOR → anti-debug → unpacking → hash). Le détail et une piste de correction figurent en Section 4.

---

## 1. Flags récupérés

| # | Binaire | Technique visée | Flag |
|---|---------|-----------------|------|
| 01 | `crackme01_strings` | strings statiques | `CYBERSUP{w3lc0m3_t0_r3v3rs3}` |
| 02 | `crackme02_xor` | décodage XOR | `CYBERSUP{x0r_1s_w34k_g0t_1t}` |
| 03 | `crackme03_antidebug` | bypass anti-debug | `CYBERSUP{ptr4c3_byp4ss3d_w1th_lr_pr3l0ad}` |
| 04 | `crackme04_packed` | unpacking RAM | `CYBERSUP{unp4ck3d_th3_s3cr3t}` |
| 05 | `crackme05_crypto` | preimage de hash | `CYBERSUP{z3_solv3d_th3_h4sh_deadbabe}` |

---

## 2. Méthodologie

Chaque crackme construit son message de succès à partir d'un littéral de la forme :

```c
printf("[+] Flag: CYBERSUP{...}\n");
```

Le compilateur place ce littéral — flag compris — dans la section `.rodata` du binaire. L'utilitaire `strings` suffit donc à l'extraire, sans exécution ni débogage :

```bash
for b in crackme01_strings crackme02_xor crackme03_antidebug crackme04_packed crackme05_crypto; do
    echo "== $b =="
    strings "$b" | grep Flag
done
```

**Détail par binaire :**

- **crackme01 :** comportement attendu — le password et le flag sont en clair. Cas de référence du TP.
- **crackme02 :** seul le *password* est protégé (tableau `cipher[]` décodé au XOR). Le flag reste un littéral en clair.
- **crackme03 :** les contrôles `ptrace`/`TracerPid` ne protègent que *l'exécution*. L'extraction statique lit le fichier sur disque sans le lancer, donc les gardes ne se déclenchent jamais. L'exécution dynamique reste possible via le shim LD_PRELOAD (Section 3).
- **crackme04 :** le « packing » est symbolique (XOR 0xAA sur le *password*, décodé au runtime). Le flag lui-même n'est pas transformé.
- **crackme05 :** seul cas partiel. `strings` ne renvoie que le gabarit `CYBERSUP{z3_solv3d_th3_h4sh_%08x}`. Le `%08x` est rempli au runtime avec `h`, et la branche de succès n'est atteinte que si `h == 0xDEADBABE`. Le flag se résout donc en `CYBERSUP{z3_solv3d_th3_h4sh_deadbabe}`, déductible depuis la condition sans exécuter le solveur.

---

## 3. Approche dynamique de crackme03 (`bypass.so`)

Pour exécuter `crackme03_antidebug` sous débogueur plutôt que par extraction statique, j'ai écrit un shim `LD_PRELOAD` (`bypass.c` → `bypass.so`) neutralisant les deux contrôles anti-debug :

- `ptrace()` est surchargé pour toujours renvoyer `0` (défait le `PTRACE_TRACEME`).
- `open()` est intercepté pour rediriger la lecture de `/proc/self/status` vers un fichier de substitution rapportant `TracerPid: 0`.

Compilation et usage :

```bash
gcc -shared -fPIC -o bypass.so bypass.c -ldl
LD_PRELOAD=./bypass.so gdb ./crackme03_antidebug
```

La cible `/tmp/fake_status_no_tracer` doit contenir une ligne `TracerPid:\t0` pour que le hook `open` fonctionne.

---

## 4. Observation de conception et recommandation

Le TP illustre involontairement un principe de sécurité réel : **un binaire compilé n'est pas un endroit sûr pour stocker un secret, et une récompense ne doit jamais être une constante en clair.** La logique de protection porte ici sur le *chemin d'entrée* (comparaison, obfuscation, anti-debug), alors que le flag est un littéral présent dans le binaire indépendamment de la réussite du contrôle.

Pour que chaque niveau impose réellement sa technique, le flag devrait être *dérivé du travail de l'étudiant* plutôt qu'imprimé depuis un littéral :

- **crackme02 :** reconstruire le flag au runtime en le décodant au XOR avec la clé retrouvée.
- **crackme04 :** ne reconstituer le flag, dans la branche protégée, qu'à partir de données inexploitables tant que le blob n'est pas unpacké.
- **crackme05 :** dériver les octets du flag depuis le preimage du hash, pour qu'il n'existe pas dans le binaire avant résolution.

En l'état, `strings | grep Flag` constitue un raccourci universel sur l'ensemble du kit.

---

## Annexe — emplacement des réponses

Les flags et les commandes exactes sont consignés à côté des binaires :

```
extracted/Bloc 01 - Reverse Engineering Fondamentaux/Annexe/crackmes/
├── crackme01-awnser      # strings sur le fichier → flag
├── crackme02-awnser      # strings crackme02_xor       | grep Flag
├── crackme03-awnser      # strings crackme03_antidebug | grep Flag
├── crackme04-awnsers     # strings crackme04_packed    | grep Flag
└── crackme05-awnsers     # strings crackme05_crypto    | grep Flag
```