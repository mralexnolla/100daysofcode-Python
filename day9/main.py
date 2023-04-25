alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction_text, plain_text, shift_amount):
  cipherText = "";
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction_text == "encode":
         newposition = position + shift_amount
    elif direction_text == "decode":
      newposition = position - shift_amount   
    cipherText += alphabet[newposition]
  print(f"The encoded text is {cipherText}")
  
caesar(direction, text, shift)      


