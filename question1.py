def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if char == ')' and top != '(' or \
               char == ']' and top != '[' or \
               char == '}' and top != '{':
                return False

    return len(stack) == 0

#test case
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2)) 