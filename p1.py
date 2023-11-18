input_string = "This is a sample string. This string is a sample. Sample is the keyword." 

word_to_count = "sample" 
count = input_string.lower().count(word_to_count.lower()) 

print(f"The word '{word_to_count}' appears {count} times in the input string.") 
