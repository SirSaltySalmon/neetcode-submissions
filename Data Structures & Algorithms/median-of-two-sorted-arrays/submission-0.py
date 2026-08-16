class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        l, r = 0, len(nums1)

        while l <= r:
            # i = number of elements taken from nums1
            i = (l + r) // 2

            # j = number of elements taken from nums2
            j = half - i

            # Values immediately to the left/right of each partition
            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < len(nums1) else float("inf")

            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < len(nums2) else float("inf")

            # Valid partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                left_max = max(nums1_left, nums2_left)

                if total % 2 == 1:
                    return float(left_max)

                right_min = min(nums1_right, nums2_right)
                return (left_max + right_min) / 2

            # Too many elements chosen from nums1
            elif nums1_left > nums2_right:
                r = i - 1

            # Too few elements chosen from nums1
            else:
                l = i + 1