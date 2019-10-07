# Merge Sort
# Divide and Conquer algorithm
# Funtion calls T(n) = n*2-1
# Time Complexity O(n) = nlgn

from collections import deque

def merge_sort(s, low, high):
    if low < high:
        middle = int( (low+high)/2 )
        merge_sort(s, low, middle)
        merge_sort(s, middle+1, high)
        #merge(s, low, middle, high)
    else:
        return


    buffer1 = deque(s[low : middle+1])
    buffer2 = deque(s[middle+1: high+1])
    
    i = low
    while buffer1 and buffer2:
        if buffer1[0] < buffer2[0]:
            s[i] = buffer1.popleft()
        else:
            s[i] = buffer2.popleft()
        i+=1

    while buffer1: 
        s[i] = buffer1.popleft()
        i += 1
    while buffer2: 
        s[i] = buffer2.popleft()
        i += 1 

def main():
    l = [4, 7, 3, 6, 8, 9, 8, 0, 3, 4]
    merge_sort(l, 0, len(l)-1)

    print('[%s]' % ', '.join(map(str, l)))

if __name__ == "__main__":
    main()
