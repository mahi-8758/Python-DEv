import input_word
word_count = input_word.guessedword
holder = []
word_len = len(word_count)
print(f"The number of letter : {word_len}") 
firstword = word_count[0]

if word_len > 8:
    print("Word length is greater than 8, revealing first letter.")
    print(f"First word as a hint is : {firstword}")
    holder.append(firstword)
    for i in range(1, word_len):
        holder.append('_')
else:
     for i in range(word_len):
         holder.append('_')
final_holder = (' '.join(holder))
print(final_holder)