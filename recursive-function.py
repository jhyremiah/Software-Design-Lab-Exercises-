# Recursive function to reverse a string.
def reverse_string(string):
    def get_reversed_string(string_a, string_b):
        ## check if string_b 
        ## is the last letter of the string.
        if len(string_b) == 1:
            return string_b + string_a
        else:
            return get_reversed_string(string_b[0], string_b[1:]) + string_a
    return get_reversed_string(string[0], string[1:])