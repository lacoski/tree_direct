class Directory_Tree(object):    
    def __init__(self, name = None, own_directory = None):
        self.own_directory = own_directory
        self.name = name
        self.child_directory = []
        self.level = 0

    def add_subtree(self, sub_tree):
        self.child_directory.append(sub_tree)
        sub_tree.own_directory = self
        sub_tree.level = self.level + 1
    def delete_subtree(self):
        if self.child_directory:
            for item in self.child_directory:
                item.delete_subtree()
        else:
            del self
    def print_all_tree(self):
        if self.child_directory:
            print("In {name} - {level}".format(name=self.name, level=self.level))
            for item in self.child_directory:                
                item.print_all_tree()
                print('{level} - {name}'.format(name=item.name, level = item.level))
            


class manager_tree(object):
    myTree = None
    def __init__(self):
        self.myTree = Directory_Tree(name= 'root', own_directory= None)        
    
    def add_child_directory(self, subtree):
        self.myTree.add_subtree(subtree)
        
    def cd_sub_directory(self,name):
        #print(name)        
        for item in self.myTree.child_directory:
            #print(item.name)
            if item.name == name:
                self.myTree = item
    
    def cd_home_directory(self):
        if self.myTree.own_directory == None:
            print('still in root')
        else:
            self.myTree = self.myTree.own_directory
    
    def ls_directory(self):
        print('ls dir:')
        for item in self.myTree.child_directory:            
            print("\t {name} - {level}".format(name=item.name, level=item.level))    

    def rm_directory(self):
        self.myTree.delete_subtree()

    def print_all_tree(self):
        self.myTree.print_all_tree()

    def print_tree(self):
        print('print tree:')
        print("{name} - {level}".format(name=self.myTree.name, level=self.myTree.level))        

def main():       
    new_tree = manager_tree()
    new_tree.print_tree()
    d_home = Directory_Tree(name='home')    
    d_download = Directory_Tree(name='download')
    new_tree.add_child_directory(d_home)
    new_tree.add_child_directory(d_download)
    new_tree.ls_directory()

    new_tree.cd_sub_directory('home')
    new_tree.print_tree()
    d_thanh = Directory_Tree(name='thanh')
    d_pic = Directory_Tree(name='pic')
    new_tree.add_child_directory(d_thanh)
    new_tree.add_child_directory(d_pic)

    new_tree.cd_home_directory()
    new_tree.print_tree()

    new_tree.print_all_tree()
if __name__ == '__main__':
    main() 