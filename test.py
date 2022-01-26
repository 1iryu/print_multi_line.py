import time
import reprint


def print_processing_time(function):
    start_time = time.time()
    function()
    end_time = time.time()
    print(end_time-start_time)


reprint = Reprint.Reprint()
reprint2 = Reprint.ReprintVersion2()

def test_ver1():
    for i in range(100):
        list = [i, i+1, i+2]
        reprint.do(list)


def test_ver2():
    for i in range(100):
        list = [i, i+1, i+2]
        reprint2.do(list)


print_processing_time(test_ver1)
print_processing_time(test_ver2)
