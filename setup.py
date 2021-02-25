import subprocess
import shutil
import os

subprocess.run("python3 -m PyInstaller --noconsole --onefile --icon=icon.ico --version-file meta_file/VersionInfoFile.txt Virtual2038.py", shell=True)
subprocess.run("python3 -m PyInstaller --noconsole --onefile --icon=icon.ico --version-file meta_file/VersionInfoFile_Config.txt Virtual2038_Config.py", shell=True)
if(os.path.exists("./dist/icons/") == True):
    shutil.rmtree("./dist/icons/")
shutil.copytree("./icons/", "./dist/icons/")
if(os.path.isfile("./dist/config.json") == True):
    os.remove("./dist/config.json")
shutil.copy("./config.json", "./dist/")
