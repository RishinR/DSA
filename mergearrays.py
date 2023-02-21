nums1 = [4,0,0,0,0,0]
nums2 = [1,2,3,5,6]
m = len(nums1) - len(nums2)
n = len(nums2)
i = m-1
j = n-1
k = m+n-1
while i >=0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1