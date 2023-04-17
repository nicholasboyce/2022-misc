def encrypt(key):
    message = input("What would you like to encrypt today? ")
    encrypted = ""
    for start in range(key):
        position = start
        while position < len(message):
            encrypted += message[position]
            position += key
    return encrypted
            
    