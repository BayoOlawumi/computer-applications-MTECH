
import sys

def test(is_palindrome):
    lineno = sys._getframe(1).f_lineno
    if is_palindrome == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)


# A function that check if it is palindrome

def is_palindrome(args):
    mirrored = ""
    each = -1
    while each >= -len(args):
        letter = args[each]
        # Append string from behind
        mirrored += letter
        each -= 1
    # Check if the word is really pallindrome
    if args == mirrored:
        return True
    else:
        return False

def test_suite():
    # Passed Test
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))


test_suite()