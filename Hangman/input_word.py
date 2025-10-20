from english_words import get_english_words_set

web2_lowerset = get_english_words_set(['web2'], lower=True)
guess_word = (list(web2_lowerset)[:1])  
guessedword = ''.join(guess_word)
print(guessedword)  # Debug: shows word during development