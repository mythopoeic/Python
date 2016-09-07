N = int(raw_input())
email = []
alnum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
alnumplus = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
for _ in range(N):
    email.append(raw_input())

fun1 = lambda x: '@' in x and '.' in x and 0 < x.index('@') < len(x) - x[::-1].index('.') and x[::-1].index('.') < 4

fun2 = lambda x: all(c in alnum for c in x[(x.index('@') + 1):(len(x) - x[::-1].index('.')-1)])

fun3 = lambda x: all(c in alnumplus for c in x[:x.index('@')])

email = list(filter(fun1,email))
email = list(filter(fun2,email))
email = list(filter(fun3,email))
print sorted(email)