class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



def generateListNode(list):
    head=ListNode(list[0])
    ptr=head
    for i in range(1,len(list)):
        ptr.next=ListNode(list[i])
        ptr=ptr.next
    return head