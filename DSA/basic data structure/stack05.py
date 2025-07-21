
from stack01 import Stack

def infix_to_postfix(infix_exp):
    # Define operator precedence
    prec = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1  # Lowest precedence to keep it in stack until ')'
    }
    
    op_stack = Stack()
    postfix_list = []
    token_list = infix_exp.split()

    for token in token_list:
        if token.isalnum():  # Check if operand (letters or numbers)
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            # Pop until matching '(' is found
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                if op_stack.is_empty():
                    raise ValueError("Mismatched parentheses")
                top_token = op_stack.pop()
        else:  # Operator
            # Pop higher or equal precedence operators
            while (not op_stack.is_empty()) and (prec.get(op_stack.peek(), 0) >= prec.get(token, 0)):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    
    # Empty the remaining operators
    while not op_stack.is_empty():
        token = op_stack.pop()
        if token == '(':
            raise ValueError("Mismatched parentheses")
        postfix_list.append(token)
    
    return " ".join(postfix_list)

# Test cases
print(infix_to_postfix("( A + B ) * ( C + D )"))  # Should output: A B + C D + *
print(infix_to_postfix("A + B * C"))             # Should output: A B C * +
print(infix_to_postfix("( A + B ) * C"))         # Should output: A B + C *



# from stack01 import Stack


# def infix_to_postfix(infix_exp):
#     prec = {}
#     prec["*"] = 3
#     prec["/"] = 3
#     prec["+"] = 2
#     prec["-"] = 2
#     prec["("] = 1
#     op_stack = Stack()
#     postfix_list = []
#     token_list = infix_exp.split()

#     for token in token_list:
#         if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
#             postfix_list.append(token)
#         elif token == "(":
#             op_stack.push(token)
#         elif token == ")":
#             top_token = op_stack.pop()
#             while top_token != '(':
#                 postfix_list.append(top_token)
#                 top_token = op_stack.pop()
#         else:
#             while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
#                 postfix_list.append(op_stack.pop())
#             op_stack.push(token)

#             while not op_stack.is_empty():
#                 postfix_list.append(op_stack.pop())
#             return " ".join(postfix_list)


# print(infix_to_postfix("( A + B ) * ( C + D )"))
