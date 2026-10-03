class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        #treat every pair as opposite corners --> n^2
        #I originally was tring to iterate through every 3 points, and fill in the remaining point,
        #which would take n^3

        points_set = set()
        res = float('inf')

        for x, y in points:
            points_set.add((x, y))
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if (x1 != x2 and y1 != y2 and (x1, y2) in points_set and (x2, y1) in points_set):
                    area = abs(x1 - x2) * abs(y1 - y2)
                    res = min(res, area)
        
        return res if res < float('inf') else 0


        