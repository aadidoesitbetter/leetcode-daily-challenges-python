import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        def extraPassRatio(p, t):
            return (p + 1) / (t + 1) - p / t

        maxHeap = [(-extraPassRatio(p, t), p, t) for p, t in classes]
        heapq.heapify(maxHeap)

        for _ in range(extraStudents):
            gain, p, t = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-extraPassRatio(p + 1, t + 1), p + 1, t + 1))

        return sum(p / t for _, p, t in maxHeap) / len(classes)
