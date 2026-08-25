# Image Docker Reverse Lab

## Build
```bash
docker build -t cybersup/reverse-lab:m2 .
```

## Run
```bash
docker run -it --rm \
  --security-opt seccomp=unconfined \
  --cap-add=SYS_PTRACE \
  -v $(pwd)/../crackmes:/home/student/crackmes \
  cybersup/reverse-lab:m2
```

Les capabilities `SYS_PTRACE` + seccomp unconfined sont nécessaires pour gdb.

## Outils inclus

gdb+pwndbg, radare2, pwntools, LIEF, capstone, unicorn, keystone, ropper, yara, strace, ltrace, checksec, r2pipe.
