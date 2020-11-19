
with open("Learn_file.jpg", "rb") as rf:
    with open("Learn_file_copy.jpg", "wb") as wf:
        chunk_size = 4096
        cont = rf.read(chunk_size)
        while len(cont) > 0:
            wf.write(cont)
            cont = rf.read(chunk_size)

'''    
    size_to_read = 40
    cont = f.read(size_to_read)
    #print(f.tell())
    print(cont, end="")

    f.seek(0)
    cont = f.read(size_to_read)
    print(cont, end="")
'''
#############
'''
    while(len(cont) > 0):
        print(cont, end="*")
        cont = f.read(size_to_read)
'''
'''
    for line in f:
        print(line, end="")
    content = f.readline()
    print(content, end="")

    content = f.readline()
    print(content, end = "")    
'''
