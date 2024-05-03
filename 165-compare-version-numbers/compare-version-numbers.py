class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        for i in range(max(len(version1), len(version2))):
            w1 = int(version1[i]) if i < len(version1) else 0
            w2 = int(version2[i]) if i < len(version2) else 0

            if w1<w2:
                return -1
            elif w1>w2:
                return 1

        return 0
