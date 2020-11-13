import threading
import time

x = 0


def increment_global():
    global x
    x += 1


def task_of_thread(lock=None):
    # define a range of 50.000, since we have two threads
    # the end result should be 100.000
    for _ in range(50000):
        if lock is not None:
            lock.acquire()
        increment_global()
        if lock is not None:
            lock.release()


def main(fixed=False):
    global x
    x = 0

    # create two threads to demonstrate race condition
    t1 = threading.Thread(target=task_of_thread)
    t2 = threading.Thread(target=task_of_thread)

    if fixed:
        # introduce a lock
        lock = threading.Lock()
        t1 = threading.Thread(target=task_of_thread, args=(lock,))
        t2 = threading.Thread(target=task_of_thread, args=(lock,))

    t1.start()
    t2.start()

    """
    https://stackoverflow.com/questions/15085348/what-is-the-use-of-join-in-python-threading
    join([timeout]) Wait until the thread terminates. This blocks the calling thread until the thread whose join() 
    method is called terminates – either normally or through an unhandled exception – or until the optional timeout occurs.
    """
    t1.join()
    t2.join()


if __name__ == "__main__":
    # indicate if you want with or without race condition fix
    fixed = True

    start = time.time()
    for i in range(3):
        main(fixed)
        print("x = {1} after Iteration {0}".format(i, x))
    end = time.time()
    print("Total time it took: {1}s".format(i, end-start))
