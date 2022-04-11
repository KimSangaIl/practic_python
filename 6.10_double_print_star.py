from tkinter import N


if __name__ == "__main__":
    ns = input('input number: ')
    print()
    for i in range(0, len(ns)):
        n = int(ns[i])
        for j in range(0, n * 2):
            print('\u2605', end = ' ')
        print()