def combinations(nums):
    if not nums:
        return

    result = []
    def func(slate, poss):
        if len(poss) == 0:
            result.append(slate[:])
            return

        func(slate, poss[1:])
        slate.append(poss[0])
        func(slate, poss[1:])
        slate.pop()

    func(slate = [], poss = nums)
    return result


nums = [1, 2, 3]
print(combinations(nums))
