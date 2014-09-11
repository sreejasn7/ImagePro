import threading

i=0
def ppp(i):
    i = int(i)
    i += 1
    t = threading.Timer(1, ppp, str(i))
    t.start()
    print "Hello, World!"
    if i == 10:
        t.cancel()


ppp(0)