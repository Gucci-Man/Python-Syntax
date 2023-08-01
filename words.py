def print_upper_words(words_list, must_starts_with):
    """
    Prints out each word on a seprate line but in all uppercase.
    
    words_list: list of words to be uppercased 
    must_start_with: a set of letters for which only words that start with them can be printed
    
    words and letters in arguments can be either lowercase or uppercase initially
    """
    
    for word in words_list:
        for letter in must_starts_with:
            if word.lower().startswith(f"{letter.lower()}"):
                print (word.upper())
        

print_upper_words(["Hello", 'hey', 'goodbye', 'yo', 'yes', 'daddy', 'moose', 'elephant'], must_starts_with={"D","e"})