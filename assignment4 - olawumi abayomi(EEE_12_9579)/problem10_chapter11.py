import sys
def test(status):
    lineno = sys._getframe(1).f_lineno
    if status == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)



def replace(s, old, new):
    new_string = s.replace(old,new)
    return new_string


def test_replace_method():
    # Test
    test(replace("Mississippi",'i',"I") == 'MIssIssIppI')
    s = "I love spom! Spom is my favourite food. Spom, spom, yum!"
    test(replace(s,'om',"am") == "I love spam! Spam is my favourite food. Spam, spam, yum!")
    test(replace(s,'o',"a") == "I lave spam! Spam is my favaurite faad. Spam, spam, yum!")



test_replace_method()