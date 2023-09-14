import re
from collections import defaultdict

def word_frequency(sentence):
    word_count = defaultdict(int)
    words = re.findall(r'\w+', sentence.lower())
    
    for word in words:
        word_count[word] += 1
    
    return dict(word_count)

#test case !
sentence = "That Dad is the best.The best is that Dad."
result = word_frequency(sentence)
print(result)
