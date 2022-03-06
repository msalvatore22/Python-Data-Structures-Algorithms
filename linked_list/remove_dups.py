
# Remove duplicates from and unsorted linked list

from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        visited = set([currNode.value])
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next = currNode.next.next
            else:
                visited.add(currNode.next.value)
                currNode = currNode.next
        return ll

custom_ll = LinkedList()
custom_ll.generate(10, 0, 99)
print(custom_ll)
print(removeDups(custom_ll))