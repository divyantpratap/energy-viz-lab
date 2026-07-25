#!/usr/bin/env python3
"""Fetch the public dataset into data/raw (credentials never committed)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from energyviz.config import RAW_DIR, SAMPLE_DIR

print("=" * 60)
print("Energy Visualization Lab — data setup")
print("=" * 60)
print(f"Source: https://www.kaggle.com/datasets/jeanmidev/smart-meters-in-london")
print(f"Place files under: {RAW_DIR}")
print("Sample for CI already at:", SAMPLE_DIR / "sample.csv")
print("Do NOT commit raw downloads.")
RAW_DIR.mkdir(parents=True, exist_ok=True)
print("Ready. Implement provider-specific download here when credentials exist.")
