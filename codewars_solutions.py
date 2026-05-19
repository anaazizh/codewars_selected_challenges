"""
SE Foundations Codewars Knowledge Check
Solutions for selected Codewars challenges.
"""


# Even or Odd
# Return "Even" if the integer is even, "Odd" otherwise.
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# Convert a Number to a String
# Convert the given number into its string representation.
def number_to_string(num):
    return str(num)


# Remove String Spaces
# Remove all space characters from the given string.
def no_space(x):
    return x.replace(" ", "")


# Vowel Count
# Count the number of lowercase vowels (a, e, i, o, u) in the input string.
def get_count(sentence):
    return sum(1 for ch in sentence if ch in "aeiou")


if __name__ == "__main__":
    # Lightweight local verification
    assert even_or_odd(2) == "Even"
    assert even_or_odd(1) == "Odd"
    assert even_or_odd(0) == "Even"
    assert even_or_odd(-7) == "Odd"

    assert number_to_string(67) == "67"
    assert number_to_string(-1) == "-1"
    assert number_to_string(0) == "0"

    assert no_space("8 j 8   mBliB8g  imjB8B8  jl  B") == "8j8mBliB8gimjB8B8jlB"
    assert no_space("") == ""
    assert no_space("hello world") == "helloworld"

    assert get_count("abracadabra") == 5
    assert get_count("") == 0
    assert get_count("bcdfg") == 0
    assert get_count("aeiou") == 5

    print("All verifications passed.")
