import json
import urllib.error

import pytest

from megacalculator.services.currency import CurrencyError, CurrencyService


def test_currency_live_success_is_cached(monkeypatch, tmp_path) -> None:
    service = CurrencyService(tmp_path / "rates.json")

    monkeypatch.setattr(
        service,
        "_fetch",
        lambda _from_code, to_code: {"date": "2026-04-25", "rates": {to_code: 83.0}},
    )

    result = service.convert(2, "USD", "INR")

    assert result.amount == 166
    assert not result.cached
    assert json.loads((tmp_path / "rates.json").read_text())["USD_INR"]["rates"]["INR"] == 83.0


def test_currency_uses_cache_when_live_fetch_fails(monkeypatch, tmp_path) -> None:
    cache = tmp_path / "rates.json"
    cache.write_text(json.dumps({"USD_INR": {"date": "cached", "rates": {"INR": 80}}}))
    service = CurrencyService(cache)

    def fail(*_args):
        raise CurrencyError("offline")

    monkeypatch.setattr(service, "_fetch", fail)

    result = service.convert(3, "USD", "INR")

    assert result.amount == 240
    assert result.cached


def test_currency_without_live_or_cache_raises(monkeypatch, tmp_path) -> None:
    service = CurrencyService(tmp_path / "missing.json")

    def fail(*_args):
        raise urllib.error.URLError("offline")

    monkeypatch.setattr(service, "_fetch", fail)

    with pytest.raises(CurrencyError):
        service.convert(1, "USD", "INR")
