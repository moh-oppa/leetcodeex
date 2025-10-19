def validAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    MapS, MapT = {}, {}
    for i in range(len(s)):
        MapS[s[i]] = 1 + MapS.get(s[i], 0)
        MapT[t[i]] = 1 + MapT.get(t[i], 0)
        # print (MapS)
        # print (MapT)

    for c in MapS:
        if MapS[c] != MapT.get(c, 0):
            print(MapS)
            print(MapT)
            return False

    return True


s = "anagram"
t = "anargma"
print(validAnagram(s, t))
