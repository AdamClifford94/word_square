from marisa_trie import Trie

# get word_count of words
def word_count(word): 
    counter = {}
    for k in word:
        if k not in counter:
            counter[k] = 1
        else:
            counter[k] += 1
    return counter

def word_check(word):
    word_counts = word_count(word)
    for c, n in word_counts.items():
        if n > counts.get(c, 0):
            return False
        if n >= 2 and n * 2 - 1 > counts[c]:
            return False
    return True

def recurse(words, i):
    if i == N:
        counter = word_count("".join(words)) # sanity check, if the result is actually correct
        for c, n in counter.items():
            if n > counts[c]:
                return None
        return words
    for j in range(i, N):
        sofar = "".join(word[j] for word in words)
        if not trie.has_keys_with_prefix(sofar):
            return None
    sofar = "".join(word[i] for word in words)
    for word in trie.iterkeys(sofar):
        result = recurse(words+(word,), i+1)
        if result:
            return result
    return None

N, letters = 8, "aaaaccddddeeeeeeeeeeeeeeeeeeiiiiiilmmnnnnooprrrrrrssssssstttttzz"
counts = word_count(letters)
words = [
    word
    for word in open("../../enable1.txt").read().splitlines()
    if len(word) == N and word_check(word)
]
trie = Trie(words)
result = recurse((), 0)
print(result)
