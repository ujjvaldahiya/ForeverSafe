import cx_Freeze
from cx_Freeze import *

setup(
	name = 'ForeverSafe',
	options = {'build_exe':{'packages':['PyQt5']}},
	executables = [Executable('ForeverSafe.py')]
		)