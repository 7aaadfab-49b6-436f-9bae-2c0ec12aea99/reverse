# x86_64 Assembly - Cheatsheet Rapide

## Registres généraux
| 64 | 32 | 16 | 8 | Usage |
|----|----|----|----|--------|
| RAX | EAX | AX | AL | Accumulateur, retour de fonction |
| RBX | EBX | BX | BL | Base, preserved |
| RCX | ECX | CX | CL | Counter / 4e arg |
| RDX | EDX | DX | DL | 3e arg |
| RSI | ESI | SI | SIL | Source / 2e arg |
| RDI | EDI | DI | DIL | Destination / 1er arg |
| RBP | EBP | BP | BPL | Base frame, preserved |
| RSP | ESP | SP | SPL | Stack pointer |
| R8-R15 | ... | | | args 5-6, tmp |

## Convention d'appel System V (Linux, macOS)
args 1-6: RDI RSI RDX RCX R8 R9 ; reste sur la pile
retour : RAX
preserved : RBX RBP R12-R15

## Convention Windows x64
args 1-4: RCX RDX R8 R9 ; shadow space 32 bytes sur pile

## Instructions fréquentes
| Instr | Effet |
|-------|-------|
| `mov dst, src` | copie |
| `lea rax, [rbx+8]` | addr = rbx+8 (pas de deref) |
| `add/sub/imul/idiv` | arith |
| `xor rax, rax` | met rax à 0 |
| `cmp a, b ; je/jne/jg/jl` | compare + saut |
| `test rax, rax ; jz` | zéro test |
| `push/pop` | pile |
| `call <addr>` | push RIP + saut |
| `ret` | pop RIP |
| `syscall` | entre noyau (rax=num, rdi/rsi/... args) |

## Prologue / épilogue typique
```asm
; prologue
push    rbp
mov     rbp, rsp
sub     rsp, 0x20       ; réserve 32 bytes locaux

; épilogue
leave                    ; = mov rsp, rbp ; pop rbp
ret
```

## Patterns fréquents
```
; boucle for(i=0; i<N; i++)
mov rcx, 0
.loop:
    cmp rcx, N
    jge .end
    ; body
    inc rcx
    jmp .loop
.end:

; strcmp
rep cmpsb

; XOR block decrypt
mov rcx, LEN
.dec:
    xor byte [rdi+rcx-1], KEY
    loop .dec
```

## Syscalls Linux x64 (rax = num)
| num | syscall | rdi | rsi | rdx |
|-----|---------|-----|-----|-----|
| 0 | read | fd | buf | count |
| 1 | write | fd | buf | count |
| 2 | open | path | flags | mode |
| 59 | execve | path | argv | envp |
| 60 | exit | status | | |
