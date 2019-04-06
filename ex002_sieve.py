import time

class sieve1:
    def __init__(self, n):
        self.wn = n**.5
        self.sieve = list(range(n,1,-1))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            p = self.sieve.pop()
            if p < self.wn: 
                self.sieve = [k for k in self.sieve if k%p]
            return p
        except:
            raise StopIteration()

def sieve2(n):
    wn = n**.5
    si = list(range(n,1,-1))
    while len(si)>0:
        p = si.pop()
        if p < wn:
            si = [k for k in si if k%p]
        yield p

class sieve3:
    def __init__(self, n):
        self.wn = n**.5
        self.sieve = list(range(n,1,-1))

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.sieve) > 0:
            p = self.sieve.pop()
            if p < self.wn: 
                self.sieve = [k for k in self.sieve if k%p]
            return p
        else:
            raise StopIteration()

sieve = sieve2


def times(n):
    a = time.time()
    _ = list(sieve1(n))
    b = time.time()
    a = time.time()
    _ = list(sieve1(n))
    b = time.time()
    print(f"sieve 1: {b-a}")
    a = time.time()
    _ = list(sieve2(n))
    b = time.time()
    print(f"sieve 2: {b-a}")


