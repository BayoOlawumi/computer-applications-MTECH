import sys

def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

def test(fn,result):
    lineno = sys._getframe(1).f_lineno
    if fn == result:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)


def return_items_present_both(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            result.append(xs[xi])
            xi += 1
            yi += 1
print("******************Return only those items that are present in both lists.**************************")
test(return_items_present_both(insertion_sort(['a','b','aab','ab','aba','c','was','like','p']), insertion_sort(['a','c','p','e','u'])) ,['a','c','p'])
test(return_items_present_both(insertion_sort([1,3,4,5,23,55,34,53,45]), insertion_sort([6,78,53,1,4,3,45])),[1,3,4,45,53])


def return_item_present_in_first_only(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.append(xs[yi:])
            print(result)
            return result

        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
        else:
            yi += 1

print("******************Return only those items that are present in the first list, but not in the second**************************")
test(return_item_present_in_first_only(insertion_sort([0, 1, 1, 2, 3, 4, 5, 7]), insertion_sort([1, 3, 5, 6, 7, 10])), [0,2,4])
test(return_item_present_in_first_only(insertion_sort([1,3,4,5,23,55,34,53,45]), insertion_sort([6,78,53,1,4,3,45])),[5,23,34,55])



def return_second_list_present_only(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            return result

        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] == ys[yi]:
            yi += 1
        else:
            result.append(ys[yi])
            yi += 1


print("******************Return only those items that are present in the second list, but not in the first.**************************")
test(return_second_list_present_only(insertion_sort([0, 1, 1, 2, 3, 4, 5, 7]), insertion_sort([1, 3, 5, 6, 7, 10])), [6,10])
test(return_second_list_present_only(insertion_sort([1,3,4,5,23,55,34,53,45]), insertion_sort([6,78,53,1,4,3,45])),[6,78])



def return_unique_items_in_both_lists(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1
        else:
            xi += 1
            yi += 1

print("******************Return items that are present in either the first or the second list.**************************")
test(return_unique_items_in_both_lists(insertion_sort([0, 1, 1, 2, 3, 4, 5, 7]), insertion_sort([1, 3, 5, 6, 7, 10])), [0, 1, 2, 4, 6, 10])
test(return_unique_items_in_both_lists(insertion_sort([1,3,4,5,23,55,34,53,45]), insertion_sort([6,78,53,1,4,3,45])),[5, 6, 23, 34, 55, 78])



def bagdiff(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            print(result)
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            print(result)
            return result

        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1


print("******************Return items from the first list that are not eliminated by a matching element**************************")
test(bagdiff(insertion_sort([1,3,4,5,23,55,34,53,45]), insertion_sort([6,78,53,1,4,3,45])),[5, 23, 34, 55, 78])
