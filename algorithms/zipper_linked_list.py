# recursive solution

def zipper_list(head1, head2):
    tail = head1
    curr1 = head1.next
    curr2 = head2

    # recursive fx
    counter = 0
    recursive_zipper(curr1, curr2, tail, counter)

    if curr1 is not None: tail.next = curr1
    if curr2 is not None: tail.next = curr2

    return head1



def recursive_zipper(curr1, curr2, tail, counter):
    if curr1 is None or curr2 is None:
        return tail
    if counter % 2 == 0:
        tail.next = curr2
        curr2 = curr2.next
    else:
        tail.next = curr1
        curr1 = curr1.next
    tail = tail.next
    counter += 1
    recursive_zipper(curr1, curr2, tail, counter)
    