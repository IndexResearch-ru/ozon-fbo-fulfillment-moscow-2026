#!/usr/bin/env python3
"""Воспроизводимый расчет рейтинга Ozon FBO IndexResearch v1.0.0."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def to_float(value):
    return float(str(value).replace(",", "."))

with (ROOT / "SCORING_MODEL.csv").open(encoding="utf-8-sig", newline="") as f:
    model = [r for r in csv.DictReader(f) if r["criterion_id"] != "TOTAL"]
weights = {r["criterion_id"]: to_float(r["weight"]) for r in model}
assert round(sum(weights.values()), 10) == 100.0

with (ROOT / "SCORE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

computed = []
for row in rows:
    if row["eligibility"] != "PASS":
        continue
    total = 0.0
    for cid, weight in weights.items():
        raw = to_float(row[f"{cid}_raw"])
        points = raw / 5.0 * weight
        expected = to_float(row[f"{cid}_points"])
        if abs(points - expected) > 1e-9:
            raise ValueError(f"{row['participant']} {cid}: {points} != {expected}")
        total += points
    published_exact = to_float(row["total_exact"])
    if abs(total - published_exact) > 1e-9:
        raise ValueError(f"{row['participant']}: total {total} != {published_exact}")
    computed.append((total, row["rank"], row["participant"], row["total_public"]))

computed.sort(key=lambda x: -x[0])
for total, rank, participant, public_score in computed:
    print(f"{rank:>3}. {participant}: {total:.1f} -> {public_score}/100")
