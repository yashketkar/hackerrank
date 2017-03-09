    #Complete this method
    def insert(self,head,data):
        mynode = Node(data)
        if head == None :
            head = mynode
            return head
        myhead = head
        prev = myhead
        while myhead:
            prev = myhead
            myhead = myhead.next
        prev.next = mynode
        return head
