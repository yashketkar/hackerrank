    def removeDuplicates(self,head):
        mlist = []
        _prev = head
        mlist.append(_prev.data)
        _curr = _prev.next
        while _curr != None:
            if _curr.data in mlist:
                _prev.next = _curr.next
                _curr = _curr.next
            else:
                mlist.append(_curr.data)
                _prev = _curr
                _curr = _curr.next
        return head
