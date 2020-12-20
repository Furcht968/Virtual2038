import sys,os,shutil
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32" : base = "Win32GUI"
# CUIの場合はこのif文をコメントアウトしてください。

exe = Executable(script = "Virtual2038.py", base= base, icon="icon.ico")

setup(
    name = 'Virtual2038',
    version = '2.1 GA', 
    description = 'RealTime 32bit UNIX Time viewer.',
    executables = [exe]
)


shutil.copy("./icon.png", "build/" + os.listdir("./build/")[0]+"/")