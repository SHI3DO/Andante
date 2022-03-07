import subprocess
import shutil
import os

if os.path.isdir('./dist'):
    shutil.rmtree('./dist')

if not os.path.isdir('./release'):
    os.mkdir('./release')
else:
    shutil.rmtree('./release')

subprocess.run('pip freeze > requirements.txt', shell=True)
subprocess.run('pyinstaller --noconfirm --onefile --windowed --icon "D:/Github/Andante/src/icon.ico" --add-data '
               '"D:/Github/Andante/src;src/"  "D:/Github/Andante/Andante.py"', shell=True)
shutil.make_archive('./release/Andante', 'zip', './dist')
print('done')
