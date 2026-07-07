class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res = []

        i = 0 
        curr_row = []
        row_length = 0

        while i < len(words):
            curr_word = words[i]
            if row_length != 0 and row_length + 1 + len(curr_word) > maxWidth :
                diff = maxWidth - row_length
                while diff > 0:
                    if len(curr_row) == 1:
                        curr_row[0] += ' '
                        diff -= 1
                    else:
                        for j in range(len(curr_row) - 1):
                            if diff == 0:
                                break
                            curr_row[j] += ' '
                            diff -= 1
                res.append("".join(curr_row))
                curr_row = []
                row_length = 0
            else:
                if not curr_row:
                    curr_row.append(curr_word)
                    row_length += len(curr_word)
                else:
                    curr_row[-1] += ' '
                    row_length += 1 + len(curr_word)
                    curr_row.append(curr_word)
                i += 1
        
        last = "".join(curr_row)
        while len(last) < maxWidth:
            last += " "
        res.append(last)
        
        return res







