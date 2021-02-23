def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def square(a):
    return a**2

testList = [1, -4, 8, -9]

applyToEach(testList, square)

print(testList)
