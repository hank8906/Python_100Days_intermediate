student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter: row.code for (index, row) in df.iterrows()}


# print(nato_dic["A"])


def produce_word_list():
    word = input('Enter a word: ')
    letter_list = [letter for letter in word]
    word_list = [nato_dic[letter.upper()] for letter in letter_list]
    print(word_list)


is_letter = True
while is_letter:
    try:
        produce_word_list()
    except KeyError:
        print("Only accept for letters in the word")
