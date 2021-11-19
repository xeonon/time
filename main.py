import time


def xtime():
    curr = time.time()
    if check < curr:
        print("TIME!")
        end = time.time()
        print("start ", time.ctime(start), "end ", time.ctime(end))
        print(x)
        f = open("time.txt", "a")
        f.write(str(x) + "\n")
        f.close()
        raise SystemExit
    else:
        return


if __name__ == "__main__":
    x = 0
    print("Sleeping for 2 secs")
    delay = 2
    start = time.time()
    check = start + delay
    while 1:
        xtime()
        x += 1
