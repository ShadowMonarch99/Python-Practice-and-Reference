if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    for i in range(0,n):
        if arr[i]<max(arr):
            print arr[i]
            break

    
