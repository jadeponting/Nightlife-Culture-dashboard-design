#!/usr/bin/env python3
"""Stage 2 of closing the Dashboard Design book: move each chapter's process sections,
verbatim, into 06-register/working-record/chNN-workings.md, and renumber the chapter's
numbered sections. Nothing is deleted; nothing else in the chapter text changes.

Run from the repo root: python3 08-edit/move_workings.py
Writes 08-edit/edit-notes/chNN-MOVES.md with what moved and the section renumbering.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "04-chapters"
WR = ROOT / "06-register" / "working-record"
NOTES = ROOT / "08-edit" / "edit-notes"
WR.mkdir(parents=True, exist_ok=True)
NOTES.mkdir(parents=True, exist_ok=True)

MOVE_HEADINGS = [
    r"^## Before you start\s*$",
    r"^## \d+ · (The symmetry test|The studio's own .*tested)\s*$",
    r"^## Open questions and flags\s*$",
    r"^## Looking back\s*$",
    r"^## Gaps found while writing this chapter\s*$",
    r"^## Design system .*conflict log\s*$",
    r"^## Postscript, 7 October 2026.*$",
]
STATUS_LINE = re.compile(r"^\*Version 2, draft 2.*\*\s*$|^\*Version 2 · revised 7 October.*$")

def split_sections(lines):
    """Return list of (heading_line_index_or_None, [lines]) blocks split at '## ' headings."""
    blocks, cur, cur_head = [], [], None
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            blocks.append((cur_head, cur))
            cur, cur_head = [ln], ln
        else:
            cur.append(ln)
    blocks.append((cur_head, cur))
    return blocks

def main():
    for path in sorted(CH.glob("ch*.md")):
        if path.name.startswith("ch00"):
            continue
        num = path.name[2:4]
        lines = path.read_text(encoding="utf-8").splitlines()
        notes = [f"# Chapter {int(num)} · what moved out, by script, 14 October 2026", ""]
        # 1. status line
        kept = []
        for ln in lines:
            if STATUS_LINE.match(ln):
                notes.append(f"- Retired status line: `{ln.strip()}`")
                continue
            kept.append(ln)
        lines = kept
        # 2. sections
        blocks = split_sections(lines)
        moved, remaining = [], []
        for head, blk in blocks:
            if head and any(re.match(p, head) for p in MOVE_HEADINGS):
                moved.append(blk)
                notes.append(f"- Moved to working record: `{head.strip()}` ({len(blk)} lines)")
            else:
                remaining.append((head, blk))
        # strip trailing '---' separators left dangling before a removed block
        out = []
        for head, blk in remaining:
            out.extend(blk)
        # collapse runs of '---' separated only by blank lines
        cleaned, i = [], 0
        while i < len(out):
            cleaned.append(out[i]); i += 1
        text = "\n".join(cleaned)
        text = re.sub(r"(\n---\n)(\s*\n---\n)+", r"\1", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        lines = text.splitlines()
        # 3. renumber '## N · ' headings
        mapping, n = {}, 0
        new = []
        for ln in lines:
            m = re.match(r"^## (\d+) · (.*)$", ln)
            if m:
                n += 1
                old = int(m.group(1))
                mapping[old] = n
                ln = f"## {n} · {m.group(2)}"
            new.append(ln)
        changed = {o: nw for o, nw in mapping.items() if o != nw}
        if changed:
            notes.append("")
            notes.append("## Section renumbering (old → new)")
            for o, nw in sorted(changed.items()):
                notes.append(f"- {o} → {nw}")
            notes.append("")
            notes.append("In-text references to the old numbers (\"section N\", \"§N\", \"Section N\") must be updated by the writer; the verifier checks them.")
        path.write_text("\n".join(new).rstrip() + "\n", encoding="utf-8")
        # 4. workings file
        title = lines[0].lstrip("# ").strip()
        wr = [f"# Working record · {title}",
              "",
              "*How this chapter was made. These sections stood in the chapter at draft 2 and were moved here, word for word, on 14 October 2026 when the book was finished. They are the record of the method: what the chapter expected against what it found, what it did to the chapters before it, the gaps it met, where it met the design system and the Decision Book, and the loose ends it flagged. Nothing here is a rule; the rules are in the register, the open choices in the decision log, the probes in `03-tests/PROBES.md`.*",
              ""]
        for blk in moved:
            wr.extend(blk)
            wr.append("")
        (WR / f"ch{num}-workings.md").write_text("\n".join(wr).rstrip() + "\n", encoding="utf-8")
        (NOTES / f"ch{num}-MOVES.md").write_text("\n".join(notes) + "\n", encoding="utf-8")
        print(f"ch{num}: moved {len(moved)} sections; renumbered {len(changed)} headings")

if __name__ == "__main__":
    main()
