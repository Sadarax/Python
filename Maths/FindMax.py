# NguyenU
def find_max(nums):
    max = nums[0]
    for x in nums:
      if x > max:
        max = x
    print(max)

def main():
    start = 0
    list1 = []
    while start < 5:
        numbers = int(input("Enter numbers: "))
        start += 1
        list1.insert(0,numbers)
    find_max(list1)
    #print(list1)
        


main()
