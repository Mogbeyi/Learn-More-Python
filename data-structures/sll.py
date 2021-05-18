class SingleLinkedListNode(object):
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

        def __repr__(self):
            nval = self.next and self.next.value or None
            return f"[{self.value}:{repr(nval))}]"

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
