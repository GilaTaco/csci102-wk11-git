# fibonacci.py

def fib():
    fibs = [1, 2]
    F_one = 1
    F_two = 2
    for i in range(1,9):
        
        F = F_one + F_two
        fibs.append(F)
        F_one = F_two
        F_two = F

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
