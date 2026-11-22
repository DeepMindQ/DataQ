#!/usr/bin/env python3
"""Search for surviving GitHub credentials. Reports paths only — never prints secret contents."""
import os, re

PAT = re.compile(r"ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|x-access-token")
ROOTS = ["/home/z", "/tmp"]
SKIP_DIRS = {"node_modules", ".next", ".next-export", "out", "out-gh", "__pycache__",
             "site/.next", ".git/objects", ".git/modules"}
found = []
for root in ROOTS:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith("pagefind")]
        # skip huge binary dirs
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                if os.path.getsize(p) > 3_000_000:
                    continue
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    txt = fh.read()
            except Exception:
                continue
            if PAT.search(txt):
                found.append(p)

print("files containing token-like strings:")
for p in found:
    print("  ", p)
if not found:
    print("  NONE")

# also check git refs / packed configs for credential helper remnants
import subprocess
r = subprocess.run(["git", "-C", "/home/z/my-project", "config", "--list", "--show-origin"],
                   capture_output=True, text=True).stdout
cred_lines = [l for l in r.splitlines() if "credential" in l.lower()]
print("\ngit credential config lines (paths only, redacted):")
for l in cred_lines:
    print("  ", re.sub(r"(password|token)=\S+", r"\1=***", l))
