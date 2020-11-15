# 0.0
# 0.9527544408738466
# 0.8644738145642124
# 0.8951715163278082
# 0.7770887149698589
# 0.9402385695332803
# 0.7327387580875756
# 0.9258750683338899
# 0.8842724875284311
# 0.9055088817476932
# 0.8328165362273942
# 0.8804771390665607
# 0.8396432548525454
# 0.8703592552895671
# 0.8740118423302576
# 0.9442721787424647
# 0.8406361854220809
# 0.956644501523794
# 0.9442721787424647
# 0.8885443574849294
# 0.8427572744917122
# 0.8250364469440588

import numpy as np
import re
from scipy.spatial import distance

fp = open('desktop/sentences.txt', 'r') 

def dict_of_words(words, dict_of_words):
    index = 0
    for word in words:
        dict_of_words[word] = index
        index += 1

def set_of_words(words, unique_words):
    for word in words:
        if word != '':
            word = word.lower()
            unique_words.add(word)
            
def dict_of_sentences(words, dict_of_sentences):
    index = 0
    for key in dict_of_sentences:
        index += 1
    dict_of_sentences[index] = words
    
def matrix_builder(columns, rows):
    output_matrix = np.zeros(len(columns), dtype = int)
    for  centence_index, words in rows.items():
        number_of_columns = len(columns)
        row_vector = np.zeros(number_of_columns, dtype = int)
        for word in words:
            if word in columns:
                row_vector[columns[word]] += 1
        output_matrix = np.vstack([output_matrix, row_vector])
    output_matrix = np.delete(output_matrix, (0), axis=0)
    return output_matrix

def distance_cosine(vector_one, vector_two):
    return distance.cosine(vector_one, vector_two)
                
line = fp.readline()
columns_as_words = {} # словарь с парами "слово:уникальный номер соответствия"
rows_as_sentences = {} # словарь с парами "индекс пердложения:массив слов этого предложения"
unique_words = set()

counter = 1
while line:
    line = line.lower() # приведите каждую строку к нижнему регистру с помощью строковой функции lower()
    line = re.split('[^a-z]', line) # произведите токенизацию, то есть разбиение текстов на слова
    set_of_words(line, unique_words) # список всех слов, встречающихся в предложениях - будущие сталбцы матрицы
    dict_of_sentences(line, rows_as_sentences)
    line = fp.readline()
    counter += 1
    
   
dict_of_words(unique_words, columns_as_words) # Сопоставьте каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях
matrix = matrix_builder(columns_as_words, rows_as_sentences) # матрицу размера n * d, где n — число предложений

base_vector = matrix[0]

for vector in matrix:
    print(distance_cosine(base_vector, vector))
