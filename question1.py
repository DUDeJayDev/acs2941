from string import ascii_uppercase, ascii_lowercase

# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. 
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

def caesarCipher(input_str, rotation):
    def normalize(value: int, alphas) -> int:
        if value < 0:
            return normalize(value + len(alphas))
        return value % 26
    
    secret = ''
    
    for i in input_str:
        alphabet = ascii_uppercase if i.isupper() else ascii_lowercase
        try:
            index = list(alphabet).index(i)
            secret += alphabet[normalize(index + rotation, alphabet)] if index + rotation < len(alphabet) else alphabet[normalize(index + rotation - len(alphabet), alphabet)]
        except ValueError:
            secret += i
    
    return secret

if __name__ == '__main__':
    caesarCipher('middle-Outz', 2)
    caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5)
    caesarCipher('Hello_World!', 4)
