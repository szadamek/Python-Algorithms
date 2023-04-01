def has_subset_with_sum_zero(nums):
    for i in range(len(nums)):
        subset_sum = nums[i]
        # if subset_sum == 0:
        #     return True
        for j in range(i+1, len(nums)):
            subset_sum += nums[j]
            # print(subset_sum)
            # if subset_sum == 0:
            #     return True
    return False


if __name__ == '__main__':
    nums = [5, -1, 3, 2]
    print(has_subset_with_sum_zero(nums))
