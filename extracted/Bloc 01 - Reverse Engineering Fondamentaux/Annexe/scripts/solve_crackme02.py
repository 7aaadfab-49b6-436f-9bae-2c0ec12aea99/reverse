#!/usr/bin/env python3
"""Solution pour crackme02_xor - montre comment résoudre avec pwntools/python"""
cipher = bytes([0x15, 0x33, 0x03, 0x23, 0x15, 0x34, 0x17, 0x25, 0x1C, 0x26, 0x0F, 0x26, 0x0F, 0x37, 0x14])
key = b"KEY"
plaintext = bytes([c ^ key[i % 3] for i, c in enumerate(cipher)])
print(f"Password: {plaintext.decode()}")
