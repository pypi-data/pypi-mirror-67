import sys
from time import perf_counter


def wrap(iterator, n, file=sys.stdout):
    digits = len(str(n))
    fmt = '{:>3}% ({:>'+str(digits)+'}/{}) elapsed: {:.1f} sec'
    print(fmt.format(0, 0, n, 0), end='\r', file=file)
    fmt += '; estimate: {:.1f} sec'
    t0 = perf_counter()
    for i, item in enumerate(iterator):
        completed = i + 1
        pct = int(100 * completed / n)
        elapsed = perf_counter() - t0
        freq = elapsed / completed
        remaining = n - completed
        estimate = freq * remaining
        print(fmt.format(pct, completed, n, elapsed, estimate),
              end='\r', file=file)
        yield item
    print(file=file)


def test():
    import time

    n = 5
    def my_iterator():
        for i in range(n):
            time.sleep(2)
            yield None

    list(wrap(my_iterator(), n))


if __name__ == '__main__':
    test()
