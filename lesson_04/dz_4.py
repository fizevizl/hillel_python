
input_words = input("Введіть речення з двома словами: ")
word1, word2 = input_words.split()

formatted_1 = f"!{word2.upper()} {word1.capitalize()}?"
formatted_2 = "!{} {}?".format(word2.upper(), word1.capitalize())
formatted_3 = "!%s %s?" % (word2.upper(), word1.capitalize())

# output = f"{input_words}<<<>>>{formatted_1}<<<>>>{formatted_2}<<<>>>{formatted_3}"
# print(output)
print(input_words, formatted_1, formatted_2, formatted_3, sep="<<<>>>" )