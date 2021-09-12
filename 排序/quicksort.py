'''class Solution:
    def quick(self,arr,left, right):
        if left >=right: return  # 1
        pivot = left
        l, r = left, right
        while l < r:
            while l < r and arr[r] > arr[pivot]: r -= 1  # 2
            while l < r and arr[l] <= arr[pivot]: l += 1
            arr[l], arr[r] = arr[r], arr[l]
        arr[l], arr[pivot] = arr[pivot], arr[l]
        self.quick(arr,left, r - 1)
        self.quick(arr,r + 1, right)
        return arr
    def quickSort(self,arr):
        n=len(arr)
        res=self.quick(arr,0,n-1)

        return res

sort=Solution()
res=sort.quickSort([5,1,95,32,66,22,11])
print(res)
'''
def quick_sort(nums):
    n = len(nums)

    def quick(left, right):
        if left >= right:
            return nums
        pivot = left
        i = left
        j = right
        while i < j:
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[pivot], nums[j] = nums[j], nums[pivot]
        quick(left, j - 1)
        quick(j + 1, right)
        return nums

    return quick(0, n - 1)
res=quick_sort([5,1,95,32,66,22,11])
print(res)

