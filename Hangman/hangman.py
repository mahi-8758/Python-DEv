from english_words import get_english_words_set

# Get a set of English words from the "web2" list, lowercased
web2_lowerset = get_english_words_set(['web2'], lower=True)
print(f"Number of words in web2_lowerset: {len(web2_lowerset)}")
print(list(web2_lowerset)[:1]) # Print first 10 words