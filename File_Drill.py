import os
import time

def start():
    fPath = "/Users/cameronhackwith/Documents/School_Projects/Basic_Python_Projects/Drill/"
    files = os.listdir(fPath)
    find_txt(files)
    

def find_txt(files):
    lst = []
    access = []
    for i in files:
        if i[-1:-4:-1] == "txt":
            lst.append(i)
    try:
        for file in lst:
            fPath = "/Users/cameronhackwith/Documents/School_Projects/Basic_Python_Projects/Drill/"
            fName = file
            abPath = os.path.join(fPath, fName)
            local_time = os.path.getmtime(abPath)
            access.append(time.localtime(local_time))
    except OSError:
        print("File cannot be found")
    for x, y in zip(lst, access):
        print("{} was last modified on {}...".format(x, time.asctime(y)))


if __name__ == "__main__":
    start()

