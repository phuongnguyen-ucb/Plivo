# Convert letter to phone number:
LETTERS = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9]
def letter_to_digit(character):
  string_numbers = map(str, NUMBERS)
        for alphabet_set in enumerate(LETTERS):
                if character in alphabet_set[1]:
                        index = alphabet_set[0]
        return string_numbers[index]
        

# Create a string of a telephone number:
def clean_phone_number(text):
        clean_number = []
        for item in text.lower():
                if item.isdigit():
                        clean_number.append(item)
                elif item.isalpha():
                        clean_number.append(letter_to_digit(item))
        return ''.join(clean_number) 

# Ask users to input text:
text = raw_input("Please enter your text: ")

# Display a telephone number:
print clean_phone_number(text)