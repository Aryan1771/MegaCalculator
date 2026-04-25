# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files


datas = [
    ("assets/megacalculator.ico", "assets"),
    ("assets/megacalculator-icon.png", "assets"),
]
datas += collect_data_files("customtkinter")


a = Analysis(
    ["src/megacalculator/__main__.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=["darkdetect"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="MegaCalculator",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="assets/megacalculator.ico",
)
