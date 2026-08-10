from day_36.day_36_stock_news.main import difference


class Solution:
    def asteroidCollision(self, asteroids):
        '''
        asteroids: List[int] - array of integers representing asteroids
        asterioids = [-1,3,2,-3]
        diff = 2+(-3) = -3 asteriods.pop() or asteriosd = 0

        diff =

        '''
        stack = []
        for i in asteroids:
           while stack and stack[-1] > 0 and i < 0:
               difference = stack[i] + i
               if difference < 0:
                   stack.pop()
               elif difference > 0:
                   i = 0
                   # loop will break
               else:
                   a = 0
                   stack.pop()
        if i:
           stack.append(i)
        return stack