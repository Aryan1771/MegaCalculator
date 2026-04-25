import os

import pytest


@pytest.mark.skipif(os.environ.get("DISPLAY") is None and os.name != "nt", reason="No UI display")
def test_app_can_switch_panels() -> None:
    from megacalculator.ui.app import MegaCalculatorApp

    app = MegaCalculatorApp()
    app.update_idletasks()
    app.show_panel("Length")
    app.show_panel("Calculator")
    app.destroy()
