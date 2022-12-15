# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['home.py'],
    pathex=[],
    binaries=[('F:\\This Semester\\Python\\Lib\\site-packages\\face_recognition_models', 'face_recognition_models')],
    datas=[('F:\\This Semester\\Python\\Projects\\Face Recognition\\giphy.gif', '.') , ('F:\\This Semester\\Python\\Projects\\Face Recognition\\temp2.png', '.') , ('F:\\This Semester\\Python\\Projects\\Face Recognition\\temp4.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='home',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='home',
)
