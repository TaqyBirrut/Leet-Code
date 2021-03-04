def angkatunggal(nums):
  for i in nums:
    total = nums.count(i)
    if total == 1:
      return i

def main():
  nums = [4,2,2]
  print(angkatunggal(nums))
main()
