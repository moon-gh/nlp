def clean_by_stopwords(tokenized_words, stop_words_set):
    cleaned_words = []

    for word in tokenized_words:
        if word not in stop_words_set:
            cleaned_words.append(word)
    
    return cleaned_words