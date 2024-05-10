import re

# You are given a string.
# Your task is to find out if the string contains: 
# * alphanumeric characters, 
# * alphabetical characters, 
# * digits, 
# * lowercase and uppercase characters.

# In the first line, print True if has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if has any alphabetical characters. Otherwise, print False.
# In the third line, print True if has any digits. Otherwise, print False.
# In the fourth line, print True if has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if has any uppercase characters. Otherwise, print False. 

def string_validate(s: str):
    print(re.search('[\w]', s) is not None)
    print(re.search('[A-Za-z]', s) is not None)
    print(re.search('[0-9]+', s) is not None)
    print(re.search('[a-z]', s) is not None)
    print(re.search('[A-Z]', s) is not None)


string_validate('qA2')