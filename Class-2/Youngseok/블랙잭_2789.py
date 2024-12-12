n, m = map(int, input().split())
nums = list(map(int, input().split()))
maxsum, l = 0, len(nums)
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            sum = nums[i]+nums[j]+nums[k]
            if sum <= m and maxsum < sum: maxsum = sum
print(maxsum)