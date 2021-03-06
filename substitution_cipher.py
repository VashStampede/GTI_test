def encrypt(text, n):
    i = 0
    while i < n:
        evens  = "".join(text[index].lower() for index in range(1, len(text), 2))
        odds = "".join(text[index].lower() for index in range(0, len(text), 2))
        text = evens + odds
        i += 1

    encrypted_text = text
    print("Encripted text: ", encrypted_text)
    return encrypted_text


def decrypt(encrypted_text, n):
    i = 0
    while i < n:
        middle = int(len(encrypted_text) / 2)
        first_part = encrypted_text[:middle]
        second_part = encrypted_text[middle:]

        resulted_text = ""

        pairs = zip(second_part, first_part)

        for pair in pairs:
            resulted_text += pair[0] + pair[1]

        if len(encrypted_text) & 1:
            resulted_text += second_part[-1]
        i +=1

        encrypted_text = resulted_text

    decrypted_text = resulted_text
    print("Decripted text: ", decrypted_text)
    return decrypted_text


text = input("Enter text: ")
n = input("Enter int n: ")
# Check text 
if (len(text) == 0 or not text):
    print("Entered text: ", text)
# Check n
elif (not n or int(n) <= 0):
    print("Entered text: ", text)
else:
    n = int(n)
    encrypted_text = encrypt(text, n)
    decrypted_text = decrypt(encrypted_text, n)