import time
from morse import MORSE_CODE_DICT

def encode(char_list):
    code_list = []
    for char in char_list:
        if char == " ":
            code_list.append(" ")
        elif char.upper() not in MORSE_CODE_DICT:
            return None
        else:
            new_char = MORSE_CODE_DICT[char.upper()]
            code_list.append(new_char)
    return code_list

def decode(list_of_codes):
    morsed_word = ""
    for code in list_of_codes:
        if code != " ":
            morsed_word += code
            morsed_word += " "
        else:
            morsed_word += " / "
    print(morsed_word)

word = input("Give a word to convert to Morse Code or type 'exit' to quit the program: ")
while word != "exit":
    word_list = list(word)
    encoded_code_list = encode(word_list)
    if encoded_code_list:
        decode(encoded_code_list)
    else:
        print("A given character does not exist in Morse Code Alphabet.")
    word = input("Give a word to convert to Morse Code or type 'exit' to quit the program: ")
print("Good Bye!")
