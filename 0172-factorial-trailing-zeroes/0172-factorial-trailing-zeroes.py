class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        twos = 0
        fives = 0
        while n > 0:
            n_copy = n
            if n % 10 == 0:
                n_copy //= 10
                zeros += 1
            elif n % 2 == 0:
                twos += 1

            if (n_copy % 5) == 0:
                while n_copy % 5 == 0 and n_copy:
                    fives += 1
                    n_copy //= 5
            
            n -= 1
        print(zeros, twos, fives)
        return zeros + min(twos, fives)

        