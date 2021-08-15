if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    from builtins import hash as h
    print(h(integer_list))
