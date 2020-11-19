# this to explain __name__=="__main__"


def cool_func():
    print("This is super Cool!!")

if(__name__=="__main__"):
#print("__name__="+__name__)
    print("call it locally")
    cool_func()