# Références externes — Bloc 01 Reverse Engineering M2

## VMs prêtes à l'emploi (à télécharger)

| Ressource | URL | Usage |
|-----------|-----|-------|
| Kali Purple | https://www.kali.org/get-kali/ | Distribution offensive+défensive |
| REMnux | https://remnux.org | Reverse malware |
| FlareVM | https://github.com/mandiant/flare-vm | Windows RE (Mandiant) |
| SIFT Workstation | https://www.sans.org/tools/sift-workstation/ | Forensic (inclut RE tools) |

## Outils majeurs

| Outil | URL | Licence |
|-------|-----|---------|
| Ghidra | https://github.com/NationalSecurityAgency/ghidra/releases | Open source (NSA) |
| radare2 | https://github.com/radareorg/radare2 | Open source |
| Cutter (GUI r2) | https://cutter.re | Open source |
| pwndbg | https://github.com/pwndbg/pwndbg | Open source |
| IDA Free | https://hex-rays.com/ida-free/ | Gratuit (version limitée) |
| Binary Ninja | https://binary.ninja | Commercial (licence éducation) |
| x64dbg | https://x64dbg.com | Open source (Windows) |
| Frida | https://frida.re | Open source |

## Crackmes supplémentaires (externes)

| Plateforme | URL | Difficulté |
|-----------|-----|------------|
| crackmes.one | https://crackmes.one | Tous niveaux |
| Reverse Engineering challenges | https://challenges.re | Tous niveaux |
| Flare-On | https://flare-on.com | CTF annuel Mandiant (hard) |
| HackTheBox RE track | https://app.hackthebox.com | Bonne progression |
| TryHackMe Reverse Engineering | https://tryhackme.com/module/reverse-engineering | Débutant |
| PicoCTF Reverse | https://picoctf.org | Étudiants |

## Ressources pédagogiques

| Type | Titre | Lien |
|------|-------|------|
| Livre | Practical Malware Analysis (Sikorski) | O'Reilly |
| Livre | Practical Binary Analysis (Andriesse) | No Starch Press |
| Livre | Reverse Engineering for Beginners (Yurichev) | https://beginners.re (gratuit !) |
| Cours | MalwareUnicorn Workshops | https://malwareunicorn.org/workshops |
| Cours | OpenSecurityTraining2 | https://ost2.fyi |
| Blog | liveoverflow YouTube | https://youtube.com/liveoverflow |

## Datasets malware (pour analyse lab)

**ATTENTION : samples malware réels. À manipuler UNIQUEMENT dans VM isolée sans réseau.**

| Source | URL | Accès |
|--------|-----|-------|
| MalwareBazaar | https://bazaar.abuse.ch/ | Gratuit inscription |
| VirusShare | https://virusshare.com | Sur demande |
| theZoo | https://github.com/ytisf/theZoo | Public (⚠️) |
| VX Underground | https://vx-underground.org | Public (⚠️) |
| Hybrid Analysis | https://www.hybrid-analysis.com | Gratuit (public reports) |

## Règles YARA publiques

| Repo | Lien |
|------|------|
| YARA-Rules | https://github.com/Yara-Rules/rules |
| Elastic Security rules | https://github.com/elastic/protections-artifacts |
| Neo23x0 signature-base | https://github.com/Neo23x0/signature-base |
| Reversing Labs YARA rules | https://github.com/reversinglabs/reversinglabs-yara-rules |

## Tutoriels vidéo recommandés (FR/EN)

- LiveOverflow (YT) — séries RE et binary exploitation
- Ippsec (YT) — HackTheBox walkthroughs
- OALabs (YT) — malware analysis live
- Guided Hacking (YT) — game hacking / RE (pour la pratique seulement)

## Challenges pour examen blanc

Suggérés avant certifications CEH/OSCE/CRTE (niveau M2) :
1. Flare-On années 2022 et 2023 (tous niveaux)
2. HackTheBox Reverse section : Phonebook, Baby RE, Cryptohorrific
3. Root-Me RE challenges (FR)

## Setup conseillé environnement local

```bash
# VM Kali Purple + outils supplémentaires
sudo apt install -y ghidra radare2 gdb gef
git clone https://github.com/pwndbg/pwndbg /opt/pwndbg && cd /opt/pwndbg && ./setup.sh
pip3 install pwntools r2pipe lief capstone unicorn

# Ghidra (dernière version)
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.x/ghidra_11.x_PUBLIC.zip
unzip ghidra_*.zip -d /opt/

# Ajouter au .bashrc
export GHIDRA_HOME=/opt/ghidra_11.x_PUBLIC
export PATH=$PATH:$GHIDRA_HOME/support
```

## Liens crackmes à récupérer AVANT cours (pré-requis étudiants)

Créer un script `download_prerequisites.sh` :
```bash
#!/bin/bash
mkdir -p ~/cybersup_m2/reverse_samples
cd ~/cybersup_m2/reverse_samples
wget https://raw.githubusercontent.com/Yara-Rules/rules/master/malware/MALW_Zeus.yar
# etc.
```
