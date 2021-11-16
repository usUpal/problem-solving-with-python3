def fib2(n) -> int:
    if n<2:  # base case
        return n
    return fib2(n-2)+ fib2(n-1) # recursive case

if __name__ == "__main__":
    print(fib1(5))
    print(fib1(10))