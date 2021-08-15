if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l1=list(arr)
    l1ma=max(l1)
    while l1ma in l1:
        l1.remove(l1ma)

    print(max(l1)) 
