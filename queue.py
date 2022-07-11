class LinkedListItem:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item


class LinkedList:

    def __init__(self, first_item):
        self.first_item = first_item
        self.last_item = first_item
        self.current_item = first_item

    def __iter__(self):
        return self

    def __next__(self):

        if self.current_item is None:
            raise StopIteration()
        else:
            current_item_value = self.current_item.value
            self.next()
            return current_item_value

    def next(self):
        self.current_item = self.current_item.next

    def append(self, new_linked_list_item):
        new_linked_list_item.next = None
        self.last_item.next = new_linked_list_item
        self.last_item = new_linked_list_item

    def reset_cursor(self):
        self.current_item = self.first_item

    def remove(self, value: int):
        """
        Remove the first element found with the value given
        """
        local_cursor = self.first_item
        previous_element = None

        while local_cursor is not None:
            if local_cursor.value == value:
                if local_cursor == self.first_item:
                    self.first_item = local_cursor.next
                elif local_cursor == self.last_item:
                    previous_element.next = None
                else:
                    previous_element.next = local_cursor.next
                return

            previous_element = local_cursor
            local_cursor = local_cursor.next

    def __str__(self):
        string = ''
        cursor_position = self.current_item
        self.reset_cursor()
        while self.current_item is not None:
            string += f'{self.current_item.value} -> '
            self.next()
        self.current_item = cursor_position

        return string + 'None'


class Queue(LinkedList):
    def __init__(self, first_item):
        super().__init__(first_item)

    def enqueue(self, new_linked_list_item):
        new_linked_list_item.next = None
        self.last_item.next = new_linked_list_item
        self.last_item = new_linked_list_item

    def dequeue(self):
        # 2 <- 3 <-4
        local_cursor = self.first_item
        #if local_cursor == self.first_item:
        self.first_item = local_cursor.next
        return


if __name__ == '__main__':

    list1 = Queue((LinkedListItem(3)))
    print(list1)
    list1.enqueue(LinkedListItem(5))
    print(list1)
    list1.dequeue()
    print(list1)
