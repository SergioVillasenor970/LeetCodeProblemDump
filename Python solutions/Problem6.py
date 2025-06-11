def nums_of_elements_under(curRow: int,numRows: int) -> int:
    res = (numRows-curRow) + (numRows-curRow - 1)
    if res < 0:
        return 0
    else:
        return res

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        curRow = 1
        while curRow < numRows:
            curIndex = curRow-1
            res = res + s[curIndex]
            nextIndex = curIndex + nums_of_elements_under(curRow, numRows) + 1
            while nextIndex < len(s):
                res = res + s[nextIndex]
                curIndex = nextIndex
                nextIndex = curIndex + nums_of_elements_under(curRow, numRows) + 1
            curRow += 1
        return res