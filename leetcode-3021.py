class Solution:
    def flowerGame(self, n, m):
        n_odd = (n + 1) // 2
        n_even = n // 2
        m_odd = (m + 1) // 2
        m_even = m // 2
        
        case1_pairs = n_odd * m_even
        case2_pairs = n_even * m_odd
        
        return case1_pairs + case2_pairs