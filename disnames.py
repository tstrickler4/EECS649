VOWELS = ['a','e','i','o','u','y']

class Find:
    def __init__(self):
        self._prev = {}
        self._next = {}

    def __repr__(self):
        return "<Find(prev={}, next={})>".format(repr(self._prev), repr(self._next))

    def __str__(self):
        precede = [repr(i) + (" ({})".format(j) if j > 1 else "")
                for i,j in self._prev.items()]
        follow = [repr(i) + (" ({})".format(j) if j > 1 else "")
                for i,j in self._next.items()]
        return "Preceded by: {}\nFollowed by: {}\n".format(
                ', '.join(precede), ', '.join(follow))

    preceding = property(lambda self: self._prev)
    following = property(lambda self: self._next)

    def prev(self, item):
        if not hasattr(self._prev, item):
            self._prev[item] = 0
        self._prev[item] += 1

    def next(self, item):
        if not hasattr(self._next, item):
            self._next[item] = 0
        self._next[item] += 1

def consclusters(names, truncate_final_e=True):
    '''
    Parse a list of names into a dict whose keys are diphthongs
    (vowel clusters) and values are the consonant clusters that precede/follow them
    '''
    ret = {}
    for name in names:
        cons = ""
        diphthong = ""
        last_diph = ""
        for i in name:
            i = i.lower()
            if i not in VOWELS:
                #if we've been getting vowels
                if diphthong:
                    if ret.get(diphthong) is None:
                        ret[diphthong] = Find()
                    #we finished getting the diphthong
                    ret[diphthong].prev(cons)
                    if last_diph:
                        ret[last_diph].next(cons)
                    #update state
                    cons = ""
                    last_diph = diphthong
                    diphthong = ""
                cons += i
            else:
                diphthong += i
        #consonant termination
        if cons and not diphthong:
            ret[last_diph].next(cons)
        #vowel termination
        elif diphthong:
            if ret.get(diphthong) is None:
                ret[diphthong] = Find()
            #we finished getting the diphthong
            ret[diphthong].prev(cons)
            if last_diph:
                ret[last_diph].next(cons)
    return ret

def count(name):
    return len(consclusters([name]))

def print_dict(dict):
    [print(i + ":", str(j)) for i, j in dict.items()]

if __name__ == '__main__':
    test = consclusters(["Katie", "Jamie", "Ben", "Joe", "Alphonse"])
    ct = count(["Katie", "Jamie", "Ben", "Joe", "Alphonse"])
    print_dict(test)
    print_dict(ct)
