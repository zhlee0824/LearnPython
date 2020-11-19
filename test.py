import os
import subprocess

print("Louis Test")
'''
#result = os.system("adb devices")
testInt = 7
testStr = f"print testStr: {testInt:>03d}"

print(testStr)

for i in range(10):
    print(i)
    print(i+1)

''' 
'''
p1 = subprocess.run(["adb", "shell", "ls", "-al", "/sdcard/kLog/90233_1026__Ker0.txt_"], shell = True, stdout = subprocess.PIPE)
print(p1.stdout)
strOut = p1.stdout.decode("utf8")
outArg = strOut.split(" ")
print(outArg)
size = int(outArg[4])
print(size)
'''

'''
p1 = subprocess.run(["adb", "devices"], shell = True, stdout = subprocess.PIPE)
print(p1.stdout)
strOut = p1.stdout.decode("utf8")
print(strOut.find("192.168.205.154"))
'''
'''
condition = False

x=1 if condition else 0

if condition:
    x=1
else:
    x=0


print(x)
'''

num1 = 100_000_000
num2 = 100_000

total = num1+num2
print(f"{total:,}")

names = ["coey", "rolly", "katerson", "billboard"]

for index, name in enumerate(names, start  = 100):
    print(index, name)

names = ["Peter Parker","Clark Kent", "Wad Wilson", "Bruce Wayne"]
heros = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

#for index, name in enumerate(names):
    #hero = heros[index]
for name, hero, universe in zip(names, heros, universes):
    print(f"{name} is actually {hero} from {universe}")

for value in zip(names, heros, universes):
    print(value)




a, b, *_, d = (1, 2, 3, 4, 5, 6, 7, 8)

print(a)
print(b)
#print(c)
print(d)

class Person():
    pass

person = Person()

first_key = "first"
first_val = "Louis"

person_info = {"first":"Louis", "last":"Lee"}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person,key))


#####################

from getpass import getpass

username = input("Username:")
passord = getpass("Password:")

print("logging in ....")