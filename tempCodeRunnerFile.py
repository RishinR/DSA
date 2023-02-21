j = m
index = m
for i in nums2:
    nums1[index] = i
    index += 1
i = 0
while True:
    if nums1[i] <= nums1[j]:
        i += 1
    elif nums1[i] > nums1[j]:
        (nums1[i], nums1[j]) = (nums1[j], nums1[i])
        if i == j-1:
            j += 1
        else:
            i += 1
    if i == j == m+n-1:
        break