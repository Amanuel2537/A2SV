class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        val=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                val.append("FizzBuzz")
            elif i%3==0:
                val.append("Fizz")
            elif i%5==0:
                val.append("Buzz")
            else:
                val.append(str(i))
        return val