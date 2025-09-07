alphabet = 'abcdefghijklmnopqrstuvwxyz'
def vigenere(message, key, direction = 1):
    final_message = ''
    i = 0
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[i%len(key)]
            # print(f'key_char: {key_char}, i: {i}\n')
            idx = alphabet.index(char)
            key_idx = alphabet.index(key_char)
            new_char = alphabet[(idx + key_idx*direction) % len(alphabet)]
            final_message += new_char
            i += 1
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)


test_cases = {
    "HELLO": ["keythree", "rijev"],
    "Python": ["keyfive", "zcrmwi"],
    "abc": ["keytwo", "kfa"],
    "Zoo": ["keyone", "jsm"],
    "OpenAI": ["keythirteen", "ytcghq"],
    "Cipher Test": ["keyseven", "mmnzim xrcx"],
    "Data Science": ["keyfour", "nerf gwzoraj"],
    "Secret123": ["keyten", "ciakig123"],
    "Good Morning": ["keyeight", "qsmh uuygsre"],
    "Attack at Dawn": ["keytwentyfive", "kxrtyo nm bfei"]
}




def main():

    for key, value in test_cases.items():
        encryption = encrypt(key, value[0])
        print(f'Encryption process: message: {key}, key & final_message: {value}, Encryption: {encryption}, Comparaison: {encryption == value[1]} \n')
        decryption = decrypt(encryption, value[0])
        print(f'Decryption process: key & final_message:: {value}, message: {key.lower()}, Decryption: {decryption}, Comparaison: {decryption == key.lower()} \n')

if __name__ == "__main__":
    main()