import os
import subprocess
from datetime import datetime

orgPath = os.getcwd()
print(orgPath)

result = os.system("adb wait-for-device")
print("result as {}".format(result))
'''
os.chdir("d:\works")
#os.makedirs("PythonTest\\abc")
dirList = os.listdir()

for cur in dirList:
    os.chdir(cur)
    subprocess.run("dir", shell = True)
    os.chdir("..")

'''
#
'''
os.chdir(orgPath)
#os.rename("testOS.txt", "testXXXX.txt")
modtime = os.stat("testXXXX.txt").st_mtime
print(datetime.fromtimestamp(modtime))
#print(os.listdir())
'''

###########
'''
os.chdir("..")
orgPath = os.getcwd()

for dirpath, dirname, filename in os.walk(orgPath):
    print("current path:", dirpath)
    print("current folder:", dirname)
    print("filename:", filename)
    if(len(filename)>0):
        fullpath = os.path.join(dirpath, filename[0])
        print(datetime.fromtimestamp(os.stat(fullpath).st_mtime))

'''
'''
print(dir(os.path))
print(os.environ.get("PATH"))
print(os.path.basename("c:\\tmp\\test.txt"))
print(os.path.exists("c:\\tmp\\test.txt"))
print(os.path.splitext("c:\\tmp\\test.txt"))
print(os.path.splitdrive("c:\\tmp\\test.txt"))
'''