# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        stack = []
        for i in range(len(height)):
            if not stack:
                stack.append(i)
            # 单调小于等于栈
            else:
                while stack and height[i] > height[stack[-1]]:
                    bot_index = stack.pop()
                    if stack:
                        area += (min(height[stack[-1]], height[i]) - height[bot_index]) * (i - stack[-1] - 1)
                        print(area)
                stack.append(i)
        return area

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))