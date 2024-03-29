def es10(ftext, k):
    
    with open(ftext) as f:
        text = f.read()
    ls_words = text.split('\n')
    for i in range(len(ls_words)-1, -1, -1):
        if len(ls_words[i]) != k:
            del ls_words[i]
    s = ''
    if ls_words == []:
        return s
    for i in range(k):
        d = dict()
        for par in ls_words:
            d[par[i]] = d.get(par[i], 0) + 1
        ls1 = list(d.values())
        m = max(ls1)
        if ls1.count(m) == 1:
            for c in d:
                if d[c] == m:
                    s += c
        else:
            ls2 = []
            for c in d:
                if d[c] == m:
                    ls2.append(c)
            ls2.sort()
            s += ls2[0]
    return s


'''
count = []
with open(ftext, encoding='utf8') as f:
    for line in f:
        for i in range(len(line)):
            if len(line[i]) == k:
                count.append(line[i])
    if not count:
                return ""

    result = []  
    for char in range(k):
        w = []
        for word in count:
            w.append(word[char])
    freq = {
        c : w.count(c) for c in w
    }
    charact = max(freq.items(), key = lambda tup: (tup[1],-ord(tup[0])))[0]
    result.append(charact)
    return "".join(result)

if __name__ == "__main__":
    print(es10('ft9.txt', 3))
    
'''