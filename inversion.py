#!/usr/bin/python

def merge_and_count_split(left, right, n):
    i = j = 0
    sorted_array = []
    inversions = 0
    for k in range(n):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            inversions += len(left[i:])
            j += 1

        if i == len(left):
            sorted_array.extend(right[j:])
            break
        if j == len(right):
            sorted_array.extend(left[i:])
            break

    return (sorted_array, inversions)


def get_inversion(A,n):
    if n <= 1: return (A, 0)
    (left,x) = get_inversion(A[:n/2], n/2)
    (right,y) = get_inversion(A[n/2:], n-n/2)
    (sorted_array,z) = merge_and_count_split(left,right, n)
    return (sorted_array, x+y+z)

def main():
    A = [1,3,5,2,4,6]
    #A = [x for x in range(1000000)]
    #A.reverse()
    n = len(A)
    print 'No of inversions ',get_inversion(A,n)[1]

if __name__ == '__main__':
    main()
