# Ghidra - Cheatsheet

## Démarrage
- Lancer `./ghidraRun`
- New project → Non-Shared
- Importer binaire → Analyze (laisser défauts)

## Raccourcis (CodeBrowser)
| Raccourci | Action |
|-----------|--------|
| G | Go to address |
| L | Rename symbol |
| H | Rename variable |
| Ctrl+Shift+G | Rechercher dans disas |
| F | Create function |
| T | Change data type |
| `;` | Ajouter commentaire |
| Ctrl+H | Label/rename |
| Ctrl+Shift+F | Find references |

## Decompiler window
- `F5` : rafraîchir
- Click droit sur var → "Rename Variable"
- Click droit → "Auto Create Structure"

## Scripts utiles (Script Manager, Ctrl+Shift+O)
- `ExportSymbolsScript.java`
- `FunctionID`
- `BookmarkFunctionsScript.java`

## Headless
```bash
$GHIDRA_HOME/support/analyzeHeadless \
    /tmp/project_dir project_name \
    -import binary \
    -postScript my_script.java \
    -deleteProject
```

## Plugins utiles
- Ghidrathon (Python 3)
- BinExport (diff avec BinDiff)
- Kaiju
- ret-sync (sync avec gdb/windbg)
