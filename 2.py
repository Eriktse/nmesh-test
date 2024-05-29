input = """bge)))))))))
((IIII))))))
()()()()(uuu
))))UUUU((()"""

def solution(input):
    # 将输入分行
    lines = input.split()
    for line in lines:
        # 用栈模拟，标记所有合法的括号即可
        vis = [0] * len(line)
        # vis[i] = true表示该字符合法
        stk, top, i = [0] * int(1e5), 0, 0
        while i < len(line):
            if line[i] == '(':
                top += 1
                stk[top] = i
            elif line[i] == ')':
                if top > 0:
                    # 存在左括号
                    vis[stk[top]] = True
                    vis[i] = True
                    top -= 1
            i += 1

        
        print(line)
        i = 0
        while i < len(line):
            if not vis[i]:
                if line[i] == '(':
                    print("x", end='')
                elif line[i] == ')':
                    print("?", end='')
                else:
                    print(" ",end='')
            else:
                print(" ",end='')
            i += 1
        print()
        

solution(input)