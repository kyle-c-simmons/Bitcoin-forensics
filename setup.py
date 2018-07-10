#!/usr/bin/env python3
import cx_Freeze
from cx_Freeze import *
import sys
import matplotlib

base = None

if sys.platform == 'win32':
	base = "Win32GUI"

executables = [cx_Freeze.Executable("forensics-bitcoin-software.py", base=base)]
cx_Freeze.setup (
	name = "ForensicsBItcoinSoftware",
	options = {"build_exe": {"packages": ["tkinter", "matplotlib", "pandas", "csv", "numpy"], "include_files":["electrum-history.csv"]}},
	versionn = "1.00",
	description = "Forensics Bitcoin applicaton",
	executables = executables
	)