import os
import sys
import time


#example

# reprint = Reprint()
# for i in range(10):
#     list = [i,i+1,i+2]
#     reprint.do(list)
#     time.sleep(1)


class Reprint():
    def __init__(self):
        self.first = False
        self.lines_length = 0
        os.system("")

    def cursor_up(self, length: int):
        sys.stdout.write("\033[F" * length)

    def cursor_down(self, length: int):
        sys.stdout.write("\n" * length)



    def do(self, list_text: list):
        if(self.first == False):
            self.first = True
            self.lines_length = len(list_text)
            for text in list_text:
                print(text)
        if self.lines_length == len(list_text):
            list_text.reverse()
            for i in range(len(list_text)):
                self.cursor_up(i+1)
                print(list_text[i], end="")
                self.cursor_down(i+1)
        else:
            print("Incorrect count of rows")

