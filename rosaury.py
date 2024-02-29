import os
import sys
from getpass import getuser
if sys.argv[1] == "install":
    print("Valid Command")
else:
    print("Fail")
    sys.exit()
def pkgmaker():
    try:
        os.chdir(str(sys.argv[i]))
        os.system("makepkg -si")
    except:
        print("makepkg failed. Please ensure base-devel and makepkg are installed.")
    finally:
        os.chdir(str(cwd))
username = getuser()
os.chdir('/home/' + username + "/Documents")
cwd = os.getcwd()
print(sys.argv)
x = 1
for i in range(len(sys.argv)):
    if i < 2:
        i += 1
    else:
        try:
            os.system("git clone https://aur.archlinux.org/" + str(sys.argv[i]) + ".git")
            print(str(sys.argv[i] + "/PKGBUILD"))
            y = os.path.isfile(str(sys.argv[i] + "/PKGBUILD"))
            if y == True:
                print("Success")
                print(str(sys.argv[i]))
                pkgmaker()
                os.system("rm -r " + sys.argv[i])
            else:
                os.system("rm -r " + sys.argv[i])
                print("Invalid Package")
                sys.exit()
        except:
            print("Clonning failed. Please ensure git is installed.")
            sys.exit()
