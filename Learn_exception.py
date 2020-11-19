

try:
    f=open("test.py")
    var = bad_var
except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)