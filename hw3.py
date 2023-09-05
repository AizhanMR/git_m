while True:
    word = input('enter any word: ').lower()
    vowels = 0
    consonants = 0
    print('letter count:', len(word))

    for i in word:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
            vowels = vowels + 1 # +=
        else:
            consonants = consonants + 1
    print('number of vowels: ', vowels)
    print('number of consonants: ', consonants)

    v = str(round(vowels/(vowels+consonants)*100, 2))
    c = str(round((consonants / (vowels + consonants)) * 100, 2))

    print('vowel/consonant ratio', v,'/',c)
