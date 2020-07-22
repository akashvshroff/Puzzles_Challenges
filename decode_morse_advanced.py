import re

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}


def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    smallest_set = min(re.findall(r'1+', bits), key=len)
    len_s = len(smallest_set)
    pauses = re.findall(r'0+', bits)
    if pauses:
        if len(min(pauses, key=len)) < len_s:  # set bits are dash
            bit_time = len_s//3
        else:
            bit_time = len_s
    else:
        bit_time = len_s

    mapping = {
        '1'*bit_time: '.',
        '111'*bit_time: '-',
        '0'*bit_time: '',
        '000'*bit_time: ' ',
        '0000000'*bit_time: '  '
    }
    mapping = sorted(mapping.items(), reverse=True, key=lambda x: len(x[0]))
    for key, value in mapping:
        bits = bits.replace(key, value)
    return bits


def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    words = morseCode.split('  ')
    res = ''
    for word in words:
        res += ''.join([MORSE_CODE[l] for l in word.split()]) + ' '
    return res.strip()


bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
print(decode_morse(decode_bits(bits)))
