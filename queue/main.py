
def sortPeople(names: list[str], heights: list[int]) -> list[str]:
        dic = {}
        res = []
        for i in range(len(names)):
            dic[names[i]] = heights[i]
        
        dic2 = dict(sorted(dic.items(), key = lambda item: item[1], reverse = True))
        for i in dic2:
            res.append(i)
        return res

if __name__ == "__main__":
    names = ["Alice","Bob","Bob"]
    heights = [155,185,150]
    print(sortPeople(names, heights))
