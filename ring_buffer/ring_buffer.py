from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length >= self.capacity:
            # If the storage is at capacity, replace the
            # `current` item with the new one
            self.current.value = item
            # Increment `current` to the next node,
            # looping from the end to the head
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head
        else:
            # Add to tail until it's full
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_index = 0
        self.storage = [None] * capacity

    def append(self, item):
        # Update the current item
        self.storage[self.current_index] = item
        # Increment the current item index,
        # looping from end to head
        self.current_index += 1
        if self.current_index >= self.capacity:
            self.current_index = 0

    def get(self):
        return [x for x in self.storage if x is not None]
