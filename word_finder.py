import json
import sys
import argparse

class Wordle():
    
    def __init__(self, word_length: int = 0, language: str = 'en', char_to_find: str = '', starting_char_index: bool = False, 
                 ending_char_index: bool = False, char_index: list = [], custom_finder: dict = {}, contains_char: list = []):        
        self.word_length = word_length
        self.language = language
        self.char_to_find = char_to_find
        self.starting_char_index = starting_char_index
        self.ending_char_index = ending_char_index
        self.char_index = char_index
        self.custom_finder = custom_finder
        self.contains_char = contains_char
    

    def word_rule(self, words: list = []):
        
        words_list = []
        counter = 1
        for word in words:        
            if len(word) == self.word_length:
                if self.starting_char_index:
                    if word.startswith(self.char_to_find):
                        words_list.append(f'{counter}:{word}')
                elif self.ending_char_index:
                    if word.endswith(self.char_to_find):
                        words_list.append(f'{counter}:{word}')
                elif self.char_index:
                    temp_words = {}
                    for i in self.char_index:
                        if word[i] == self.char_to_find:
                            self._is_in_dictionary(word, temp_words)
                    if self.loop_dictionary(temp_words, self.char_index):
                        words_list.append(f'{counter}:{self.loop_dictionary(temp_words, self.char_index)}')
                        counter += 1
                elif self.custom_finder:
                    temp_words = {}
                    for k,v in self.custom_finder.items():
                        if word[v] == k:
                            self._is_in_dictionary(word, temp_words)
                    if self.loop_dictionary(temp_words, self.custom_finder):
                        words_list.append(f'{counter}:{self.loop_dictionary(temp_words, self.custom_finder)}')
                        counter += 1
                elif self.contains_char:
                    temp_words = {}
                    for i in self.contains_char:
                        if i in word:
                            self._is_in_dictionary(word, temp_words)
                    if self.loop_dictionary(temp_words, self.contains_char):
                        words_list.append(f'{counter}:{self.loop_dictionary(temp_words, self.contains_char)}')
                        counter += 1
                else:
                    words_list.append(f'{counter}:{word}')
        return words_list
    
    @staticmethod
    def _is_in_dictionary(word, temp_words):
        if word in temp_words:
            temp_words[word] += 1
        else:
            temp_words[word] = 1
        return temp_words

    @staticmethod
    def loop_dictionary(temp_dict, custom):
        for k,v in temp_dict.items():        
            if v > len(custom)-1:
                return k


    def find_word(self, data):
        word_list = []
        for words in data:            
            if self.language == 'en':        
                for word in words.keys():
                    word_list.append(word)
            else:
                word_list.append(words)
        return self.word_rule(words=word_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find Word in Given Language")
    parser.add_argument('-l', '--language', type=str, required=True)
    args = vars(parser.parse_args())
    
    english = Wordle(word_length=5, language='en', contains_char=['a','u'])
    turkish = Wordle(word_length=5, language='tr', contains_char=['a','u','b'])
    
    try:
        if args['language'] == 'en':
            with open('dictionary_alpha_arrays.json', 'r') as f:
                print(*english.find_word(json.load(f)), sep='\n')
        elif args['language'] == 'tr':
            with open('dictionary_tr.json', 'r') as f:
                print(*turkish.find_word(json.load(f)), sep='\n')
        else:
            pass
    except Exception as e:
        print('Error Occurred:', e)
    finally:
        sys.exit()
    

