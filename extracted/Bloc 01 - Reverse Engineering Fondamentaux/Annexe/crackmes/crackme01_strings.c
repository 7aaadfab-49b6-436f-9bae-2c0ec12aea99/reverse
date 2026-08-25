/* Crackme 01 - Niveau DÉBUTANT
 * Objectif : retrouver le password par analyse statique (strings)
 * Solution : le password est en clair dans le binaire
 * Outils : strings, radare2 izz command, ghidra
 */
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    const char *secret = "CyberSup_M2_Reverse_Rocks!";
    char input[128];

    printf("[Crackme 01] Password: ");
    if (!fgets(input, sizeof(input), stdin)) return 1;
    input[strcspn(input, "\n")] = 0;

    if (strcmp(input, secret) == 0) {
        printf("[+] Flag: CYBERSUP{w3lc0m3_t0_r3v3rs3}\n");
        return 0;
    }
    printf("[-] Wrong!\n");
    return 1;
}
