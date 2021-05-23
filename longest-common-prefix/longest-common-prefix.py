class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ## if strs is empty return ""
        if len(strs) == 0:
            return ""
        
        ## if any string in strs is empty return "" since no common prefix for it
        for string in strs:
            if len(string) == 0:
                return ""
        ## find the length of all the strings, to find the shortest length
        len_list = list(map(len, strs))
        max_common_prefix_length = min(len_list)
        
        common_prefix_string = ""
        i=0
        
        ## the common_prefix length can be at max the length of the shortest string in strs
        while i < max_common_prefix_length:
            all_match_flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    all_match_flag = False
                    break
            
            if all_match_flag:
                common_prefix_string += strs[0][i]
                i += 1
            else:
                return common_prefix_string
            
        
        return common_prefix_string
        