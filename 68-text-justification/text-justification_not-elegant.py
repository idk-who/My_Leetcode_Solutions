class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i = 0
        lines = [] ## [(line[], len_line), (line, len_line), ....]
        while i < len(words):
            line = []
            line_len = 0
            while line_len+len(words[i])<=maxWidth:
                line.append(words[i])
                line_len += (len(words[i]) + 1)
                i+=1
                if i >= len(words):
                    break
            lines.append((line, line_len-len(line)))
        
        justified_lines = []
        for i in range(len(lines)-1):
            line = lines[i][0]
            line_length = lines[i][1]
            spaces = len(line) - 1
            if spaces == 0:
                justified_lines.append(line[0]+" "*(maxWidth-len(line[0])))
                continue
            quotient = (maxWidth-line_length) // spaces
            remainder = (maxWidth-line_length) % spaces
            
            for i in range(spaces):
                if remainder > 0:
                    line[i] = line[i]+ (' '*(quotient + 1))
                    remainder -= 1
                else:
                    line[i] = line[i]+ (' '*(quotient))
            justified_lines.append("".join(line))
        

        lastline = " ".join(lines[-1][0])
        justified_lines.append(lastline+" "*(maxWidth-len(lastline)))

        return justified_lines
