import timeit


def message():
    #printing only 2 hello.dont know the reason
    print "hello"

#timeit.repeat("message()","",number=2)
timeit.repeat("message()",setup="from __main__ import message",timer=3, number=5)