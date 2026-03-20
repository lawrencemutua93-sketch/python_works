#User input
user_input = input("Enter string: ")

#Case sensitivity option
case_choice = input("Should the program ignore case? (Y/n): ").lower()
if case_choice == 'n':
    processed_text = user_input.lower()  #Converts everything to lowercase
else:
    processed_text = user_input 

#Slicing
def reverse_with_slice(text):
    return text[::-1]  # get the text backwards

#Looping
def reverse_with_loop(text):
    reversed_text = ""
    for letter in text:
        reversed_text = letter + reversed_text  
    return reversed_text

#Frequency
def count_characters(text):
    counter = {}
    for letter in text:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter

#Printing table of characters
def display_count_table(counter_dict):
    print("\nChar | Count")
    print("------------")
    for key in counter_dict:
        print(key, "   ", counter_dict[key])


print("Original Input:", user_input)
print("Slicing:", reverse_with_slice(user_input))
print("Looping:", reverse_with_loop(user_input))

frequency = count_characters(processed_text)
print("Character counts:", frequency)
display_count_table(frequency)