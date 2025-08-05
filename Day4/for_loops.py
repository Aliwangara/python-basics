# forloop = execute a block of code a fixed number of times
#             You can iterate over a range,  string, sequence e.tc

for i in range(1 ,11, 2)  :
    print(i)

print("Happy new year")

# to skip over an iteration we use the continue keyword eg:

for x in range(1,21):
        if x == 13:
            continue # 13 won't be displayed
        else:
            print(x)