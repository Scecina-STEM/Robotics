import os
import shutil

print("Removing old instance...")
try:
    os.remove("psoa.zip")
except:
    print("Nothing to remove")
print("Zipping work...")
shutil.make_archive("psoa", 'zip', "_py")

print("Done. Running Setup...")
os.system("python3.11 psoa.zip")