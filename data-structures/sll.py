class SingleLinkedListNode(object):
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

        def __repr__(self):
            nval = self.next and self.next.value or None
            return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        node = SingleLinkedListNode(obj, None)

        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node
            assert self.begin != self.end

        assert self.end.next == None

    def pop(self):
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            assert self.end != node
            self.end = node
            return node.next.value

    def count(self):
        node = self.begin
        count = 0

        while node:
            count += 1
            node = node.next
        return count
