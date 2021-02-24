def arrayUrut(nums1,m,nums2,n):
    maxArray = m + n
    newList = [] * maxArray
    for i in nums1:
        while i == 0:
            nums1.remove(0)
            i+=1
    newList.extend(nums1)
    

    for o in nums2:
        while o == 0:
            nums2.remove(0)
            o+=1
    newList.extend(nums2)

    newList.sort()
    newList.remove(0)
    
    return newList

def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6,]
    n = 3
    print(arrayUrut(nums1,m,nums2,n))
main()
