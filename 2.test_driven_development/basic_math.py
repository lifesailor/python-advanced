import os

# developer
def div(n1, n2):
    return n1 / n2


def sortlist(lst):
    # copy list
    alist = lst[:]

    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            # if alist[i] > alist[i+1]:
            if alist[i] < alist[i+1]:
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp
    return alist


def openfile(filename):
    # QA asks a developer raise an exception
    if not os.path.exists(filename):
        raise FileNotFoundError
        # return

    open(filename)
