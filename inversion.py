#!/usr/bin/python

import sys

def merge_and_count_split(left, right, n):
    i = j = 0
    sorted_array = []
    inversions = 0
    for k in xrange(n):
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


def get_inversion(array):
    n = len(array)
    if n <= 1: return (array, 0)
    (left,x) = get_inversion(array[:n/2])
    (right,y) = get_inversion(array[n/2:])
    (sorted_array,z) = merge_and_count_split(left,right,n)
    return (sorted_array,x+y+z)

def read_n_convert_to_array(name):
    with open(name) as f:
        array = f.readlines()
    return [int(x.strip()) for x in array]

def main():

    if len(sys.argv) < 2:
        print 'Please input a file containing integers'
        exit(0)
    name = sys.argv[1]
    array = read_n_convert_to_array(name)
    print 'No of inversions ',get_inversion(array)[1]

if __name__ == '__main__':
    main()
