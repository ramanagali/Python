class Solution(object):
    def decodeString(self, s):
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString


if __name__ == '__main__':
    s = Solution()
    data = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef", "abc3[cd]ef"]
    for d in data:
        print(s.decodeString(d))
