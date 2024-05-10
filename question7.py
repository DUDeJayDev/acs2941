# Check if a given text is a palindrome (reads the same backward as forward).

def is_palindrome(text: str):
    text = [text.lower() for text in text if text.isalpha()] 
    left, right = 0, len(text) - 1

    while left <= right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man, a plan, a canal: Panama"))