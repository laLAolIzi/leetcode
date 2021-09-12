
def insertion_sort(a):
    # 取出列表长度
    num = len(arr)

    for i in range(1, num):
        left = 0
        right = i - 1
        temp = arr[i]
        # left一旦大于right，跳出循环
        while left <= right:
            # 取lift与right的中间位置（取整）
            mid = (left + right) // 2

            # 利用二分查找的特性，对中间位置的值与待插入数字比较
            # mid右边
            if arr[mid] < temp:
                left = mid + 1
            # mid左边
            else:
                right = mid - 1
                # 查找出temp应插入的位置后，将left后面的数字均向后移动一位
        j = i - 1
        while j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        # 此时left位置上放置待插入的数字
        arr[left] = temp
    print(a)


arr = [7, 9, 14, 51, 2, 8, 32]
insertion_sort(arr)
