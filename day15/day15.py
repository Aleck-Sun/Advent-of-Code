class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class OrderedDict:
    def __init__(self):
        self.dict = {}
        self.left, self.right = Node('', 0), Node('', 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, key):
        if key in self.dict:
            node = self.dict[key]
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev
            del self.dict[key]

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def add(self, key, value):
        if key in self.dict:
            self.dict[key].val = value
        else:
            self.dict[key] = Node(key, value)
            self.insert(self.dict[key])

    def get_sum(self):
        sum = 0
        idx = 1
        curr = self.left.next
        while curr != self.right:
            sum += idx * curr.val
            curr = curr.next
            idx += 1
        return sum

    def get_contents(self):
        content = []
        curr = self.left.next
        while curr != self.right:
            content.append((curr.key, curr.val))
            curr = curr.next
        return content

def get_hash(string):
    hash = 0
    for c in string:
        hash += ord(c)
        hash *= 17
        hash = hash % 256
    return hash

def day15_part_one():
    with open('input.txt', 'r') as f:
        strings = f.read().split(',')
        return sum(get_hash(string) for string in strings)

def day15_part_two():
    with open('input.txt', 'r') as f:
        boxes = [OrderedDict() for _ in range(256)]
        strings = f.read().split(',')
        for string in strings:
            if '-' in string:
                label = string[:-1]
                boxes[get_hash(label)].remove(label)
            else:
                label, value = string.split('=')
                boxes[get_hash(label)].add(label, int(value))

        return sum(boxes[box].get_sum() * (box+1) for box in range(len(boxes)))

if __name__ == '__main__':
    print(day15_part_one())
    print(day15_part_two())