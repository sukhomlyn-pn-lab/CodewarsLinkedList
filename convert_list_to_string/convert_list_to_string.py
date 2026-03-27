"""Convert list to string"""
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node:Node):
    if not isinstance(node, Node):
        return 'None'
    prev = node
    final_return = ''
    while True:
        final_return+=f'{prev.data} -> '
        if prev.next is None:
            final_return+='None'
            break
        prev = prev.next
    return final_return
print(stringify(Node(1, Node(2, Node(3)))))
