#!/usr/bin/env python3
"""Ad-hoc verification: check that all 11 docs/CENTERS/ and docs/MEMBERS/ files exist and have expected structure."""
import os, sys

PROJECT = os.path.expanduser("~/Desktop/ai-army-identity/docs")
CENTERS = ["STRATEGY.md","TAI_SHI_GE.md","ENGINEERING.md","BUSINESS.md","RISK.md","THINK_TANK.md"]
MEMBERS = ["LU_BAN.md","QIAO_ZHIYONG.md","HAI_RUI.md","XIAO_BING.md","SIMA_QIAN.md"]

errors, passes = [], []

for dirname, files in [("CENTERS",CENTERS),("MEMBERS",MEMBERS)]:
    for f in files:
        path = os.path.join(PROJECT, dirname, f)
        if not os.path.exists(path):
            errors.append(f"MISSING: {dirname}/{f}")
            continue
        passes.append(f"{dirname}/{f} exists")
        size = os.path.getsize(path)
        if size < 100:
            errors.append(f"{dirname}/{f}: too small ({size}B)")
        elif size > 2000:
            errors.append(f"{dirname}/{f}: too large ({size}B)")
        else:
            passes.append(f"{dirname}/{f}: {size}B")
        with open(path) as fh:
            content = fh.read()
        if not content.startswith("# "):
            errors.append(f"{dirname}/{f}: missing H1")
        elif "## " not in content:
            errors.append(f"{dirname}/{f}: missing H2")
        else:
            passes.append(f"{dirname}/{f}: has H1+H2")

print("="*58)
print("  AD-HOC VERIFICATION: docs/CENTERS/ + docs/MEMBERS/")
print("="*58)
for p in passes:
    print(f"  ✓ {p}")
if errors:
    for e in errors:
        print(f"  ✗ {e}")
    sys.exit(1)
else:
    print(f"\n✓ ALL {len(passes)} checks passed. 11 files OK.")
    sys.exit(0)
