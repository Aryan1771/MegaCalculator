# MegaCalculator

MegaCalculator is a modern Python desktop calculator app with a phone-style UI.
It started as a learning project made from menu-driven calculator scripts and is
now structured like a professional Python package.

## Features

- Normal and scientific calculator modes
- Smooth phone-sized desktop window built with CustomTkinter
- Panel switcher for currency, length, weight, BMI, area, temperature, speed,
  volume, pressure, and number-system converters
- Live currency conversion using the free Frankfurter API, with cached fallback
- Refactored legacy tools: factorial, Fibonacci, primes, pi, Euler's number,
  binomial calculation, digit writer, and geometry helpers
- Tested pure calculation logic

## Run

```powershell
python -m pip install -e .[dev]
python -m megacalculator
```

You can also run the compatibility launcher:

```powershell
python main.py
```

## Test

```powershell
python -m pytest
python -m ruff check .
```

## Build Windows EXE

```powershell
python -m pip install -e .[dev,build]
python -m PyInstaller --clean MegaCalculator.spec
```

The compiled app is created at:

```text
dist/MegaCalculator.exe
```

## Project Structure

```text
assets/       App icon source, PNG, and Windows ICO files
src/megacalculator/
  core/       Pure calculator, converter, and geometry functions
  services/   Live currency service and local rate cache
  ui/         CustomTkinter desktop app
tests/        Automated tests for the reusable logic
```

## License

GPL-3.0-or-later
