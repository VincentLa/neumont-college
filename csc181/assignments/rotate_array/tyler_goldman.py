numsLista = input('please enter a list of numbers seperated with a comma. (No Spaces): ')
numsList = numsLista.split(',')
def rotateNums(nums, k):
    print(nums)
    while k > 0:
        numsList.insert(0,numsList.pop())
        k-=1
    print(nums) 
rotateNums(numsList,3)