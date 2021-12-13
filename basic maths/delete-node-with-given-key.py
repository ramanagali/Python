import random


def delete_node(head, key):
    prev = None
    current = head

    while (current != None):
        if current.data == key:
            if current == head:
                head = head.next
                current = head
            else:
                prev.next = current.next
                current = current.next

        else:
            prev = current
            current = current.next

    # key not found in list
    if current == None:
        return head

    return head


def create_random_list(n):
    random_list = []
    for i in range(n):
        random_list.append(random.randint(0, n))
    return random_list


def display_list(list_head):
    for i in range(len(list_head)):
        print(i, end=' ')


list_head = create_random_list(10)
print("Original:")
