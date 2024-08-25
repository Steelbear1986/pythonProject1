
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        answer=sorted(items1+items2)
        i=0
        j=1
        dlina=len(answer)
        while j <dlina:
                if answer[i][0]==answer[j][0]:
                   answer[i]=[answer[i][0],(answer[i][1]+answer[j][1])]
                   answer=answer[:j]+answer[j+1:]
                   dlina-=1
                else:
                   i+=1
                   j+=1
        return answer