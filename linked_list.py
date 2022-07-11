class LinkedListItem:

    def __init__(self, value, next_item):
        self.value = value
        self.next = next_item

class LinkedList:

    def __init__(self, first_item):
        self.first_item = first_item
        self.last_item = first_item
        self.current_item = first_item

    def next(self):
        self.current_item = self.current_item.next

    def append(self, new_linked_list_item):
        new_linked_list_item.next = None
        self.last_item.next = new_linked_list_item
        self.last_item = new_linked_list_item

    def reset_cursor(self):
        self.current_item = self.first_item

    def remove(self, value):

        # self.first_item = self.first_item.next
        # print('*****  First Item is *****')
        # print(self.first_item.value)

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



if __name__ == '__main__':

    list1 = LinkedList(LinkedListItem(4, None))
    list1.append(LinkedListItem(5, None))
    list1.append(LinkedListItem(6, None))

    print(list1.first_item.value)
    print(list1.current_item.value)
    list1.next()
    print(list1.current_item.value)
    list1.next()
    print(list1.current_item.value)

    list1.next()
    print(list1.current_item)

    list1.reset_cursor()
    print(list1.current_item.value)

    if list1.first_item.value is None:
        print('No items in the list')
    else:
        list1.remove(5)

    print(list1)


