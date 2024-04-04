# Read a given string, change the character at a given index and then print the modified string. 

def mutate_string(string, position, character):
    res = list(string)
    res[position] = character
    string = ''.join(res)
    return string


mutate_string('abracadabra', 5, 'k')
mutate_string('hello', 2, 'w')