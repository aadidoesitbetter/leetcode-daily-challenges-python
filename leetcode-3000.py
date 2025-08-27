class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        max_diag_sq = 0 
        max_area = 0
        for dim in dimensions:
            l, w = dim[0], dim[1]
            diag_sq = l * l + w * w 
            area = l * w
            if diag_sq > max_diag_sq or (diag_sq == max_diag_sq and area > max_area):
                max_diag_sq = diag_sq
                max_area = area
        return max_area