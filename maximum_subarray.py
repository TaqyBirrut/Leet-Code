def maxSubArray(nums):
        angkaMax = nums[0]
        total = 0
        
        for n in nums:
            if total < 0:
                total = 0
            total += n
            angkaMax = max(angkaMax, total)
        return angkaMax

def main():
  nums = [-2,1,-3,4,-1,2,1,-5,4]
  print(maxSubArray(nums))
main()
