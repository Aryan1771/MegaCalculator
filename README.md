# MegaCalculator

MegaCalculator is a Python desktop calculator built with CustomTkinter. It combines a phone-style scientific calculator, unit converters, currency conversion, legacy math tools, automated tests, and a Windows executable build configuration.

## Features

- Normal and scientific calculator modes
- Phone-sized desktop UI built with CustomTkinter
- Currency, length, weight, BMI, area, temperature, speed, volume, pressure, and number-system converters
- Live currency conversion through the Frankfurter API
- Cached currency fallback for offline or failed API requests
- Legacy tools for factorials, Fibonacci numbers, primes, pi, Euler's number, binomial expansion, digit writing, and geometry helpers
- Reusable package layout under `src/`
- Test suite for calculation, conversion, currency, geometry, and UI smoke behavior
- Ruff linting configuration
- PyInstaller spec for building a Windows executable

## Tech Stack

- Python 3.13+
- CustomTkinter
- pytest
- ruff
- PyInstaller

## Project Structure

```text
assets/                         Application icons
src/megacalculator/
  core/                         Pure calculation, converter, and geometry logic
  services/                     Currency service and rate cache
  ui/                           CustomTkinter desktop interface
tests/                          Automated tests
main.py                         Compatibility launcher
MegaCalculator.spec             Windows executable build config
pyproject.toml                  Package, dependency, test, and lint configuration
```

## Getting Started

Python 3.13+ and a working Tk installation are required. Run `python -m tkinter` to check Tk availability. Create and activate a virtual environment before installing dependencies.

### Install in development mode

```powershell
python -m pip install -e ".[dev]"
```

### Run the app

```powershell
python -m megacalculator
```

You can also run the compatibility launcher:

```powershell
python main.py
```

## Testing and Linting

Run the test suite:

```powershell
python -m pytest
```

Run lint checks:

```powershell
python -m ruff check .
```

## Build a Windows Executable

Install build dependencies:

```powershell
python -m pip install -e ".[dev,build]"
```

Build with PyInstaller:

```powershell
python -m PyInstaller --clean MegaCalculator.spec
```

The executable is created at:

```text
dist/MegaCalculator.exe
```

## Currency data

Currency conversion depends on provider availability. Cached rates may be older than the latest published rates; inspect the rate date before relying on a conversion.

## License

This repository is licensed under the GPL-3.0 license. See `LICENSE` for details.
