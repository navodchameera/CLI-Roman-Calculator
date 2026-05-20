# CLI Roman Calculator

A command-line calculator that works entirely in Roman Numerals. Perform arithmetic operations and convert Roman Numerals to integers — all from your terminal.

## Features

- Add, subtract, multiply, and divide Roman Numerals
- Convert a Roman Numeral to its integer value
- Handles both uppercase and lowercase input (e.g. `XIV` or `xiv`)
- Validates that results stay within the Roman Numeral range (1–3999)

## Usage

Run the script with Python:

```bash
python roman_calculator.py
```

You'll be prompted to enter a Roman Numeral, then choose an operator:

```
Enter a Roman Numeral between 0 and 4000 : X

Enter Operator
X +
```

### Supported Operators

| Operator | Action |
|----------|--------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `t` | Convert to integer |

### Example

```
Enter a Roman Numeral between 0 and 4000 : XX
Enter Operator
XX + 
Enter a Roman Numeral between 0 and 4000 : V
XX + V = XXV
```

```
Enter a Roman Numeral between 0 and 4000 : XIV
Enter Operator
XIV t
14
```

## Roman Numeral Reference

| Symbol | Value |
|--------|-------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

> Valid range: **I (1)** to **MMMCMXCIX (3999)**. Results outside this range will display an error.

## Requirements

- Python 3.x
- No external libraries needed
