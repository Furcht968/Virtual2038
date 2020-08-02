import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32" : base = "Win32GUI"
# CUIの場合はこのif文をコメントアウトしてください。

exe = Executable(script = "Virtual2038.py", base= base)

setup(
    name = 'Virtual2038',
    version = '1.0 GA', 
    description = 'RealTime 32bit UNIX Time viewer.',
    executables = [exe]
)