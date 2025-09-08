

def enigma_light():

    keys = 'abcdefghijklmnopqrstuvwxyz !'

    values = keys[-1] + keys[0:-1]

    print(keys)
    print(values)

    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values,keys))

    # # OR create 1 and then flip
    # dict_e = dict(zip(keys, values))
    # dict_d = {value: key for key, value in dict_e.items()}

    msg = input("Enter message Quietly: ")
    mode = input("Enter mode (e) encryption or decryption as default mode: ")

    if mode == 'e':
        new_msg  = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg =''.join([dict_d[letter] for letter in msg.lower()])
    return new_msg.capitalize()
saved_enigma = enigma_light()
print(saved_enigma)