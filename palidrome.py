def is_palidrome(string_value):
    char_array = list(string_value)
    size = len(char_array)
    half_size = int(size / 2)
    for i in range(0, half_size):
        if char_array[i] != char_array[size - i - 1]:
            return False
    return True
    
def convert_to_palidrome(v):
    def action(string_value, chars):
        chars_to_append = list(string_value)[0:chars]
        chars_to_append.reverse()
        new_value = string_value + "".join(chars_to_append)
        if not is_palidrome(new_value):
            new_value = action(string_value, chars + 1)
        return new_value
    return action(v, 0)

user_input = input("String to convert to palindrome (exit to terminate program): ")
while user_input != "exit":
    print(str(convert_to_palidrome(user_input)))
    user_input = input("string to check (exit to terminate): ")
