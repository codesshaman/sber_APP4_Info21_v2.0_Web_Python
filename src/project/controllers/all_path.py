from sys import path as path


def above_directory():
    arr = path[0].split('/')
    arr.pop()
    return '/'.join(arr)

def above_two_directory():
    arr = path[0].split('/')
    arr.pop()
    arr.pop()
    return '/'.join(arr)