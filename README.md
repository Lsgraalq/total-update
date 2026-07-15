# total-update

> **Created: September 2021** — early learning project (beginner Python practice).

A collection of small practice scripts in Python — solutions to basic programming exercises.
Each script is standalone: it reads input from `input.txt` and writes the result to `output.txt`.

## Running

Put an `input.txt` file next to the script and run it:

```bash
python a.py
```

The result will be written to `output.txt`.

## Scripts

| File    | What it does |
|---------|--------------|
| `a.py`  | Calculation task: from the dimensions of a box and coverage parameters, computes the amount of material needed (accounting for a reserve/discount) and rounds up. |
| `c.py`  | Time validation: for 5 lines of `hours minutes seconds`, prints `YES` if the time is valid (`0–23`, `0–59`, `0–59`), otherwise `NO`. |
| `d.py`  | Number processing by parity: depending on the sign and parity, prints `YES`/`NO` and the modified value. |
| `g.py`  | Sorting: reads a list of integers and prints it sorted in ascending order. |

## Input format

Each script expects its own format in `input.txt` — see how the input lines are parsed at the top of the corresponding file.

## Stack

- Python 3
