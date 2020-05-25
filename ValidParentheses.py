# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
# Input: "()"
# Output: true
#
# Example 2:
# Input: "()[]{}"
# Output: true
#
# Example 3:
# Input: "(]"
# Output: false
#
# Example 4:
# Input: "([)]"
# Output: false
#
# Example 5:
# Input: "{[]}"
# Output: true


def is_valid(s):
    d = {')': '(', '}': '{', ']': '['}
    stk = []
    for c in s:
        if c in ['(', '{', '[']:
            stk.append(c)
        else:
            if not stk or stk.pop() != d[c]:
                return False
    return stk == []


assert is_valid("") is True
assert is_valid("()") is True
assert is_valid("()[]{}") is True
assert is_valid("(]") is False
assert is_valid("([)]") is False
assert is_valid("{[]}") is True
