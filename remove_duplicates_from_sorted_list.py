def buangsama(nums):
    sekarang = 1
    sebelum = 0
    for i in nums:
   
        if nums[sekarang] == nums[sebelum]:
            del(nums[sebelum])
            sebelum = sekarang
            sekarang += 1

    return nums

def main():
	nums = [0,0,1,1,1,2,2,3,3,4]
	print(buangsama(nums))
main()
