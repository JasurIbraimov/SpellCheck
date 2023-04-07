import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


# Reading dictionary.txt into an array. 
dictionary_list = [] # List that will contain all words in dictionary.txt
dictionary_file = open("dictionary.txt") # Opening file dictionary.txt to read

for line in dictionary_file: # for each line in dictionary.txt (for each word)
    dictionary_list.append(line.strip()) # add word into the dictionary list, and remove ant line feeds or spaces (.strip)

dictionary_file.close() # Close file after operation done 


# Linear Search Version
print("--- Linear Search ---")
# Reading AliceInWonderLand200.txt 
story_file = open("AliceInWonderLand200.txt")

for i, line in enumerate(story_file): # for loop to iterate through each line of story and numerate each line assigning it to variable i
    word_list = split_line(line) # splitting apart the line of text in the story and assigning variable word_list
    for word in word_list: # for loop to iterate through each word in the words list
        current_list_position = 0 # Start at the beggining of the dictionary list

        # Loop until you reach the end of the list, or the value at the
        # current position is equal to the word in upper case, cause words in dictionary are in upper case
        while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper(): 
            current_list_position += 1  #  Advance to the next word in the dictionary
        if current_list_position == len(dictionary_list): # If iterated through all words in dictionary, and not founded it
            print(f"Line {i+1} possible misspelled word: {word}" )


story_file.close() # Closing the AliceInWonderLand200.txt 


# Binary Search Version 
print("--- Binary Search ---")

# Reading AliceInWonderLand200.txt 
story_file = open("AliceInWonderLand200.txt")

for i, line in enumerate(story_file): # for loop to iterate through each line of story and numerate each line assigning it to variable i
    word_list = split_line(line) # splitting apart the line of text in the story and assigning variable word_list
    for word in word_list: # for loop to iterate through each word in the words list
        lower_bound = 0 # Low Bound of binary search
        upper_bound = len(dictionary_list) - 1 # Upper bound of binary search
        found = False # indecator that word is found or not
        
        # Loop until we find the item, or our upper/lower bounds meet
        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2 # Find the middle position
            # Figure out if we:
            # move up the lower bound, or
            # move down the upper bound, or
            # we found what we are looking for
            if dictionary_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True
            
        if not found: # If the word was not founded
            print(f"Line {i+1} possible misspelled word: {word}" )


story_file.close() # Closing the AliceInWonderLand200.txt 