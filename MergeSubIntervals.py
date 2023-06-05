class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals1 = sorted(intervals , key = lambda x:x[0])
        temp = [intervals1[0]]
        for i in intervals1[1:]:
            if(i[0] <= temp[-1][1]):
                temp[-1][1] = max(i[1],temp[-1][1])
            else:
                temp.append(i)
        return temp
