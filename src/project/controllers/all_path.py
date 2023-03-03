from sys import path as path


def above_directory():
    arr = path[0].split('/')
    arr.pop()
    return '/'.join(arr)