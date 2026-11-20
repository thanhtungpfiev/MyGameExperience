"""Pre-commit guard for StardewValley/Saves/Wind/Wind - Daily.md.

1. A closed season section must not change, because a scripted edit that
   matched the wrong day heading once overwrote Spring 10 with Summer 10.
2. No two ### headings may be identical, so a day can always be found by
   its heading alone.

Bypass check 1 with ALLOW_CLOSED_SEASON_EDIT=1 when the edit is intended.
"""
import collections
import os
import subprocess
import sys

DAILY = "StardewValley/Saves/Wind/Wind - Daily.md"
# Seasons already played out. Add the next one when its last day is closed.
CLOSED = ["## 📆 Năm 1 · Xuân"]


def show(rev):
    r = subprocess.run(["git", "show", f"{rev}:{DAILY}"], capture_output=True)
    return r.stdout.decode("utf-8").replace("\r\n", "\n") if r.returncode == 0 else None


def section(text, heading):
    lines = text.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    except StopIteration:
        return None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return "\n".join(lines[start:end]).rstrip()


def main():
    staged = subprocess.run(["git", "diff", "--cached", "--name-only", "-z"], capture_output=True)
    if DAILY not in staged.stdout.decode("utf-8").split("\0"):
        return 0
    new, old = show(""), show("HEAD")
    if new is None:
        return 0
    errors = []

    dups = [h for h, c in collections.Counter(
        l.strip() for l in new.split("\n") if l.startswith("### ")).items() if c > 1]
    for h in dups:
        errors.append(f"duplicate heading: {h}")

    if old is not None and os.environ.get("ALLOW_CLOSED_SEASON_EDIT") != "1":
        for heading in CLOSED:
            if section(old, heading) != section(new, heading):
                errors.append(f"closed season changed: {heading}")

    if errors:
        sys.stderr.reconfigure(encoding="utf-8")
        print(f"pre-commit: {DAILY}", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print("  Intended? Re-run with ALLOW_CLOSED_SEASON_EDIT=1 "
              "(duplicate headings are never allowed).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
