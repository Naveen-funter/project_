def reverse_string_with_loop(input_string):
    reversed_string = ""
    for index in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[index]
    return reversed_string

user_input = input("Enter a string to reverse: ")
result = reverse_string_with_loop(user_input)
print("Reversed string:", result)


nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
print(evens)
