class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            currVal = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, currVal)

        return arr
            

