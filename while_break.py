if __name__ == "__main__":
    count = 0
    while count < 100:
        c = 0
        while c < 10:
            if c > 5:
                break
            print(c)
            c += 1
        print(count)
        count += 1
