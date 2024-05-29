
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answers = []
    prefix = 1
    for i in range(len(nums)):
        answers.append(prefix)
        prefix = prefix * nums[i]
    suffixe = 1
    for i in range(len(nums)-1,-1,-1):
        answers[i] *= suffixe
        suffixe *= nums[i]
    return answers
print(productExceptSelf([1,2,3,4]))
