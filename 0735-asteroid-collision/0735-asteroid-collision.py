class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 1. restate problem in own words
        # 2. Input constraints and edge cases: how large is the array? Weight limit? Can the asteroid crush mutiple asteroid in a row? 0 value astroids?
        # 3. Examples: [5, 10, -5, -5] --> [5, 10]? 
        #    What is the order of collision? [ 5, 10, -5, 20, -30] -> [-30]
        #    [5, 10, -7, 20, -15] -> [20]
        #    So basically at the end all of the asteroids are moving in the same direction
        # 4. Discuss at least 2 approaches 
        # [ 5, 10, -5, 20, -30] 
        #  stack [5, 10] if i encounter a -5, I crush it aginst the top of the stack, if the asteroid gets destroyed I continue to iterate through the array, add whatever positive number to the top of the stack and whenever I run into a negative number I crush the asteroid against the stack 
        stack1 = []
        stack2 = []
        res = []
        for n in asteroids:
            if n > 0:
                stack1.append(n)
            if n < 0:
                stack2.append(n)
            while stack1 and stack2:
                print(stack1, stack2)
                if stack1[-1] > - 1 * stack2[-1]:
                    stack2.pop()
                elif stack1[-1] < -1 * stack2[-1]:
                    stack1.pop()
                else:
                    stack1.pop()
                    stack2.pop()
            if not stack1:
                res += stack2 
                stack2 = []
        
        return res + stack1