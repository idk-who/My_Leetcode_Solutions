class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [-1]*(2*n-1)
        placed = [False]*(n+1)

        def rec(seq, pos):
            if pos == len(seq):
                return True
            if seq[pos] != -1:
                return rec(seq, pos+1)
            for i in range(n, 0, -1):
                if placed[i]:
                    continue
                seq[pos] = i
                placed[i] = True
                if i == 1:
                    if rec(seq, pos+1):
                        return True
                else:
                    if pos+i < len(seq) and seq[pos+i] == -1:
                        seq[pos+i] = i
                        if rec(seq, pos+1):
                            return True
                        seq[pos+i] = -1
                seq[pos] = -1
                placed[i] = False
                    
            return False
        
        rec(seq, 0)

        return seq