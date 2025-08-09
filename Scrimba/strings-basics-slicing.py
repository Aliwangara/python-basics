msg = "Welcome to this website"

print(msg.count("w"))
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(msg.upper())


#slicing

print(msg[0]) # gives the first character in a string
print(msg[-1]) # gives the last character
print(msg[1:3]) # pricks from character number 1 - 2 : El
print(msg[2:]) #Picks from  character 2 to last character
print(msg[:6]) # picks from first character to the fifth character of the text


msg='welcome to Python 101: Strings'
msg1=   msg[18] + " " + msg[:8] + msg[25:29] + msg[7:11] + msg[13] + msg[12] + msg[2] + msg[1] + msg[-5]
print(msg1.title())
print(msg1[::-1].title())

# String find/ replace, formatting

msg2 = """Dear ali,You should cut spending
"""

print(msg2, end="")

msg='Welcome to Python 101: Strings'
print(msg.find('Python'))
print(msg.replace('Python', 'Js'))



