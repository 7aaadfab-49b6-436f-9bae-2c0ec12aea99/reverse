# reverse — Bloc 01, Reverse Engineering Fondamentaux

Write-up for the five crackmes in the **CyberSup "Bloc 01 – Reverse Engineering Fondamentaux"** kit.

The interesting part isn't that I solved them — it's *how*. The whole set is supposed to walk you up a difficulty ladder (static strings → XOR → anti-debug → unpacking → hash preimage), but a single command defeats all five, because every flag is stored **in clear text inside the binary**.

---

## TL;DR — one string, every answer

```bash
for b in crackme01_strings crackme02_xor crackme03_antidebug crackme04_packed crackme05_crypto; do
    echo "== $b =="
    strings "$b" | grep Flag
done
```

`strings` walks the binary and prints every printable byte sequence. Since each crackme builds its success message with a literal like:

```c
printf("[+] Flag: CYBERSUP{...}\n");
```

…the compiler bakes that whole string — flag included — straight into the `.rodata` section. You never have to run the check, defeat the debugger, unpack anything, or solve a hash. The flag is just *sitting there* in the file.

That's the core issue: **the intended protection is on the input path (the `strcmp`/`check`/anti-debug logic), but the reward (the flag) is a plaintext constant that lives in the binary regardless of whether you pass the check.**

---

## The issue, crackme by crackme

| # | Binary | Intended technique | What actually broke it | Flag |
|---|--------|--------------------|------------------------|------|
| 01 | `crackme01_strings` | read static strings | `strings` (this one is *meant* to fall this way) | `CYBERSUP{w3lc0m3_t0_r3v3rs3}` |
| 02 | `crackme02_xor` | reverse the XOR loop, recover key+cipher | `strings … \| grep Flag` — flag never gets XOR'd | `CYBERSUP{x0r_1s_w34k_g0t_1t}` |
| 03 | `crackme03_antidebug` | bypass `ptrace`/`TracerPid` (LD_PRELOAD) | `strings` — anti-debug guards the input, not the string | `CYBERSUP{ptr4c3_byp4ss3d_w1th_lr_pr3l0ad}` |
| 04 | `crackme04_packed` | dump the "packed" blob from RAM after unpack | `strings` — the *password* is XOR'd, the *flag* isn't | `CYBERSUP{unp4ck3d_th3_s3cr3t}` |
| 05 | `crackme05_crypto` | Z3 / bruteforce a hash preimage | `strings` leaks the flag **template** (see caveat) | `CYBERSUP{z3_solv3d_th3_h4sh_%08x}` |

### Why each "protection" doesn't protect the flag

- **02 (XOR):** only the *password* is stored as an obfuscated `cipher[]` array. The flag string is a plain literal, so obfuscating the input comparison does nothing for it.
- **03 (anti-debug):** `is_debugged_ptrace()` and the `/proc/self/status` `TracerPid` check only gate *execution*. `strings` reads the file on disk without ever running it, so the guards are irrelevant. (If you *do* want to run it under a debugger, that's what `bypass.so` in the repo root is for — see below.)
- **04 ("packed"):** the "pack" is a symbolic XOR-0xAA over the *password* bytes (`encrypted_func[]`) that's decoded at runtime. The flag itself is, again, a plain literal — no dumping required.
- **05 (crypto):** this is the one partial exception. `strings` gives you `CYBERSUP{z3_solv3d_th3_h4sh_%08x}` — the format string, not the final value. The `%08x` is filled at runtime with `h`, and the success branch is only reachable when `h == 0xDEADBABE`, so the real flag resolves to **`CYBERSUP{z3_solv3d_th3_h4sh_deadbabe}`**. You get 90% of it for free from `strings`; the last token you can reason out from the source/branch condition without ever running the solver.

---

## Where the answers live

I saved each result next to the crackmes it came from:

```
extracted/Bloc 01 - Reverse Engineering Fondamentaux/Annexe/crackmes/
├── crackme01-awnser      # strings on the file → flag
├── crackme02-awnser      # strings crackme02_xor  | grep Flag
├── crackme03-awnser      # strings crackme03_antidebug | grep Flag
├── crackme04-awnsers     # strings crackme04_packed | grep Flag
└── crackme05-awnsers     # strings crackme05_crypto | grep Flag
```

Each `*-awnser` file contains the exact command used and the line it returned. (Filenames keep the original `awnser`/`awnsers` spelling as committed.)

Full path from repo root, for reference:
`extracted/Bloc 01 - Reverse Engineering Fondamentaux/Annexe/crackmes/`

---

## `bypass.so` — the "proper" way to run crackme03

If you want to actually execute `crackme03_antidebug` under a debugger instead of just reading its strings, the repo root ships an `LD_PRELOAD` shim (`bypass.c` → `bypass.so`) that neutralises both anti-debug checks:

- `ptrace()` is overridden to always return `0` (reports "no tracer, no error"), defeating the `PTRACE_TRACEME` self-attach trick.
- `open()` is hooked so that reads of `/proc/self/status` are redirected to a fake file with `TracerPid: 0`, defeating the status-file check.

Build & use:

```bash
gcc -shared -fPIC -o bypass.so bypass.c -ldl
LD_PRELOAD=./bypass.so gdb ./crackme03_antidebug
# now the "Debugger detected" branch never fires
```

You'll need `/tmp/fake_status_no_tracer` to contain a line like `TracerPid:\t0` for the `open` redirect to work cleanly.

---

## Takeaway (a.k.a. how the course should fix this)

The lesson these crackmes accidentally teach is a real one: **never store your secret/reward as a plaintext constant.** A binary is not a safe place to hide a string. To make the higher levels actually require their intended technique, the flag should be *derived* from the work, not printed from a literal — e.g.:

- build the flag at runtime by XOR-decoding it with the recovered key (02),
- only reconstruct the flag *inside* the guarded branch from data that's meaningless until you've unpacked it (04),
- or derive the flag bytes from the hash preimage itself so it can't exist in the binary until you've solved it (05).

Until then: `strings | grep Flag` is the master key.