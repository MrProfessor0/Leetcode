def solution(arr:list[int])->int:
    start = 0
    end = len(arr)-1

    while(start < end):
        mid = (start+end)//2
        if arr[mid] < arr[mid+1]:
            start = mid + 1
            continue
        else:
            end = mid
            continue
    return start

if __name__ == '__main__':
    # arr = [0,2,1,0]
    # arr = [0,10,5,2,1]
    arr = [1,2,5,10,0]
    print(solution(arr))
