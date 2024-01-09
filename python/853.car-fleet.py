#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stack = []
        result_stack = []
        for p, s in zip(position, speed):
            car_stack.append([p, s])
        
        for position_car_stack, speed_car_stack in sorted(car_stack, reverse=True):
            result_stack.append((target - position_car_stack)/speed_car_stack)

            if len(result_stack) >= 2 and result_stack[-1] <= result_stack[-2]:
                result_stack.pop()
        
        return len(result_stack)
# @lc code=end

