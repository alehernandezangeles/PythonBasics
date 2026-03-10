def gensquares(n):
    for i in range(n):
        yield i ** 2;

def gen():
    for i in range(10):
        print('i =>', i)
        X = yield i ** 2
        print('X =>', X)

        if X == 88:
            return 89
        elif X == 99:
            return

def both(N):
    yield from range(N)
    yield from map(lambda x: x ** 2, range(N))

if __name__ == "__main__":
    for i in gensquares(5):
        print(i)

    print("Testing send()")
    G = gen()
    print(next(G))
    print(G.send(12))
#    print(G.send(99)) # Throws StopIteration exception, as expected

    print("Yield from")
    r = list(both(5))
    print(r)