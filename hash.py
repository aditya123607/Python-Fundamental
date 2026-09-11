def move_nonzero_right(arr):

    pos = 0
    for num in arr:
        if num != 0:
            arr[pos] = num
            pos += 1

    while pos < len(arr):
        arr[pos] = 0
        pos += 1
        return arr

    arr = [1,0,2,0,0,0,0]
    output = move_nonzero_right(arr)
    print(output) #[1,2,0,0,0,0,0]