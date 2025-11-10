#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program Title: Looking for Fermat's Last Theorem Near Misses
Source Filename: src/near_miss.py
External Files Required: none
External Files Created: none
Programmer(s): <Your Name Here>, <Partner Name Here>
Email(s): <you@example.com>, <partner@example.com>
Course & Section: <Course Number> - <Section>
Completion/Submission Date: 2025-11-09
Language & Version: Python 3.10+
How to Run (brief): Run via run.bat (Windows) or run.sh (macOS/Linux) or `python src/near_miss.py`.
Program Description:
    Interactive program to search for "near misses" in the Diophantine expression x^n + y^n ≈ z^n
    for integers x, y in [10, k], with 3 ≤ n ≤ 11. For each (x, y), it finds the integer z such that
    z^n ≤ s < (z+1)^n where s = x^n + y^n, reports the smaller absolute miss, and tracks the smallest
    relative miss across the search. Whenever a new global best is found, it prints a labeled update,
    and prints the final best at the end. The program pauses for review before exiting.
Resources Used:
    - Python documentation on big integers and the decimal module.
    - Integer nth-root method (binary search) is a standard technique for exact integer roots.
"""

from __future__ import annotations
from decimal import Decimal, getcontext

# Set high precision for relative miss ratios when numbers are very large.
getcontext().prec = 50

def int_nth_root(value: int, n: int) -> int:
    """Return floor(value ** (1/n)) using integer arithmetic (binary search).
    Assumes value >= 0 and n >= 2.
    """
    if value < 2:
        return value
    # Exponential bound then binary search
    hi = 1 << ((value.bit_length() + n - 1) // n + 1)
    lo = 0
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        p = mid ** n
        if p == value:
            return mid
        if p < value:
            lo = mid
        else:
            hi = mid
    return lo

def prompt_int(prompt: str, validate):
    """Prompt until validate(value) returns (ok, err)."""
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input: please enter an integer.")
            continue
        ok, err = validate(val)
        if ok:
            return val
        print(err)

def search_near_misses(n: int, k: int):
    """Exhaustive search for x,y in [10,k] reporting new best relative misses as found."""
    best = None  # (rel_miss, abs_miss, x, y, z, s, zn, z1n)
    total_pairs = (k - 9) * (k - 9)
    processed = 0

    print("\nSearching for near misses...")
    print(f"Range: x,y ∈ [10, {k}], exponent n = {n}")
    print("Labels: x, y, z; abs_miss = min(s - z^n, (z+1)^n - s); rel_miss = abs_miss / s\n")

    for x in range(10, k + 1):
        # Loop intent: iterate y for a given x and evaluate s = x^n + y^n
        for y in range(10, k + 1):
            s = (x ** n) + (y ** n)
            z = int_nth_root(s, n)  # z^n <= s < (z+1)^n
            zn = z ** n
            z1n = (z + 1) ** n
            abs_miss_lower = s - zn
            abs_miss_upper = z1n - s
            abs_miss = abs_miss_lower if abs_miss_lower <= abs_miss_upper else abs_miss_upper
            rel_miss = Decimal(abs_miss) / Decimal(s)

            if best is None or rel_miss < best[0]:
                best = (rel_miss, abs_miss, x, y, z, s, zn, z1n)
                print("New best:")
                print(f"  x={x}, y={y}, z={z}")
                print(f"  abs_miss={abs_miss}")
                print(f"  rel_miss={rel_miss}  -> {rel_miss * Decimal(100)}%\n")

            processed += 1
            # Optional lightweight progress indicator (about 5% increments)
            step = max(1, total_pairs // 20)
            if processed % step == 0:
                pct = (processed * 100) // total_pairs
                print(f"Progress: {pct}% ({processed}/{total_pairs})")

    return best

def main():
    # Input prompts with validation (each declaration's purpose is clear by name).
    print("Fermat Near Miss Finder")
    print("------------------------")
    n = prompt_int(
        "Enter n (integer, 3 through 11 inclusive): ",
        lambda v: (3 <= v <= 11, "n must be an integer between 3 and 11 (inclusive).")
    )
    k = prompt_int(
        "Enter k (integer > 10) limiting x,y range [10..k]: ",
        lambda v: (v > 10, "k must be an integer greater than 10.")
    )

    best = search_near_misses(n, k)

    if best is None:
        print("No pairs processed.")
    else:
        rel_miss, abs_miss, x, y, z, s, zn, z1n = best
        print("\n========= FINAL / BEST NEAR MISS =========")
        print(f"x={x}, y={y}, z={z}")
        print(f"abs_miss={abs_miss}")
        print(f"rel_miss={rel_miss}  -> {rel_miss * Decimal(100)}% ")
        print("(Smallest relative miss found; printed last.)")
        print("==========================================\n")

    # Pause so user can review output (especially when launched via double-click)
    try:
        input("Press Enter to exit...")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
