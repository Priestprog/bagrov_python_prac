from collections import Counter

w = int(input())
text = ""
while line := input():
    text += line

text = text.lower()
cleaned_text = ''.join([char if char.isalpha() or char.isspace() else ' ' for char in text])
words = cleaned_text.split()

filtered_words = [word for word in words if len(word) == w]

word_count = Counter(filtered_words)
if word_count:
    max_count = max(word_count.values())
    most_popular_words = sorted([word for word, count in word_count.items() if count == max_count])
    print(' '.join(most_popular_words))