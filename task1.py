class Stack:
 def ___init__(self):
  self.stack= []
def is_empty(self):
 return len(self.stack)==0
def push (self,item):
 self.stack.append(item)

def pop(self):
 if self.is_empty():
  return None
 return self.stack.pop()
def size(self):
 return len(self.stack)


def reverse_string(s:str)-> str:
 stack = Stack()
 for char in s: stack.push(char)
 reverse_str =""
 while not stack.is_empty():
  reversed_str += stack.pop()
  return reverse_str
 
 input_string =""
 output_string = reverse_str(input_string)
 print(f"{input_string}")
 print(f"{output_string}")