import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('start.py', base=base, shortcutName="File Speed Tester",
            shortcutDir="DesktopFolder",)
]

setup(name='File Speed Tester',
      version='0.1',
      description='File Speed Tester',
      executables=executables
      )

bdist_msi = {
    'install_icon' : 'argus-logo.png'

}

