# bad trial

# def valid_parentheses(head: str):
#     brackets = {"a": "(", "b": ")", "c": "{", "d": "}", "e": "[", "f": "]"}
#     check = []
#     for i in head:
#         for j in brackets:
#             if i == brackets[j]:
#                 check.append(brackets[j])

#     print(check)
#     if len(head) == 1:
#         return "invalid"
#     elif len(head) == 2:
#         if check[0] == check[1]:
#             return "valid"
#         else:
#             return "invalid"
#     elif len(head) == 3:
#         return "invalid"
#     elif len(head) == 4:
#         if check[0] == check[1] and check[2] == check[3] or check[0] == check[3] and check[1] == check[2]:
#             return "valid"
#         else:
#             return "invalid"
#     elif len(head) == 5:
#         return "invalid"
#     elif len(head) == 6:
#         if (
#             check[0] == check[1]
#             and check[2] == check[3]
#             and check[4] == check[5]
#             or check[0] == check[1]
#             and check[2] == check[3]
#             or check[0] == check[1]
#             or check[0] == check[3]
#             and check[1] == check[2]
#             or check[0] == check[5]
#             and check[1] == check[4]
#             and check[2] == check[3]
#         ):
#             return "valid"
#         else:
#             return "invalid"


# new method


def valid_parentheses(s: str):
    list = {"]": "[", ")": "(", "}": "{"}
    check = []

    for i in s:
        if i in list.values():
            check.append(i)
        elif i in list.keys():
            if not check or list[i] != check.pop():
                return False
    return not check


print(valid_parentheses(s="({}"))
