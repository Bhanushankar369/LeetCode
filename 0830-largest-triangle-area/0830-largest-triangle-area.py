class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(point1, point2, point3):
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3

            return 1/2 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

        max_ = 0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    max_ = max(area(points[i], points[j], points[k]), max_)
        
        return max_