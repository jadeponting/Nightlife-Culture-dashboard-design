#!/usr/bin/env python3
"""Build the rule register (06-register/) from the Chapter 16 compilation and the chapters.

Stage 1 (this script, `parse`): read 02-research-notes/ch16-assembly.md Part 1.1 (the 486 rows as
printed, with chapter, row and file line) and Part 1.3 (the 42 duplicate groups), plus Chapter 16's
own rules table, and write 06-register/work/rows.csv and groups.csv.

Stage 2 (`build`): merge the classification files the agents returned (work/classified-*.csv — one
line per row with the re-based tier, open part, test form, check, record section, kind fields and
status) and the group decisions (work/groups-decided.csv) into rule-register.csv and
rule-register.md, one register rule per group and one per ungrouped row, with DD-nnn identifiers.

Run from the repo root:
    python3 06-register/build_register.py parse
    python3 06-register/build_register.py build
"""
import csv, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if (HERE.parent / "02-research-notes").exists() else HERE  # repo layout, or a flat working folder
def _p(sub, name):
    return (ROOT / sub / name) if (ROOT / sub).exists() else (ROOT / name)
ASSEMBLY = _p("02-research-notes", "ch16-assembly.md")
CH16 = _p("04-chapters", "ch16-breaking-these-rules-well.md")
REG = (ROOT / "06-register") if (ROOT / "02-research-notes").exists() else (ROOT / "register")
WORK = REG / "work"
OUT_CSV = REG / "rule-register.csv"
OUT_MD = REG / "rule-register.md"


def cells(line):
    parts = line.strip().strip("|").split("|")
    return [p.strip() for p in parts]


def parse():
    text = ASSEMBLY.read_text().splitlines()
    rows = []
    in_table = False
    for ln in text:
        if ln.startswith("| Ch | # | L | Rule | Why | Kind | Tier | Source | Sense [added] |"):
            in_table = True; continue
        if in_table:
            if not ln.startswith("|"):
                if rows: break
                continue
            c = cells(ln)
            if c[0].startswith("---") or c[0] == "Ch":
                continue
            if len(c) < 9:
                continue
            rows.append({"id": f"{c[0]}.{c[1]}", "ch": c[0], "n": c[1], "L": c[2], "rule": c[3], "why": c[4],
                         "kind": c[5], "tier": c[6], "source": c[7], "sense": c[8]})
    assert len(rows) == 486, len(rows)
    # Chapter 16's own table
    ch16 = CH16.read_text().splitlines()
    start = next(i for i, l in enumerate(ch16) if l.strip() == "## The rules")
    n = 0
    for i in range(start + 1, len(ch16)):
        l = ch16[i]
        if l.startswith("## ") and i > start + 1:
            break
        if l.startswith("|") and not l.startswith("| Rule |") and not l.startswith("|---"):
            c = cells(l)
            if len(c) >= 5:
                n += 1
                rows.append({"id": f"16.{n}", "ch": "16", "n": str(n), "L": str(i + 1), "rule": c[0], "why": c[1],
                             "kind": c[2], "tier": c[3], "source": c[4], "sense": ""})
    # groups
    groups = []
    g = None
    for ln in text:
        m = re.match(r"\*\*D(\d+) · (.+)\*\*", ln)
        if m:
            g = {"group": f"D{m.group(1)}", "title": m.group(2), "rows": []}
            groups.append(g); continue
        if g is not None and ln.startswith("| ") and re.match(r"\| \d+\.\d+ \|", ln):
            g["rows"].append(cells(ln)[0])
        if ln.startswith("## PART 2"):
            break
    WORK.mkdir(parents=True, exist_ok=True)
    with open(WORK / "rows.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(WORK / "groups.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["group", "title", "rows"])
        for g in groups:
            w.writerow([g["group"], g["title"], ";".join(g["rows"])])
    print("rows", len(rows), "groups", len(groups), "grouped rows", sum(len(g["rows"]) for g in groups))


TIER_ORDER = ["Fixed (requirement)", "Fixed (sequence)", "Adaptable (house default)", "Adaptable", "Decorative",
              "Statement of the record", "— (disputed; open in the decision log)"]


def build():
    rows = {r["id"]: r for r in csv.DictReader(open(WORK / "rows.csv"))}
    cls = {}
    for p in sorted(WORK.glob("classified-*.csv")):
        for r in csv.DictReader(open(p)):
            cls[r["id"].strip()] = r
    missing = [i for i in rows if i not in cls]
    if missing:
        print("unclassified rows:", len(missing), missing[:20])
    groups = list(csv.DictReader(open(WORK / "groups.csv")))
    decided = {r["group"]: r for r in csv.DictReader(open(WORK / "groups-decided.csv"))}
    # splits decided by the orchestrator after the group agent's pass (Chapter 16 §7's two- and three-rule groups)
    splits_path = WORK / "group-splits.csv"
    if splits_path.exists():
        for sp in csv.DictReader(open(splits_path)):
            moved = set(sp["rows"].split(";"))
            for g in groups:  # a moved row leaves every other group
                g["rows"] = ";".join(m for m in g["rows"].split(";") if m not in moved)
            idx = next(i for i, g in enumerate(groups) if g["group"] == sp["parent"])
            groups.insert(idx + 1, {"group": sp["new_group"], "title": sp["title"], "rows": sp["rows"]})
            decided[sp["new_group"]] = {"group": sp["new_group"], "canonical_row": sp["canonical_row"],
                                        "rule_wording": "", "tier": sp["tier"], "open_part": sp["open_part"],
                                        "reason": sp["reason"], "status": sp["status"], "notes": sp["notes"]}
    used = set()
    register = []
    by_canon = {}
    # grouped rules first, in group order, then ungrouped rows in chapter order
    for g in groups:
        d = decided.get(g["group"])
        members = [m for m in g["rows"].split(";") if m in rows]
        if d is None or not members or d.get("tier", "").strip() == "split":
            continue  # D42: the residual rows stay as their own
        canon = d["canonical_row"].strip()
        if canon in by_canon:  # two groups resolving to one wording (D1 and D2) are one register rule
            prev = by_canon[canon]
            extra = [m for m in members if m not in used]
            if extra:
                prev["chapters"] += "; " + "; ".join(extra)
                prev["all_sources"] += " || " + " || ".join(rows[m]["source"] for m in extra)
                prev["group"] += "+" + g["group"]
                used.update(extra)
            continue
        members = [m for m in members if m not in used]
        if not members:
            continue  # every row of this group is already placed by an earlier group (D39's two rows sit in D1 and D12)
        if canon not in members:
            canon = members[0]
        c = cls.get(canon) or cls.get(members[0]) or {}
        base = rows.get(canon) or rows[members[0]]
        by_canon[canon] = entry = dict(
            group=g["group"], title=g["title"], rule=base["rule"].strip(),
            tier=(d.get("tier") or c.get("tier_rebased", "")).strip(), open_part=(d.get("open_part") or c.get("open_part", "")).strip(),
            reason=(d.get("reason") or c.get("reason", "")).strip(),
            kind=c.get("kind_main", base["kind"]), subkind=c.get("standard_subkind", ""), binds=c.get("binds", ""),
            sources=base["source"], all_sources=" || ".join(rows[m]["source"] for m in members),
            chapters="; ".join(members), test=c.get("test_form", ""), check=c.get("check", ""),
            record=c.get("record_section", ""), status=(d.get("status") or c.get("status", "current")).strip(),
            why=base["why"], notes=(d.get("notes", "") or "").strip())
        register.append(entry)
        used.update(members)
    for rid, r in rows.items():
        if rid in used:
            continue
        c = cls.get(rid, {})
        register.append(dict(
            group="", title="", rule=r["rule"], tier=c.get("tier_rebased", ""), open_part=c.get("open_part", ""),
            reason=c.get("reason", ""), kind=c.get("kind_main", r["kind"]), subkind=c.get("standard_subkind", ""),
            binds=c.get("binds", ""), sources=r["source"], chapters=rid, test=c.get("test_form", ""),
            check=c.get("check", ""), record=c.get("record_section", ""), status=c.get("status", "current"), why=r["why"],
            notes=c.get("notes", ""), all_sources=r["source"]))
    def dag(ids):
        return any("†" in rows[m]["source"] or "†" in rows[m]["kind"] for m in ids if m in rows)
    SEC8 = {"DD-001": "Chapter 16 §8 row 1", "DD-002": "Chapter 16 §8 row 2 (the crop rule)", "DD-003": "Chapter 16 §8 row 3 (the interval rule)",
            "DD-004": "Chapter 16 §8 row 4 (uncertainty)", "DD-005": "Chapter 16 §8 row 5 (recognition)", "DD-006": "Chapter 16 §8 row 6 (construct before proxy)",
            "DD-007": "Chapter 16 §8 row 7 (the retirement plan)", "DD-008": "Chapter 16 §8 row 8 (the headline)", "DD-009": "Chapter 16 §8 row 9 (text inside the frame)",
            "DD-010": "Chapter 16 §8 row 10 (the withheld cell's kind)"}
    merged = []
    seen_wording = {}
    for r in register:
        # the status value "awaiting Carly" was retired on 14 October 2026; the classification files may still carry it
        for k in ("status", "open_part", "tier", "notes", "reason"):
            if r.get(k):
                r[k] = r[k].replace("awaiting Carly", "open in the decision log").replace("until Carly decides", "until the decision log settles it")
        ids = [x.strip() for x in r["chapters"].split(";")]
        if dag(ids) and "full text not read" not in r["status"]:
            r["status"] = (r["status"] + "; full text not read").strip("; ")
        if r["open_part"] and not re.search(r"Adaptable|Fixed|awaiting|open in the decision log|Decorative|requirement", r["open_part"]):
            r["open_part"] += ": Adaptable"
        if "open in the decision log" in r["open_part"] and "open in the decision log" not in r["status"]:
            r["status"] = (r["status"] + "; open in the decision log").strip("; ")
        for k in ("reason", "notes", "open_part"):
            r[k] = re.sub(r"DD-0(0[1-9]|10)\b", lambda m: SEC8["DD-0" + m.group(1)], r.get(k, ""))
        key = r["rule"].strip().lower()
        if key in seen_wording:  # the same wording printed by two chapters (the residual Decorative rows)
            prev = seen_wording[key]
            prev["chapters"] += "; " + r["chapters"]; prev["all_sources"] += " || " + r["all_sources"]
            continue
        seen_wording[key] = r; merged.append(r)
    register = merged
    statements = [r for r in register if r["tier"] == "Statement of the record"]
    register = [r for r in register if r["tier"] != "Statement of the record"]
    for i, r in enumerate(register, 1):
        r["id"] = f"DD-{i:03d}"
    for i, r in enumerate(statements, 1):
        r["id"] = f"DS-{i:03d}"
    fields = ["id", "rule", "tier", "open_part", "reason", "kind", "subkind", "binds", "sources", "chapters", "test",
              "check", "record", "status", "cited_by", "group", "title", "why", "notes", "all_sources"]
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in register + statements:
            r.setdefault("cited_by", "")
            w.writerow({k: r.get(k, "") for k in fields})
    # counts
    from collections import Counter
    tiers = Counter(r["tier"] for r in register)
    md = ["# The rule register", "",
          "*Generated from `02-research-notes/ch16-assembly.md` Part 1 and Chapter 16's rules table by `06-register/build_register.py`; "
          "the classification files in `06-register/work/` carry each row's re-basing with its reason. Do not edit by hand — edit a chapter, "
          "or a classification row, and regenerate. One register rule per duplicate group (Chapter 16 §7; the compilation's D-groups) and one per "
          "ungrouped row; `chapters` lists every source row as chapter.row. Tiers in Chapter 16 §3's senses. `cited by` is filled by the build.*", "",
          f"**{len(register)} register rules** from {len(rows)} source rows ({len(statements)} statement{'s' if len(statements)!=1 else ''} of the record listed apart). "
          f"Fixed in either sense: {sum(r['tier'].startswith('Fixed') for r in register)} ({100*sum(r['tier'].startswith('Fixed') for r in register)//len(register)} per cent) — Chapter 16 §3 estimated about two hundred before the file was built; the estimate is not confirmed, and the share is the Decision Book's own 74 per cent, because most of the 212 unmarked Fixed rows and the 102 procedures proved to be checks the build can run. By tier: " + "; ".join(f"{k} {v}" for k, v in sorted(tiers.items(), key=lambda kv: (TIER_ORDER.index(kv[0]) if kv[0] in TIER_ORDER else 99))) + ".", "",
          "| ID | Rule (stated once) | Tier · open part | Kind | Source of the stated row | Chapter rows (all statements) | Test · check | Record | Status |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in register:
        tier = r["tier"] + (f" · {r['open_part']}" if r["open_part"] else "")
        kind = r["kind"] + (f" ({r['subkind']})" if r["subkind"] else "") + (f" [{r['binds']}]" if r["binds"] else "")
        test = r["test"] + (f" · {r['check']}" if r["check"] else "")
        md.append(f"| {r['id']} | {r['rule']} | {tier} | {kind} | {r['sources']} | {r['chapters']} | {test} | {r['record']} | {r['status']} |")
    if statements:
        md += ["", "## Statements of the record, listed apart", "",
               "*Rows the chapters printed as rules that are findings (Chapter 16 §3's third sense). Not rules; the register points at them.*", "",
               "| ID | Statement | Kind | Source | Chapter rows |", "|---|---|---|---|---|"]
        for r in statements:
            md.append(f"| {r['id']} | {r['rule']} | {r['kind']} | {r['sources']} | {r['chapters']} |")
    OUT_MD.write_text("\n".join(md) + "\n")
    print("register rules", len(register), dict(tiers))


if __name__ == "__main__":
    {"parse": parse, "build": build}[sys.argv[1]]()
