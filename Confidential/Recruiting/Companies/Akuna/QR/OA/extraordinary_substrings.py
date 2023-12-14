def countSubstrings(input_str):
    length = len(input_str)
    string_int = {'a': 1, 'b': 1}
    
    for i in range(2, 26):
        string_int[chr(ord('a') + i)] = (i-2) // 3+2
    
    extraordinary = 0
    for i in range(length):
        string_sum = 0
        for j in range(i, length):
            string_sum += string_int[input_str[j]]

            if not string_sum % (j-i+1):
                extraordinary += 1

    return extraordinary

input_str = 'asdf'
print(countSubstrings(input_str))

input_str = 'bdh'
print(countSubstrings(input_str))