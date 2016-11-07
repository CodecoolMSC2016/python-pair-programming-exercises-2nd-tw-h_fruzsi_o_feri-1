def listoverlap(list1, list2):
    c = []
    for a in list1:
        if a in list2:
            c.append(a)
    c = set(c)
    c = list(c)
    return c


def main():
    x = listoverlap([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    print(x)
    return


if __name__ == '__main__':
    main()
