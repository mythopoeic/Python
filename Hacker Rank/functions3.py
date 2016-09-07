def anti_vowel(test):
    a = list(test)
    for i in range(len(a) - 1, -1, -1):
        if a[i].lower() == 'a' or a[i].lower() == 'e' or a[i].lower() == 'i' or a[i].lower() == 'o' or a[i].lower() == 'u':
            a.remove(a[i])
    print ''.join(a)
    return ''.join(a)
    
anti_vowel("Hey You!")