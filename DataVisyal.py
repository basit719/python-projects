import matplotlib.pyplot as plt
from collections import Counter

text = "Python is powerful and Python is awesome"
words = text.split()
word_counts = Counter(words)

plt.bar(word_counts.keys(), word_counts.values())
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Word Frequency')
plt.show()
