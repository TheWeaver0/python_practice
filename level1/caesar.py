alphabet = 'abcdefghijklmnopqrstuvwxyz'
def caesar(message, offset, direction = 1):
    final_message = ''
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            idx = alphabet.index(char)
            new_char = alphabet[(idx + offset*direction) % len(alphabet)]
            final_message += new_char
    return final_message

def encrypt(message, offset):
    return caesar(message, offset)

def decrypt(message, offset):
    return caesar(message, offset, -1)
test_cases= {
    "HELLO": [3, "khoor"],
    "Python": [5, "udymts"],
    "abc": [2, "cde"],
    "Zoo": [1, "app"],
    "OpenAI": [13, "bcranv"],
    "Cipher Test": [7, "jpwoly alza"],
    "Data Science": [4, "hexe wgmirgi"],
    "Secret123": [10, "combod123"],
    "Good Morning": [8, "owwl uwzvqvo"],
    "Attack at Dawn": [25, "zsszbj zs czvm"]
}



def main():

    for key, value in test_cases.items():
        encryption = encrypt(key, value[0])
        print(f'Key: {key}, Value: {value}, Encryption: {encrypt(key, value[0])}, Comparaison: {encryption == value[1]} \n')

    # encryption = encrypt("HELLO", test_cases["HELLO"][0])
    # print(encryption)
if __name__ == "__main__":
    main()