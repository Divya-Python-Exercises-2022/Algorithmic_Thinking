class LinkedListItem:

    def __init__(self, value, next_item=None, previous_item=None):
        self.value = value
        self.next = next_item
        self.previous = previous_item

    def __iter__(self):
        return self

class DoubleLinkedList:

    def __init__(self, first_item):
        self.first_item = first_item
        self.last_item = first_item
        self.current_item = first_item
        self.previous_item = first_item


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
# 4 5
    def append(self, new_linked_list_item):
        new_linked_list_item.next = None
        self.last_item.next = new_linked_list_item
        self.previous_item = self.last_item
        self.last_item = new_linked_list_item
        self.last_item.previous = self.previous_item
        self.previous_item.next = self.last_item

        print(f'Previous{self.previous_item.value}')
        print(f'last{self.last_item.value}')


    def reset_cursor(self):
        self.current_item = self.first_item

    def remove(self, value: int):
        """
        Remove the first element found with the value given
        """
        local_cursor = self.first_item
        previous_element = None


        # 1 = 2 = 3 = 4

        while local_cursor is not None:
            if local_cursor.value == value:
                if local_cursor == self.first_item:
                    self.first_item = local_cursor.next
                    self.first_item.previous = None
                elif local_cursor == self.last_item:
                    previous_element.next = None
                    self.last_item.previous = None
                else:
                    previous_element.next = local_cursor.next
                    local_cursor.next.previous = local_cursor.previous
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

if __name__ == '__main__':
    print("---------- Adding Items")
    list1 = DoubleLinkedList(LinkedListItem(4, None, None))
    print(list1)
    list1.append(LinkedListItem(5, None, None))
    print(list1)
    list1.append(LinkedListItem(10, None, None))
    print(list1)
    list1.append(LinkedListItem(7, None, None))
    print(list1)

    print(type(list1))

    for item in list1:
        print('**** printing list in for loop ****')
        print(item)

    # list1.remove(4)
    # print(f'The list after removing first item{list1}')
    # list1.remove(7)
    # print(f'The list after removing last item{list1}')
    list1.remove(10)
    print(f'The list after removing middle item{list1}')