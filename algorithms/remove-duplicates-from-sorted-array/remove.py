def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    chars = {}
    index = 0

    while (index < len(nums)):
        element = nums[index]

        if (element in chars.keys()):
            del nums[index]
        else:
            chars[element] = 1
            index += 1

    return len(nums)
