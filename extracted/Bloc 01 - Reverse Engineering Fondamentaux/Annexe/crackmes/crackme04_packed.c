/* Crackme 04 - Niveau MOYEN+
 * Objectif : binaire "packed" (chiffré en RAM, décodé au runtime)
 * Solution : dump mémoire après unpack, analyse dynamique
 * Outils : gdb avec breakpoint sur main, Volatility, dump ELF runtime
 *
 * NB : le "pack" ici est symbolique (XOR simple). Pour du vrai UPX :
 *     upx --best crackme04_packed && upx -d crackme04_packed
 */
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

/* Fonction "cachée" chiffrée au build, décodée en RAM */
static unsigned char encrypted_func[] = {
    /* XOR 0xAA de "check_flag_pwned" */
    0xE9, 0xCE, 0xC9, 0xC9, 0xE1, 0xC4, 0xC6, 0xCE, 0xC7, 0xE1, 0xDA, 0xD1, 0xC4, 0xC9, 0xC9, 0xC8, 0x00
};

int main(void) {
    for (int i = 0; i < (int)sizeof(encrypted_func); i++) encrypted_func[i] ^= 0xAA;
    char input[128];
    printf("[Crackme 04] Unpack and guess: ");
    if (!fgets(input, sizeof(input), stdin)) return 1;
    input[strcspn(input, "\n")] = 0;
    if (strcmp(input, (char *)encrypted_func) == 0) {
        printf("[+] Flag: CYBERSUP{unp4ck3d_th3_s3cr3t}\n");
        return 0;
    }
    printf("[-] Decode the blob!\n");
    return 1;
}
