# grouppyth

### Group Members

- **ANTONY SIFUNA** — COM/B/01-02365/2024
- **DENVER WALUSALA** — COM/B/01-03766/2024
- **SULEIMAN MUHAMED** — COM/B/01-05865/2024

Small Python programs: a console multiplication table and a Tkinter scientific calculator.

## Requirements

- Python 3.7+
- `tkinter` (bundled with Python on Windows/macOS; on Debian/Ubuntu: `sudo apt install python3-tk`)

## Usage

### Multiplication table

```bash
python3 multiplication_table.py
```

Prompts for the table size, then prints the n x n table from 1 to n using nested loops.

```
Enter the size of the table (e.g. 10): 5

Multiplication Table (1 to 5)
==================================================
    1    2    3    4    5
    2    4    6    8   10
    3    6    9   12   15
    4    8   12   16   20
    5   10   15   20   25
```

### Scientific calculator

```bash
python3 scientific_calc.py
```

Opens a GUI window supporting arithmetic, parentheses, `sin`/`cos`/`tan`, `√`, `x²`,
`log`, `ln`, `eˣ`, `1/x`, and `π`. Keyboard input works too: digits and operators,
`c` to clear, `BackSpace` to delete, `Enter` to evaluate.

![Scientific calculator](Screenshot%20From%202026-09-29%2007-13-45.png)
