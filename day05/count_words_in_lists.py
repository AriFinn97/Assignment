def count_words(word_list):
    word_count = {}  
    for word in word_list:
        if word in word_count:
            word_count[word] += 1 
        else:
            word_count[word] = 1  
    return word_count


words = ["man","man","cat","cat","dog"]
result = count_words(words)
print(result)
