def test():
    a = [1, 2]
    while True:
        b = a.pop(0)
        print(b)
        a.append(b)
        print(a)


if __name__ == "__main__":
    test()