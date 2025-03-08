# input = [12, 34, 45, 4, 65, 70]
# target = 74


x = 12345
y = 54321

def issso(x):
    return x == x[::-1]


print(issso(x))