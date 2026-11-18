class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        answ = []
        for idx,i in enumerate(path_list):
            if i == "":
                continue
            elif i == ".":
                continue
            elif i == "..":
                if len(answ)>0:
                    answ.pop()
            else:
                answ.append(i)
        return "/" + "/".join(answ)
                
        