class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) -1 
        area = 0 
        while (right > left):
            length = min(height[right],height[left])
            width = right - left
            a = width * length
            area = max(a, area)
            if(height[right] > height[left]):
                left += 1
            else:
                right -= 1

        return area

        