from multiprocessing import Process
import time
import os


def sleeper(slp_p):
    time.sleep(slp_p)
    print(f"Process {os.getpid()} has been finished")


if __name__ == "__main__":
    p = Process(target=sleeper, args=(10,))
    p_1 = Process(target=sleeper, args=(15,))
    p.start()
    p_1.start()
    print("Two processes has been started")
    p.join()
    p_1.join()
    print(f"Program is main process {os.getpid()} has been finished")
