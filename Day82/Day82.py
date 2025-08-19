'''
Topics to be covered:
- Project: A text-based Python program to convert Strings into Morse Code
'''

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def text_to_morse(text):
    """Convert text string to Morse code."""
    morse_text = ""
    for char in text.upper():  # Convert to uppercase
        if char in MORSE_CODE_DICT:
            morse_text += MORSE_CODE_DICT[char] + " "
        else:
            morse_text += "? "  # Unknown characters replaced with ?
    return morse_text.strip()

if __name__ == "__main__":
    print("🔠 Text to Morse Code Converter")
    user_input = input("Enter text to convert: ")
    morse_output = text_to_morse(user_input)
    print("\n🔉 Morse Code Output:")
    print(morse_output)