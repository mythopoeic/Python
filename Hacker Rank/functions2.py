def reverse(text):
    a = list(text)
    b = []
    for x in range(len(a) - 1, - 1, - 1):
        b.append(a[x])
    print ''.join(b)
    return ''.join(b)

reverse("Python!")
reverse("Hello World!")