# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ForeverSafe.py'],
             pathex=['C:\\Users\\Dahiya\\Desktop\\ForeverSafe'],
             binaries=[],
             datas = [('C:\\Users\\Dahiya\\Desktop\\ForeverSafe\\logo_transparent.png','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ForeverSafe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
