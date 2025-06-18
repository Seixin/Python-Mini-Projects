alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

def caesar(ori, shift, arah):
    output_text =""
    if arah == "decode":
        shift *= -1
    for i in ori:
        if  i not in alphabet:
            output_text += i
        else:
            shifted = alphabet.index(i) +shift
            shifted %= len(alphabet)
            output_text += alphabet[shifted]

    print(output_text)

lanjut = True

while lanjut:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type Your Message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    pilihan = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if pilihan == "yes":
        lanjut = True
    else:
        lanjut= False
        

