def is_balanced(expression):
    # Create an empty stack to hold brackets
    stack = []

    # Define the brackets and their corresponding closing brackets
    brackets = {'(': ')', '[': ']', '{': '}'}

    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening bracket, add it to the stack
        if char in brackets.keys():
            stack.append(char)

        # If the character is a closing bracket, remove the last opening bracket from the stack and check if they match
        elif char in brackets.values():
            # If the stack is empty, or the last opening bracket does not match the current closing bracket, return False
            if not stack or brackets[stack.pop()] != char:
                return False

    # After checking all the brackets in the expression, if the stack is not empty, there are unmatched opening brackets. Return False.
    # If the stack is empty, all brackets in the expression are balanced. Return True.
    return not stack



expression1 = "([]{})"
expression2 = "{[()]}"
expression3 = "((]]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  
print(is_balanced(expression3))