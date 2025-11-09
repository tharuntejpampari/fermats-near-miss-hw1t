# Fermat Near Miss Finder (HW1)

Interactive search for “near misses” of the form `x^n + y^n ≈ z^n`, with
`x, y ∈ [10, k]` and `3 ≤ n ≤ 11`. Whenever a new smallest **relative miss** is found,
the program prints a labeled update; it prints the **final/best** miss last and then pauses.

## Requirements
- Python 3.10 or newer
- No third‑party libraries required

## Quick Start

### Windows (PowerShell or CMD)
```bat
./run.bat
```

### macOS / Linux
```bash
chmod +x run.sh
./run.sh
```

You will be prompted for:
- `n` (3..11 inclusive)
- `k` (>10), which sets the x,y range `[10..k]`

> **Note on runtime:** The search is `O((k-9)^2)` and uses big integers.
Large `k` will take longer. The script prints periodic progress.

## Example
```
Enter n (integer, 3 through 11 inclusive): 3
Enter k (integer > 10) limiting x,y range [10..k]: 30

Searching for near misses...
Range: x,y ∈ [10, 30], exponent n = 3
Labels: x, y, z; abs_miss = min(s - z^n, (z+1)^n - s); rel_miss = abs_miss / s

New best:
  x=10, y=10, z=12
  abs_miss=...
  rel_miss=... -> ...%

...
========= FINAL / BEST NEAR MISS =========
x=..., y=..., z=...
abs_miss=...
rel_miss=... -> ...%
(Smallest relative miss found; printed last.)
==========================================
Press Enter to exit...
```

## Building a standalone executable (optional)
If your grader requires an `.exe`, you can bundle with PyInstaller:

```bash
# from repo root
python -m venv .venv && . .venv/bin/activate  # (on Windows: .venv\Scripts\activate)
pip install --upgrade pip pyinstaller
pyinstaller --onefile --name FermatNearMiss src/near_miss.py
# Executable will be in dist/FermatNearMiss (or FermatNearMiss.exe on Windows)
```

Include the generated file under `dist/` in your GitHub repository.

## Repository Layout
```
.
├─ src/
│  └─ near_miss.py          # main program
├─ run.bat                  # Windows runner
├─ run.sh                   # macOS/Linux runner
├─ README.md
├─ LICENSE
└─ requirements.txt
```

## Academic Honesty
List any resources used in the opening comment block in `near_miss.py` and in this README.
