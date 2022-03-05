import json
    
    
def word_rule(word: str = '', word_length: int = 0, char_to_find: str = '', starting_char_index: bool = False, 
            ending_char_index: bool = False, char_index: list = [], custom_finder: dict = {}, contains_char: list = []):
    if len(word) == word_length:
        if starting_char_index:
            if word.startswith(char_to_find):
                print(word)
        elif ending_char_index:
            if word.endswith(char_to_find):
                print(word)
        elif char_index:
            temp_words = {}
            for i in char_index:
                if word[i] == char_to_find:
                    if word in temp_words:
                        temp_words[word] += 1
                    else:
                        temp_words[word] = 1
            loop_dictionary(temp_words, char_index)
        elif custom_finder:
            temp_words = {}
            for k,v in custom_finder.items():
                if word[v] == k:
                    if word in temp_words:
                            temp_words[word] += 1
                    else:
                        temp_words[word] = 1
            loop_dictionary(temp_words, custom_finder)
        elif contains_char:
            temp_words = {}
            for i in contains_char:
                if i in word:
                    if word in temp_words:
                        temp_words[word] += 1
                    else:
                        temp_words[word] = 1
            loop_dictionary(temp_words, contains_char)
        else:
            print(word)
            
def loop_dictionary(temp_dict, custom):
    for k,v in temp_dict.items():
        if v > len(custom)-1:
            print(k)


if __name__ == '__main__':            
    with open('dictionary_alpha_arrays.json', 'r') as f:
        data = json.load(f)

    for words in data:
        for word in words.keys():
            word_rule(word=word, word_length=5, contains_char=['a','e','d'])
            # word_rule(word=word, word_length=5, custom_finder={'a':0, 'd':4, 'e':2})
