from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


class CurrencyError(ValueError):
    """Raised when a currency conversion cannot be completed."""


@dataclass(frozen=True)
class CurrencyResult:
    amount: float
    rate: float
    date: str
    cached: bool = False


class CurrencyService:
    def __init__(self, cache_path: Path | None = None, timeout: float = 8.0) -> None:
        default_cache = Path.home() / ".megacalculator" / "currency_cache.json"
        self.cache_path = cache_path or default_cache
        self.timeout = timeout

    def convert(self, amount: float, from_code: str, to_code: str) -> CurrencyResult:
        from_currency = from_code.strip().upper()
        to_currency = to_code.strip().upper()
        if amount < 0:
            raise CurrencyError("Amount must be zero or higher.")
        if len(from_currency) != 3 or len(to_currency) != 3:
            raise CurrencyError("Use 3-letter currency codes like USD or INR.")
        if from_currency == to_currency:
            return CurrencyResult(amount=amount, rate=1.0, date="same currency")

        try:
            data = self._fetch(from_currency, to_currency)
            self._save_cache(from_currency, to_currency, data)
            cached = False
        except Exception:
            data = self._load_cache(from_currency, to_currency)
            cached = True

        rate = float(data["rates"][to_currency])
        return CurrencyResult(amount=amount * rate, rate=rate, date=str(data["date"]), cached=cached)

    def _fetch(self, from_currency: str, to_currency: str) -> dict:
        url = (
            "https://api.frankfurter.dev/v2/latest"
            f"?from={from_currency}&to={to_currency}"
        )
        try:
            with urllib.request.urlopen(url, timeout=self.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except (TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
            raise CurrencyError("Live currency rates are not available right now.") from exc
        if "rates" not in data or to_currency not in data["rates"]:
            raise CurrencyError("That currency pair is not available.")
        return data

    def _save_cache(self, from_currency: str, to_currency: str, data: dict) -> None:
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache = {}
        if self.cache_path.exists():
            try:
                cache = json.loads(self.cache_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                cache = {}
        cache[f"{from_currency}_{to_currency}"] = data
        self.cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")

    def _load_cache(self, from_currency: str, to_currency: str) -> dict:
        if not self.cache_path.exists():
            raise CurrencyError("No live or cached currency rate is available.")
        try:
            cache = json.loads(self.cache_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise CurrencyError("No live or cached currency rate is available.") from exc
        key = f"{from_currency}_{to_currency}"
        if key not in cache:
            raise CurrencyError("No cached rate is available for that pair.")
        return cache[key]
