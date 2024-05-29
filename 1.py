# 题意：给定2个字符串：source 和 target，你可以通过至少多少个source拼接成target，允许将source删除若干个字符（但保持相对顺序）。

# hr您好，由于我很少用python写算法题，平时都用C++，所以可能写法比较难看，但做法应该没问题，用C++写的话可以更严谨
# 该做法的时间复杂度为O(m)


source = "abc"
target = "abcbc"

def solution(source, target):
    n, m = len(source), len(target)
    
    # 若target中存在source中没有的字符，则一定不行
    source_st = set()
    for i in range(0, n):
        source_st.add(source[i])
    for i in range(0, m):
        if target[i] not in source_st:
            return -1
    
    # nex[i][j]表示source[i]的下一位字符j所在的位置
    nex = [[-1 for _ in range(0, 26)] for _ in range(0, n)]

    nex[n - 1][ord(source[n - 1]) - ord('a')] = n - 1

    for i in range(n - 2, -1, -1):
        for j in range(0, 26):
            nex[i][j] = nex[i + 1][j]
        nex[i][ord(source[i]) - ord('a')] = i

    # for i in range(0, n):
    #     for j in range(0, 26):
    #         print(nex[i][j], end=' ')
    #     print('')
    
    ans = 0
    # i是target的指针
    i = 0
    while i < m:
        # 使用了一次source
        ans += 1
        j = 0
        while j < n - 1:
            if j > 0 and target[i] == target[i - 1]:
                j += 1
            if j >= n:
                break
            
            if nex[j][ord(target[i]) - ord('a')] == -1:
                break

            j = nex[j][ord(target[i]) - ord('a')]
            i += 1
            if i == m:
                break
    return ans

        
        

print(solution(source, target))