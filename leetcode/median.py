class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        i=0
        j=0
        result = []
        while(i < n1 and j < n2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        while (i<n1):
            result.append(nums1[i])
            i+=1
        while(j<n2):
            result.append(nums2[j])
            j+=1
        
        if len(result)%2 ==0:
            return (result[(len(result)/2) - 1] + result[len(result)/2])/2.0
        else:
            return result[len(result)/2]
            
# This solution is of the complexity O(n)

# Most optimized solution is O(log(min(m, n))). Uses binary search !!

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            A, B, m, n = nums2, nums1, n , m
        else:
            A, B = nums1, nums2
        
        if n==0:
            raise ValueError("n is zero")
        
        imin, imax, half_len = 0, m, (m+n+1)/2
        while imin <= imax:
            i = (imin+imax)/2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, Increase i
                imin = i+1
            elif i>0 and A[i-1] > B[j]:
                # Decrease i
                imax = i-1
            else:
                if i==0: max_of_left = B[j-1]
                elif j==0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])
                    
                if (m+n)%2 == 1:
                    return max_of_left
                
                if i==m: min_of_right = B[j]
                elif j==n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])
                
                return (max_of_left + min_of_right)/2.0