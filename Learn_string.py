
message = "Hello world"
message1 = "Buddy's world"
message2 = 'Buddy\'s world'
message3 = """this is 
string of helloworld"""
message4 = '''single quota 
also work'''

print(message4)
print(len(message))
print(message[10])
print(message[6:])
print(message.upper())

print(message.count("l"))
print(message.find("world"))

print(message.replace("world", "universal"))
print(message)
message_update = message.replace("l", "k")
print(message_update)

greeting = "Hello"
name = "Jennifer"
greetMessage = greeting + "," +"Jim" +", Welcome"
print(greetMessage)

message = "{}, {}, Welcome".format(greeting, name)
message2 = f"{greeting}, {name.upper()}, Welcome here!"
print(message)
print(message2)

print(dir(name))
print(help(str))
