#Dynamic Programming 

class LeetcodeSolutions:

    #70. Climbing Stairs

    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n 
        dyn = [-1] * (n+1)
        dyn[1] = 1
        dyn[2] = 2

        for x in range(3, n+1):
            dyn[x] = dyn[x-1] + dyn[x-2]
        
        return dyn[x]
