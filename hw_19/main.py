def anagrams(word_list):

    anagram_groups = []
    while word_list:
        word = word_list.pop(0)
        anagrams = [word]
        i = 0
        while i < len(word_list):
            if sorted(word) == sorted(word_list[i]):
                anagrams.append(word_list.pop(i))
            else:
                i += 1
        if len(anagrams) > 1:
            anagram_groups.append(anagrams)
    return anagram_groups


word_list = ['cat', 'dog', 'tac', 'god', 'act', 'ogd']
anagram_groups = anagrams(word_list)

print(anagram_groups)

