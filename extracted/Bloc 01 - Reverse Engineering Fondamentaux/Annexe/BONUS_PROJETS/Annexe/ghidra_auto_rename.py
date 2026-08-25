"""Ghidra script: auto-rename functions based on API calls"""
#@author Cybersup
#@category Security
#@keybinding

from ghidra.program.model.symbol import SymbolType

def get_api_calls(function):
    """Return list of API calls from a function"""
    apis = []
    listing = currentProgram.getListing()
    body = function.getBody()
    for addr in body.getAddresses(True):
        instr = listing.getInstructionAt(addr)
        if instr and instr.getFlowType().isCall():
            callee_addr = instr.getFlows()[0] if instr.getFlows() else None
            if callee_addr:
                callee = getFunctionAt(callee_addr)
                if callee:
                    apis.append(callee.getName())
    return apis

def suggest_name(apis):
    """Heuristic naming based on APIs called"""
    if any("CreateFile" in a for a in apis):
        return "file_ops"
    if any("socket" in a or "connect" in a for a in apis):
        return "network_handler"
    if any("CryptoAPI" in a or "RSA" in a for a in apis):
        return "crypto_op"
    return None

for func in currentProgram.getFunctionManager().getFunctions(True):
    if func.getName().startswith("FUN_"):
        apis = get_api_calls(func)
        suggestion = suggest_name(apis)
        if suggestion:
            new_name = f"{suggestion}_{func.getEntryPoint()}"
            func.setName(new_name, ghidra.program.model.symbol.SourceType.USER_DEFINED)
            print(f"Renamed {func.getEntryPoint()} -> {new_name}")
