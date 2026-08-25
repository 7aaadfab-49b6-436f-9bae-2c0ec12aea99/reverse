# pwntools - Cheatsheet

## Import et setup
```python
from pwn import *
context.arch = 'amd64'
context.log_level = 'info'
```

## Process / remote
```python
p = process("./binary")              # local
p = remote("ctf.example.com", 1337)  # remote
p = gdb.debug("./binary", gdbscript="break main\n")
```

## IO
```python
p.sendline(b"payload")
p.send(b"raw bytes")
p.recvuntil(b"prompt> ")
p.recvline()
p.interactive()                      # hand over shell
```

## Packing
```python
p64(0xdeadbeef)                      # struct.pack
u64(b"\x41\x42\x43...")              # unpack
```

## ROP
```python
elf = ELF("./binary")
libc = ELF("./libc.so.6")
rop = ROP(elf)
rop.puts(elf.got['puts'])
rop.main()
p.sendline(flat(cyclic(72), rop.chain()))
```

## Format string exploitation
```python
from pwn import FmtStr
def send(payload):
    p.sendline(payload)
    return p.recvline()
fs = FmtStr(execute_fmt=send)
fs.write(target_addr, value)
```

## Debugging
```python
gdb.attach(p, gdbscript="""
break *0x401234
continue
""")
```

## Payload construction
```python
padding = cyclic(40)
ret_gadget = p64(0x4006f0)
libc_base = leaked_libc - libc.sym['puts']
payload = padding + ret_gadget + p64(libc_base + libc.sym['system'])
```