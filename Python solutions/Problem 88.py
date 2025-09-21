class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = nums1[:m]
        nums1 = nums1 + nums2
