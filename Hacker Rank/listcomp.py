X = int(raw_input())
X = [i for i in range(X + 1)]
Y = int(raw_input())
Y = [i for i in range(Y + 1)]
Z = int(raw_input())
Z = [i for i in range(Z + 1)]
N = int(raw_input())
ListComp = [[X[i],Y[j],Z[k]] for i in range(len(X)) for j in range(len(Y)) for k in range(len(Z)) if X[i] + Y[j] + Z[k] != N]
print ListComp