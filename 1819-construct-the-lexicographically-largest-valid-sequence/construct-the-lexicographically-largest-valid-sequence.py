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
                if i == 1:
                    seq[pos] = i
                    placed[i] = True
                    if rec(seq, pos+1):
                        return True
                    seq[pos] = -1
                    placed[i] = False
                else:
                    if pos+i > len(seq)-1:
                        continue
                    if seq[pos+i] != -1:
                        continue
                    seq[pos] = i
                    seq[pos+i] = i
                    placed[i] = True
                    if rec(seq, pos+1):
                        return True
                    seq[pos] = -1
                    seq[pos+i] = -1
                    placed[i] = False
                    
            return False
        
        rec(seq, 0)

        return seq