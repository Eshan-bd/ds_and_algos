
def parent(n):
    a = n+1
    return (-1 if a==1 else int(a/2))-1

def left_child(n):
    return (n+1)*2 -1

def bubble_up(pq, p):
    """ @param
    q priority queue
    p position
    """
    if (parent(p) < 0):
        return
    if pq[parent(p)] > pq[p]:
        pq[parent(p)], pq[p] = pq[p], pq[parent(p)]
        bubble_up(pq, parent)

def insert(pq, x):
    """ @params
    pq: priority queue
    x: new item
    """
    pq.append(x)
    bubble_up(pq, len(pq)-1)

def make_heap(pq, s):
    for i in s:
        insert(pq, i)

def extract_min(pq):
    min = -1

    if len(pq) == 0:
        print("Empty priority queue.\n")
    else:
        min = pq[0]
        pq[0] = pq[len(pq)-1]
        bubble_down(pq, 0)

    return min

def bubble_down(pq, p):
    c = 0 # Child index
    min_index = 0

    c = left_child(p)
    min_index = p

    for i in range(0, 2):
        if c+i <= len(pq):
            if pq[min_index] > pq[c+i]:
                min_index = c+i

    if min_index != p:
        pq[p], pq[min_index] = pq[min_index], pq[p]
        bubble_down(pq, min_index)

def heapsort(s):
    pq = []

    make_heap(pq, s)

    for i in range(0, len(s)-1):
        s[i] = extract_min(pq)

def main():
    s = [5, 2, 7, 4, 2, 6, 1, 0]
    heapsort(s)

    print('[%s]' % ', '.join(map(str, s)))   

if __name__ == '__main__':
    main()
