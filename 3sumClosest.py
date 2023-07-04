class Solution(object):
    def threeSumClosest(self, nums, target):
        triplets = []
        n = len(nums)

        # Sorting the array
        nums.sort()

        # Initialize the closest sum with a large value
        closest_sum = float('inf')

        for i in range(n-2):
            # Skipping duplicate values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update the closest sum if necessary
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Found an exact match

        return closest_sum
