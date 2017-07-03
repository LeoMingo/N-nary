def n_nary_map(dnum, nnmap, nbase):
    nmax = 1
    idx = 0
    while nmax*nbase <= dnum:
        nmax *= nbase
        idx += 1
    if idx > len(nnmap)-1:
        for i in xrange(idx-(len(nnmap)-1)):
            nnmap.append(0)
    if dnum < nbase:
    #For numbers that have nbase > 2
        nnmap[0] = dnum
        nmax = dnum
    else:
        nnmap[idx] += 1
    rest = dnum-nmax
    return rest, nnmap

def rev_n_nary(dnum, nbase, base_map=None):
    nnmap = []
    rest = dnum
    while rest != 0:
        rest, nnmap = n_nary_map(rest, nnmap, nbase)
    if base_map:
        nnmap = [base_map[i] for i in nnmap]
    return nnmap

def reverse(l):
    rev_l = []
    for i in xrange(1, len(l)+1):
        rev_l.append(l[-i])
    return rev_l


def n_nary(dnum, nbase, base_map=None):
    dnum = abs(dnum)
    nbase = abs(nbase)
    return reverse(rev_n_nary(dnum, nbase, base_map))


def base_map(nbase, bm):
    if nbase != len(bm):
        print "Error base map has a length that differs from number base"
        return
    else:
        bmap = [(i, mi) for i in xrange(nbase)
                        for mi in bm]
        return dict(bmap)

def nn_str(nnl):
    nnstr = ""
    for i in nnl:
        nnstr += str(i)
    return nnstr

def nn_to_dnum(nnl, nbase, base_map=None):
    nnl = reverse(nnl)
    dnum = 0
    if base_map:
        for i in xrange(len(nnl)):
            nnl[i] = base_map.index(nnl[i])
    for i in xrange(len(nnl)):
        dnum += nbase**i*nnl[i]
    return dnum

def n_nary_convert(num1, nbase1, nbase2,
                   base_map1=None, base_map2=None):
    dnum = nn_to_dnum(num1, nbase1, base_map1)
    return n_nary(dnum, nbase2, base_map2)

def get_key(dic, val):
    dici = dic.items()
    kl = [k for (k,v) in dici if v==val]
    return kl

