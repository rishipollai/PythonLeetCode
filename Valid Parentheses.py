class Solution:
    def isValid(self, s: str) -> bool:
        dict_list = {'(':')','{':'}','[':']'}
        stack = []
        if len(s)<= 1 :
            return False
        for char in s:
            if char in dict_list.keys():
                stack.append(char)
            elif(stack):
                popped_element= stack.pop()
                if dict_list[popped_element]!=char:
                    return False
            else:
                return False
        if (stack): return False
        else:
            return True
                
