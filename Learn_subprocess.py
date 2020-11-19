import subprocess

#p1 = subprocess.run(["dirab", "..\\"], capture_output = True, shell = True, text = True, check = "True")
p1 = subprocess.run(["dirab", "..\\"], shell = True, stderr = subprocess.DEVNULL)

print(p1.stdout)
print(p1.returncode)
print(p1.stderr)


###########
p1 = subprocess.run(["type", "subprocess_text.txt"], shell=True, capture_output = True, text = True)
print(p1.stdout)

#p2 = subprocess.run(["grep", "-n",  "test"], shell=True, capture_output = True, text = True, input = p1.stdout)
#print(p2.stdout)