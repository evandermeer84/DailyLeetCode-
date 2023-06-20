class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        divisor = 2*k + 1
        finalist = [-1] * length
        if length < divisor:
            return finalist 

        prefixSum = [0] * (length+1)
        for i in range(length):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        for i in range(k, length-k):
            finalist[i] = (prefixSum[i+k+1] - prefixSum[i-k])//divisor

        return finalist
