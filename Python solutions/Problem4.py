class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()

        if len(nums1)%2 != 0:
            return nums1[len(nums1)//2]

        n1 = len(nums1)/2 - 1
        n2 = len(nums1)/2

        return (nums1[int(n1)] + nums1[int(n2)])/2