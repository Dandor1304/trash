a = 0
b = 0
def slog (a,b):
    print("Введите А")
    a = int(input())
    print("Введите B")
    b = int(input())
    return a+b
#print(slog(a,b))
i = 1
while i != "n":
    print(slog(a, b))
    print("хотите продолжить y/n")
    i = input()
