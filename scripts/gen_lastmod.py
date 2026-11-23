#!/usr/bin/env python3
"""Generate site/src/content/lastmod.json — git-derived per-page last-modified
dates for the sitemap (Top-20 #7). One git log pass over src/content/pages +
the standalone routes; sitemap.ts reads this file at build time and omits
lastmod for any page without a real date (build-timestamp noise is gone).

Run before `next build` in the export pipeline (wired into npm run export).
"""
import json
import subprocess
import sys
from pathlib import Path

SITE = Path("/home/z/my-project/site")
OUT = SITE / "src" / "content" / "lastmod.json"


def git_dates() -> dict:
    """path -> last commit date (YYYY-MM-DD) across tracked content files."""
    cmd = [
        "git", "log", "--name-only", "--pretty=format:__COMMIT__ %cs",
        "--", "src/content/pages", "src/content/brand.json", "src/app",
    ]
    res = subprocess.run(cmd, cwd=SITE, capture_output=True, text=True, check=True)
    dates = {}
    current = None
    for line in res.stdout.splitlines():
        line = line.strip()
        if line.startswith("__COMMIT__"):
            current = line.split(" ", 1)[1]
        elif line and current:
            # first occurrence walking backwards in time = last commit that touched it
            # git prints paths relative to the repo root — normalize to site/-relative
            key = line[len("site/"):] if line.startswith("site/") else line
            dates.setdefault(key, current)
    return dates


def main():
    dates = git_dates()
    OUT.write_text(json.dumps(dates, indent=1))
    print(f"lastmod.json: {len(dates)} paths tracked -> {OUT}")


if __name__ == "__main__":
    sys.exit(main())
