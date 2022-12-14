#!/usr/bin/python3
"""
Module contains the Store class and the print_stats function
"""
import sys


class Store:
    """
    Stores state of statuses
    """
    def __init__(self):
        """
        Initializes an instance of teh Store class
        """
        self.filesize = 0
        self.status = dict.fromkeys(
            ["200", "301", "400", "401", "403", "404", "405", "500"], 0)

    def update_store(self, filesize, status):
        """
        Updates the attributes of a store instance
        """
        self.filesize += filesize
        self.status[status] += 1

    def print_store(self):
        """
        Prints the attributes of an instance of the Store class
        """
        print("File size: {}".format(self.filesize))
        for status in sorted(self.status.keys()):
            if self.status[status] > 0:
                print("{}: {}".format(status, self.status[status]))


def print_stats():
    """
    Prints stats from a log
    """
    store = Store()
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            words = line.split()
            status = words[7]
            filesize = int(words[8])
            store.update_store(filesize, status)
            if count >= 10 and count % 10 == 0:
                store.print_store()
    except Exception:
        pass
    finally:
        store.print_store()


if __name__ == "__main__":
    print_stats()
