# Solution: Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


# Solution: Convert a Number to a String
def number_to_string(num):
    return str(num)


# Solution: Remove String Spaces
def no_space(x):
    return x.replace(" ", "")


# Solution: Vowel Count
def get_count(sentence):
    return sum(1 for char in sentence if char in "aeiou")
