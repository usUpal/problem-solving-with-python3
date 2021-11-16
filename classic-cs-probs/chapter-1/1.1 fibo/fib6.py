from typing import Generator

def fib6(n) -> Generator[int, None, None]:
    #! special case
    yield 0  # no equal

    if n > 0: yield 1 #! special case
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next #! main generation step
    
if __name__ == "__main__":
    for i in fib6(10):
        print(i)
