class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        result = []

        for alpha in s:
            if alpha == "(":
                count+=1
            elif alpha == ")":
                if count == 0:
                    continue
                count-=1
            result.append(alpha)

        update = []
        openNeeded = count

        for alpha in reversed(result):
            if alpha == "(" and openNeeded > 0:
                openNeeded -=1
                continue
            update.append(alpha)

        return "".join(reversed(update))
