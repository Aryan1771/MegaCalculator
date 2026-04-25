from __future__ import annotations

import tkinter as tk
from collections.abc import Callable

import customtkinter as ctk

from megacalculator.core import geometry
from megacalculator.core.calculations import (
    binomial_one_plus_x,
    digit_parts,
    euler_limit,
    evaluate_expression,
    factorial,
    fibonacci,
    pi_leibniz,
    primes,
)
from megacalculator.core.converters import (
    AREA_UNITS,
    LENGTH_UNITS,
    PRESSURE_UNITS,
    SPEED_UNITS,
    VOLUME_UNITS,
    WEIGHT_UNITS,
    calculate_bmi,
    convert_linear,
    convert_number_system,
    convert_temperature,
)
from megacalculator.resources import resource_path
from megacalculator.services.currency import CurrencyError, CurrencyService

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

PANEL_NAMES = [
    "Calculator",
    "Currency",
    "Length",
    "Weight",
    "BMI",
    "Area",
    "Temperature",
    "Speed",
    "Volume",
    "Pressure",
    "Number System",
    "Legacy Tools",
]


class MegaCalculatorApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("MegaCalculator")
        self.geometry("390x760")
        self.minsize(360, 680)
        self.maxsize(430, 820)
        self._set_window_icon()

        self.expression = ""
        self.scientific_mode = tk.BooleanVar(value=True)
        self.currency_service = CurrencyService()
        self.panels: dict[str, ctk.CTkFrame] = {}

        self.configure(fg_color="#101114")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self.container = ctk.CTkFrame(self, fg_color="#101114", corner_radius=0)
        self.container.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self._build_calculator_panel()
        self._build_converter_panels()
        self._build_legacy_panel()
        self.show_panel("Calculator")

    def _set_window_icon(self) -> None:
        icon_path = resource_path("assets/megacalculator.ico")
        if icon_path.exists():
            self.iconbitmap(str(icon_path))

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color="#101114")
        header.grid(row=0, column=0, sticky="ew", padx=14, pady=(12, 8))
        header.grid_columnconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(
            header,
            text="MegaCalculator",
            font=ctk.CTkFont(size=19, weight="bold"),
            text_color="#F7F7F8",
        )
        self.title_label.grid(row=0, column=0, sticky="w")

        self.menu = ctk.CTkOptionMenu(
            header,
            values=PANEL_NAMES,
            command=self.show_panel,
            width=136,
            height=34,
            fg_color="#20242C",
            button_color="#2D7DFF",
            button_hover_color="#4D91FF",
            dropdown_fg_color="#20242C",
        )
        self.menu.grid(row=0, column=2, padx=(8, 0), sticky="e")

    def show_panel(self, name: str) -> None:
        for panel in self.panels.values():
            panel.grid_forget()
        self.panels[name].grid(row=0, column=0, sticky="nsew")
        self.menu.set(name)
        self.title_label.configure(text=name)

    def _panel(self, name: str) -> ctk.CTkFrame:
        frame = ctk.CTkFrame(self.container, fg_color="#15171C", corner_radius=28)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        self.panels[name] = frame
        return frame

    def _build_calculator_panel(self) -> None:
        panel = self._panel("Calculator")
        panel.grid_rowconfigure(2, weight=1)

        display = ctk.CTkFrame(panel, fg_color="#15171C", corner_radius=24)
        display.grid(row=0, column=0, sticky="ew", padx=18, pady=(18, 6))
        display.grid_columnconfigure(0, weight=1)

        self.expression_label = ctk.CTkLabel(
            display,
            text="",
            anchor="e",
            font=ctk.CTkFont(size=22),
            text_color="#A8ADB8",
            height=42,
        )
        self.expression_label.grid(row=0, column=0, sticky="ew")
        self.result_label = ctk.CTkLabel(
            display,
            text="0",
            anchor="e",
            font=ctk.CTkFont(size=46, weight="bold"),
            text_color="#F7F7F8",
            height=70,
        )
        self.result_label.grid(row=1, column=0, sticky="ew")

        toolbar = ctk.CTkFrame(panel, fg_color="#15171C")
        toolbar.grid(row=1, column=0, sticky="ew", padx=18, pady=(0, 8))
        toolbar.grid_columnconfigure(1, weight=1)

        ctk.CTkSwitch(
            toolbar,
            text="Scientific",
            variable=self.scientific_mode,
            command=self._refresh_keypad,
            progress_color="#2D7DFF",
            button_color="#F7F7F8",
        ).grid(row=0, column=0, sticky="w")
        ctk.CTkButton(
            toolbar,
            text="History",
            width=86,
            height=32,
            fg_color="#20242C",
            hover_color="#2B303A",
            command=self._show_history,
        ).grid(row=0, column=2, sticky="e")

        self.keypad = ctk.CTkFrame(panel, fg_color="#15171C")
        self.keypad.grid(row=2, column=0, sticky="nsew", padx=14, pady=(0, 18))
        self._history: list[str] = []
        self._refresh_keypad()

    def _refresh_keypad(self) -> None:
        for child in self.keypad.winfo_children():
            child.destroy()
        for column in range(4):
            self.keypad.grid_columnconfigure(column, weight=1, uniform="keys")

        normal_rows = [
            ["AC", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
        ]
        scientific_rows = [
            ["sin(", "cos(", "tan(", "^"],
            ["sqrt(", "log(", "ln(", "π"],
            ["(", ")", "e", "//"],
        ]
        rows = scientific_rows + normal_rows if self.scientific_mode.get() else normal_rows
        for row_index, row in enumerate(rows):
            self.keypad.grid_rowconfigure(row_index, weight=1, uniform="keys")
            for column_index, label in enumerate(row):
                self._key_button(label).grid(
                    row=row_index,
                    column=column_index,
                    sticky="nsew",
                    padx=5,
                    pady=5,
                )

    def _key_button(self, label: str) -> ctk.CTkButton:
        operators = {"+", "-", "×", "÷", "=", "^", "//"}
        utility = {"AC", "⌫", "%", "±"}
        if label in operators:
            color, hover = "#FF9F0A", "#FFB13B"
        elif label in utility:
            color, hover = "#5D6675", "#727C8E"
        else:
            color, hover = "#252932", "#323845"
        return ctk.CTkButton(
            self.keypad,
            text=label,
            font=ctk.CTkFont(size=18, weight="bold"),
            corner_radius=18,
            fg_color=color,
            hover_color=hover,
            text_color="#FFFFFF",
            command=lambda value=label: self._press(value),
        )

    def _press(self, value: str) -> None:
        if value == "AC":
            self.expression = ""
            self._set_result("0")
        elif value == "⌫":
            self.expression = self.expression[:-1]
        elif value == "=":
            self._calculate()
            return
        elif value == "±":
            self.expression = f"-({self.expression})" if self.expression else "-"
        elif value == "π":
            self.expression += "pi"
        elif value == "e":
            self.expression += "e"
        else:
            self.expression += value
        self.expression_label.configure(text=self.expression)

    def _calculate(self) -> None:
        try:
            result = evaluate_expression(self.expression)
        except ValueError as exc:
            self._set_result(str(exc))
            return
        formatted = format_number(result)
        self._history.insert(0, f"{self.expression} = {formatted}")
        self._history = self._history[:8]
        self.expression = formatted
        self.expression_label.configure(text=self.expression)
        self._set_result(formatted)

    def _set_result(self, text: str) -> None:
        self.result_label.configure(text=text)

    def _show_history(self) -> None:
        content = "\n".join(self._history) if self._history else "No history yet."
        self._set_result(content)

    def _build_converter_panels(self) -> None:
        self._currency_panel()
        self._linear_panel("Length", LENGTH_UNITS)
        self._linear_panel("Weight", WEIGHT_UNITS)
        self._bmi_panel()
        self._linear_panel("Area", AREA_UNITS)
        self._temperature_panel()
        self._linear_panel("Speed", SPEED_UNITS)
        self._linear_panel("Volume", VOLUME_UNITS)
        self._linear_panel("Pressure", PRESSURE_UNITS)
        self._number_system_panel()

    def _base_form(self, name: str) -> tuple[ctk.CTkFrame, ctk.CTkFrame, ctk.CTkLabel]:
        panel = self._panel(name)
        content = ctk.CTkFrame(panel, fg_color="#15171C")
        content.grid(row=0, column=0, sticky="nsew", padx=18, pady=18)
        content.grid_columnconfigure(0, weight=1)
        result = ctk.CTkLabel(
            content,
            text="0",
            height=84,
            fg_color="#101114",
            corner_radius=18,
            font=ctk.CTkFont(size=25, weight="bold"),
            text_color="#F7F7F8",
        )
        result.grid(row=99, column=0, sticky="ew", pady=(14, 0))
        return panel, content, result

    def _entry(self, parent: ctk.CTkFrame, row: int, placeholder: str) -> ctk.CTkEntry:
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder, height=46, corner_radius=14)
        entry.grid(row=row, column=0, sticky="ew", pady=6)
        return entry

    def _option(
        self,
        parent: ctk.CTkFrame,
        row: int,
        values: list[str],
        default: str | None = None,
    ) -> ctk.CTkOptionMenu:
        option = ctk.CTkOptionMenu(parent, values=values, height=42, corner_radius=14)
        option.set(default or values[0])
        option.grid(row=row, column=0, sticky="ew", pady=6)
        return option

    def _action(
        self,
        parent: ctk.CTkFrame,
        row: int,
        text: str,
        command: Callable[[], None],
    ) -> None:
        ctk.CTkButton(
            parent,
            text=text,
            height=46,
            corner_radius=16,
            fg_color="#2D7DFF",
            hover_color="#4D91FF",
            command=command,
        ).grid(row=row, column=0, sticky="ew", pady=(10, 6))

    def _currency_panel(self) -> None:
        _, content, result = self._base_form("Currency")
        amount = self._entry(content, 0, "Amount")
        from_code = self._entry(content, 1, "From currency, e.g. USD")
        to_code = self._entry(content, 2, "To currency, e.g. INR")

        def convert() -> None:
            result.configure(text="Loading live rate...")
            self.update_idletasks()
            try:
                converted = self.currency_service.convert(
                    float(amount.get()),
                    from_code.get(),
                    to_code.get(),
                )
                suffix = " cached" if converted.cached else ""
                result.configure(
                    text=f"{format_number(converted.amount)}\nrate {converted.rate:g}\n{converted.date}{suffix}"
                )
            except (ValueError, CurrencyError) as exc:
                result.configure(text=str(exc))

        self._action(content, 3, "Convert Currency", convert)

    def _linear_panel(self, name: str, units: dict) -> None:
        _, content, result = self._base_form(name)
        amount = self._entry(content, 0, "Value")
        values = list(units)
        from_unit = self._option(content, 1, values)
        to_unit = self._option(content, 2, values, values[min(1, len(values) - 1)])

        def convert() -> None:
            try:
                value = convert_linear(float(amount.get()), from_unit.get(), to_unit.get(), units)
                result.configure(text=f"{format_number(value)}\n{to_unit.get()}")
            except ValueError as exc:
                result.configure(text=str(exc))

        self._action(content, 3, f"Convert {name}", convert)

    def _temperature_panel(self) -> None:
        _, content, result = self._base_form("Temperature")
        amount = self._entry(content, 0, "Temperature")
        values = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = self._option(content, 1, values)
        to_unit = self._option(content, 2, values, "Fahrenheit")

        def convert() -> None:
            try:
                value = convert_temperature(float(amount.get()), from_unit.get(), to_unit.get())
                result.configure(text=f"{format_number(value)}\n{to_unit.get()}")
            except ValueError as exc:
                result.configure(text=str(exc))

        self._action(content, 3, "Convert Temperature", convert)

    def _bmi_panel(self) -> None:
        _, content, result = self._base_form("BMI")
        weight = self._entry(content, 0, "Weight in kg")
        height = self._entry(content, 1, "Height in cm")

        def calculate() -> None:
            try:
                bmi, label = calculate_bmi(float(weight.get()), float(height.get()))
                result.configure(text=f"{bmi:.1f}\n{label}")
            except ValueError as exc:
                result.configure(text=str(exc))

        self._action(content, 2, "Calculate BMI", calculate)

    def _number_system_panel(self) -> None:
        _, content, result = self._base_form("Number System")
        value = self._entry(content, 0, "Number")
        labels = ["Binary", "Octal", "Decimal", "Hexadecimal"]
        bases = {"Binary": 2, "Octal": 8, "Decimal": 10, "Hexadecimal": 16}
        from_base = self._option(content, 1, labels, "Decimal")
        to_base = self._option(content, 2, labels, "Binary")

        def convert() -> None:
            try:
                converted = convert_number_system(
                    value.get(),
                    bases[from_base.get()],
                    bases[to_base.get()],
                )
                result.configure(text=converted)
            except ValueError as exc:
                result.configure(text=str(exc))

        self._action(content, 3, "Convert Number", convert)

    def _build_legacy_panel(self) -> None:
        _, content, result = self._base_form("Legacy Tools")
        tools = [
            "Factorial",
            "Fibonacci",
            "Primes",
            "Pi Approximation",
            "Euler Approximation",
            "Binomial (1+x)^n",
            "Digit Writer",
            "Circle Area",
            "Cube Volume",
        ]
        tool = self._option(content, 0, tools)
        first = self._entry(content, 1, "First value")
        second = self._entry(content, 2, "Second value when needed")

        def run_tool() -> None:
            try:
                selected = tool.get()
                if selected == "Factorial":
                    output = factorial(int(first.get()))
                elif selected == "Fibonacci":
                    output = ", ".join(map(str, fibonacci(int(first.get()))))
                elif selected == "Primes":
                    output = ", ".join(map(str, primes(int(first.get()))))
                elif selected == "Pi Approximation":
                    output = pi_leibniz(int(first.get() or "10000"))
                elif selected == "Euler Approximation":
                    output = euler_limit(int(first.get()))
                elif selected == "Binomial (1+x)^n":
                    output = binomial_one_plus_x(float(first.get()), int(second.get()))
                elif selected == "Digit Writer":
                    output = ", ".join(map(str, digit_parts(int(first.get()))))
                elif selected == "Circle Area":
                    output = geometry.circle_area(float(first.get()))
                else:
                    output = geometry.cube_volume(float(first.get()))
                result.configure(text=str(output))
            except ValueError as exc:
                result.configure(text=str(exc))

        self._action(content, 3, "Run Tool", run_tool)


def format_number(value: float) -> str:
    if abs(value - round(value)) < 1e-12:
        return str(int(round(value)))
    return f"{value:.10g}"
