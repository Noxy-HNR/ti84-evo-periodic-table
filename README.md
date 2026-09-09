# TI-84 Evo — Periodic Table Explorer

Look up any element by atomic number, symbol, or name and get its full
electron configuration, computed live from the atomic number.

Written for the **TI-84 Evo** (Texas Instruments, April 2026) running TI's
adapted CircuitPython build.

## What it does

Enter `26`, `Fe`, or `Iron` and get back:

```
------------------------------
Sym   : Fe
Name  : Iron
Z     : 26
Mass  : 55.845 amu
Val e-: 8
Config (Aufbau fill order):
  1s2 2s2 2p6 3s2 3p6 4s2 3d6
------------------------------
```

- Elements **1–118**, with symbol, name, and standard atomic mass.
- Full electron configuration in long form — no noble-gas shorthand.
- Valence electron count.
- A menu option that prints the Aufbau filling order itself.

## Configurations are computed, not stored

No electron configuration is hardcoded anywhere in this file. The filling
order is generated from the **Madelung (n+l) rule**: order subshells by
increasing `n+l`, breaking ties by increasing `n`. That reproduces exactly

```
1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p
```

which covers the table through Z=118. Electrons are then dropped into that
sequence, `2(2l+1)` per subshell.

### Aufbau exceptions

Strict Aufbau predicts chromium as `4s2 3d4`, but the measured ground state
is `4s1 3d5`. The program stores **only the atomic numbers** of the 20 known
exceptions and prints a caution flag — it never stores or prints a corrected
configuration, so the computed answer stays honest about what it is.

Lanthanides and actinides also print a note that the valence count there is
convention-dependent.

### Note on ordering

Configurations print in **filling order** (`...4s2 3d6`), not shell-sorted
order (`...3d6 4s2`), matching the Aufbau sequence above. Some textbooks
re-sort by shell.

## Calculator constraints

- Imports nothing — pure Python.
- No f-strings. TI's Python builds have rejected `f"..."` with a
  `SyntaxError`, so all formatting uses `.format()` and concatenation.
- No file I/O; the Python environment is sandboxed.
- Output is capped at 30 columns for the calculator screen.

## Transfer

Send `PTABLE.py` to the calculator with **TI Connect Evo**, then run it from
the Python App's File Manager. The filename is 6 characters — TI program
names follow the 8-character variable-name limit.

## Verification

All 118 configurations were checked programmatically: electron totals match
Z exactly, no subshell exceeds `2(2l+1)`, no impossible subshells (`2d` and
friends), no duplicate symbols, and the valence rule reproduces the group
number across the main group and d block.
