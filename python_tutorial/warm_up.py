""" Đề bài: Cho một chuỗi văn bản: text = "data science is cool but data cleaning is boring"

Yêu cầu: Viết code trả về một Dictionary đếm số lần xuất hiện của từng từ. Input: Chuỗi trên. Output mong đợi: {'data': 2, 'science': 1, 'is': 2, 'cool': 1, 'but': 1, 'cleaning': 1, 'boring': 1} 
"""

text = "data science is cool but data cleaning is boring"

def count_words(text: str) -> dict[str, int]:
    words = text.split()
    #words = ['data']
    word_counts = {word:words.count(word) for word in words}  #O(n^2)
    return word_counts
print(count_words(text))

def count_words_improved(text: str) -> dict[str, int]:
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
print(count_words_improved(text))

def count_words_improved_pro(text: str) -> dict[str, int]:
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
print(count_words_improved_pro(text))

from collections import Counter
def count_word_ultra(text: str) -> dict[str, int]:
    words = text.split()
    word_counts = Counter(words)
    return word_counts

print(f"ULTRA Version of counting words: {count_word_ultra(text)}")