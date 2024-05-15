class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            # ^^ why does this work?? we haven't confirmed if board[r][c] == word[i] yet??
            # OH! becuase len() is 1-indexed, not 0-indexed. so if this condition is true
            # it means you've actually already found the word's full path

            if (
                r < 0 or c < 0 or         # if current row or col is out of bounds (top, left)
                r >= ROWS or c >= COLS or # if current row or col is out of bounds (bottom, right)
                (r, c) in path or         # if this cell is already in our path
                board[r][c] != word[i]    # if this cell's value doesn't match the value we're looking for
            ):
                return False              # break

            path.add((r, c))              # otherwise this cell *is* in the path. add it to the set
                                          # THEN: look for next letter in word (in cells around last cell)
            res = (dfs(r + 1, c, i + 1) or    # if any one of these returns true, 'res' -> 'True'
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or    # then you remove the last cell from the set? OH-- same as
                   dfs(r, c - 1, i + 1))      # above: the last cell is actually past the end of your word
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # see explanation below as to how/ why this works
                    return True
        return False

# ** recursion + if-statement return
# so for each cell, it's going to look for a full path *starting* from that cell
# if you reach the end of the word from your starting cell path, then it returns
# True and you're done.

# I think I was thinking this would return 'True' for every intermittent 'True'
# found as you're traversing the cells from your starting cell. But that's not
# what happens. True is only returned from 'dfs'' *if* the "i == len(word)"
# statement is satisfied.
