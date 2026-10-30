class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        is_valid = False
        for i in s:
            if not i in map_s:
                map_s[i] = map_s.get(i, 1)  
            else:
                map_s[i] += 1   

        for c in t:
            if not c in map_t:
                map_t[c] = map_t.get(c, 1)  
            else:
                map_t[c] += 1     
        print('MAPS', map_s, map_t)
        return True if map_s == map_t else False