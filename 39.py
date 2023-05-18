class LinkedList:

    def __init__(self, a:list):

        self.store = []
        next = None
        for i in range(len(a) - 1, -1, -1):
            node = self.ListNode(a[i], next)
            self.store.append(node)
            next = node

        self.enter = self.store[len(self.store) - 1]

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

        def __str__(self):
            next = "None" if self.next is None else self.next.val
            return f"({self.val}, next={next})"

        __repr__ = __str__

    def __str__(self):
        return str(self.store)

    __repr__ = __str__


a = [2, 4, 3]
linked_list = LinkedList(a)
l1 = LinkedList([9,9,9,9,9,9,9])
l2 = LinkedList([9,9,9,9])
# l1 = LinkedList([9,9,9])
# l2 = LinkedList([9,9,9])
l1 = l1.enter
l2 = l2.enter

extra = 0
store = []

while not (l1 is None or l2 is None) :

    div1 = (l1.val + l2.val) // 10
    res1 = (l1.val + l2.val) % 10

    div2 = (extra + res1) // 10
    res2 = (extra + res1) % 10

    extra = 0 if div1 + div2 == 0 else div1 + div2
    store.append(LinkedList.ListNode(val=res2))

    l1 = l1.next
    l2 = l2.next


if not (l1 is None):
    while not (l1 is None):
        div = (extra + l1.val) // 10
        res = (extra + l1.val) % 10

        extra = 0 if div == 0 else div
        store.append(LinkedList.ListNode(val=res))
        l1 = l1.next

if not (l2 is None):
    while not (l2 is None):
        div = (extra + l2.val) // 10
        res = (extra + l2.val) % 10

        extra = 0 if div == 0 else div
        store.append(LinkedList.ListNode(val=res))
        l2 = l2.next

if extra != 0:
    store.append(LinkedList.ListNode(val=extra))

for i in range(len(store) - 1):
    store[i].next = store[i + 1]

print(store)
# print(linked_list)
# print(linked_list.enter)
