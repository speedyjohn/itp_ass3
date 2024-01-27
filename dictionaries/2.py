def cumulative_frequency(tuples_list):
    frequency_dict = {}
    for word, frequency in tuples_list:
        if word in frequency_dict:
            frequency_dict[word] += frequency
        else:
            frequency_dict[word] = frequency

    return frequency_dict


word_frequencies = [('apple', 2), ('banana', 3), ('apple', 4), ('orange', 5)]
print(cumulative_frequency(word_frequencies))
