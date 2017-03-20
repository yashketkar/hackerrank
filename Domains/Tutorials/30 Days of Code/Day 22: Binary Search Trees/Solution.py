    def getHeight(self,root):
        if root == None:
            return -1        
        lefth = self.getHeight(root.left)
        righth = self.getHeight(root.right)
        if lefth > righth:
            return lefth + 1
        else:
            return righth + 1