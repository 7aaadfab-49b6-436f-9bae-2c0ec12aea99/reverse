// Détection de packers connus
rule UPX_packed {
    meta:
        author = "Cybersup"
        description = "Detects UPX packed binaries"
    strings:
        $upx0 = "UPX!"
        $upx1 = "UPX0"
        $upx2 = "UPX1"
        $upx_copyright = "UPX Copyright"
    condition:
        2 of them
}

rule ASPack_packed {
    meta:
        description = "Detects ASPack packed binaries"
    strings:
        $a1 = ".aspack"
        $a2 = ".adata"
    condition:
        any of them
}

rule Themida_packed {
    strings:
        $s1 = "Themida"
        $s2 = "WinLicense"
    condition:
        any of them
}

rule Custom_XOR_loop {
    meta:
        description = "Simple XOR decryption loop pattern (x86/x64)"
    strings:
        // xor al, KEY ; inc rdi ; loop pattern
        $hex_xor_loop = { 30 ?? 48 ff c? 48 83 ?? ?? 75 ?? }
    condition:
        $hex_xor_loop
}
