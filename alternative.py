# To make each alternate character Upper and lower case in a string
def alternate_case(input_string):
    result = ""
    #First, we need to split the lenght of the string by using len.
    for i in range(len(input_string)):
        if i % 2 == 0:
    # Second, we need to add the upper() function to the first character and += operator repeats this logic
    #to the next alternate character
            
            result += input_string[i].upper()
        else:
    # Third, the next character should be made a lower case by adding lower() function and the += operator
    #repeats this logic to the next alternate character.
            result += input_string[i].lower()
    return result

# Example usage with "Hello World"
input_string = "Hello World"
output_string = alternate_case(input_string)
print("Original string:", input_string)
print("Modified string:", output_string)

# Make each alternate word in a sentence lower and upper case
def alternate_word_case(input_sentence):
#first, we need to split the words in the sentence by using split().
    words = input_sentence.split()
#Second, we need to assign the lower () and upper () functions  to each alternating word
    result_words = [word.lower() if i % 2 == 0 else word.upper() for i, word in enumerate(words)]
# Finally , using the ' '.join function, we will create space between each word in the sentence.
    result_sentence = ' '.join(result_words)
    return result_sentence

# Example usage with "I am learning to Code"
input_sentence = "I am learning to Code"
output_sentence = alternate_word_case(input_sentence)
print("Original sentence:", input_sentence)
print("Modified sentence:", output_sentence)