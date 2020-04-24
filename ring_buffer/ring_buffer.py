from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # self.current = 0
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            # self.current += 1
        elif len(self.storage) >= self.capacity:
            if self.current is None or self.current.next is None:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            elif self.current.next is not None:
                self.current.next.delete()
                self.current.insert_after(item)
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        current_node = self.storage.head
        list_buffer_contents.append(current_node.value)
        while current_node.next is not None:
            list_buffer_contents.append(current_node.next.value)
            current_node = current_node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
