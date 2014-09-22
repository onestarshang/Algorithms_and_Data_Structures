#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
有头节点的链表
"""

class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def __repr__(self):
        ptr = self.head
        if ptr is None:
            return '<%s>'%('None')
        else:
            _res = '( HEAD'
            while ptr:
                _res += ' --> [ %s ]'%ptr.data
                ptr = ptr.next

            return _res + ' )'

    def insert(self, data):
        self.head = Node(data, self.head)

    def get_size(self):
        cnt = 0
        ptr = self.head
        if ptr is None:
            return cnt
        else:
            while ptr:
                cnt += 1
                ptr = ptr.next
        return cnt

    def get_index(self, data):
        ptr = self.head
        cnt = 0
        if ptr is None:
            return None
        else:
            while ptr:
                if ptr.data == data:
                    return cnt
                cnt += 1
                ptr = ptr.next
                

    def find_by_index(self, idx):


        pass

    def delete_by_index(self, idx):

        pass

    def delete_linkedlist(self):
        self.head = None



if __name__ == '__main__':
    ll = LinkedList()
    print ll
    for i in [3,2,54,6]:
        ll.insert(i)
    print ll
    print ll.get_size()