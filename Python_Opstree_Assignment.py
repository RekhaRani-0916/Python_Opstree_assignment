class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result[::-1]
    
    def print_list(self):
        print(''.join(map(str, self.traverse())))

def create_linked_list_from_number(number):
    linked_list = LinkedList()
    for digit in str(number):
        linked_list.append(int(digit))
    return linked_list

def add_linked_lists(l1, l2):
    result = LinkedList()
    p, q = l1.head, l2.head
    carry = 0
    while p or q or carry:
        x = p.data if p else 0
        y = q.data if q else 0
        total = x + y + carry
        carry = total // 10
        result.append(total % 10)
        if p: p = p.next
        if q: q = q.next
    return result

def subtract_linked_lists(l1, l2):
    result = LinkedList()
    p, q = l1.head, l2.head
    borrow = 0
    negative = False
    
    # Check if l1 < l2
    num1 = int(''.join(map(str, l1.traverse())))
    num2 = int(''.join(map(str, l2.traverse())))
    if num1 < num2:
        p, q = l2.head, l1.head
        negative = True
    
    while p:
        x = p.data - borrow
        y = q.data if q else 0
        if x < y:
            x += 10
            borrow = 1
        else:
            borrow = 0
        result.append(x - y)
        p = p.next
        if q: q = q.next
    
    # Remove leading zeros
    while result.head and result.head.data == 0:
        result.head = result.head.next
    
    if not result.head:
        result.append(0)
    
    # If result is negative and not zero, mark it as negative
    if negative and result.head.data != 0:
        result.head.data = -result.head.data
    
    return result

def multiply_linked_lists(l1, l2):
    num1 = int(''.join(map(str, l1.traverse())))
    num2 = int(''.join(map(str, l2.traverse())))
    product = str(num1 * num2)
    return create_linked_list_from_number(product)

def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    l1 = create_linked_list_from_number(num1[::-1])
    l2 = create_linked_list_from_number(num2[::-1])
    
    sum_result = add_linked_lists(l1, l2)
    print("Sum:", end=" ")
    sum_result.print_list()
    
    sub_result = subtract_linked_lists(l1, l2)
    print("Subtraction:", end=" ")
    sub_result.print_list()
    
    mul_result = multiply_linked_lists(l1, l2)
    print("Multiplication:", end=" ")
    mul_result.print_list()

if __name__ == "__main__":
    main()
