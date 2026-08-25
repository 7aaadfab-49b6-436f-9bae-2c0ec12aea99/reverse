#!/usr/bin/env python3
"""Extrait strings avec classification (URL, IP, chemins, flags...)"""
import re, sys, subprocess

PATTERNS = {
    "URL":    re.compile(r"https?://[^\s\"'<>]{8,}"),
    "IP":     re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "PATH":   re.compile(r"/(?:usr|etc|var|tmp|home)/[\w\-./]+"),
    "REG":    re.compile(r"HKEY_[A-Z_]+\\\\[^\s\"']+"),
    "FLAG":   re.compile(r"[A-Z]+\{[^}]{5,100}\}"),
    "EMAIL":  re.compile(r"[\w.\-]+@[\w.\-]+\.[a-z]{2,}"),
    "B64":    re.compile(r"[A-Za-z0-9+/]{40,}={0,2}"),
}

def main(path):
    out = subprocess.run(["strings", "-n", "5", path], capture_output=True, text=True).stdout
    buckets = {k: set() for k in PATTERNS}
    for line in out.splitlines():
        for key, pat in PATTERNS.items():
            for m in pat.findall(line):
                buckets[key].add(m)
    for k, v in buckets.items():
        if v:
            print(f"\n=== {k} ({len(v)}) ===")
            for x in sorted(v): print(f"  {x}")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("Usage: string_extractor.py <binary>")
    main(sys.argv[1])
