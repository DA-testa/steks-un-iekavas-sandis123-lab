# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i, next))
            # Process opening bracket, write your code here
            
            
        if next in ")]}":
 
            if len(opening_brackets_stack) == 0:
                return i + 1
          top = opening_brackets_stack.pop()
               
                    if not are_matching(top[0], next):
                       
                        return i + 1
                
        

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[-1][1] + 1
    else:
        return 0

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch != 0:
        print(mismatch)
        return 0
    print("Success")
    return 0



if __name__ == "__main__":
    main()
