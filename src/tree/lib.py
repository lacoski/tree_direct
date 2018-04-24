from .node import (
    node
)

class manager_node(object):
    myTree = None
    def __init__(self):
        self.myTree = node(name= 'root', own_directory= None)        
    
    def add_node(self, new_node):
        self.myTree.child_directory.append(new_node)
        new_node.own_directory = self.myTree
        new_node.level = self.myTree.level + 1
                
    def cd_child_node(self,name):          
        for item in self.myTree.child_directory:            
            if item.name == name:
                self.myTree = item
    
    def cd_parent_node(self):
        if self.myTree.own_directory == None:
            print('still in root')
        else:
            self.myTree = self.myTree.own_directory

    def cd_path_to_node(self, path_to_node):
        path_array = str(path_to_node).split('/')
        for item in path_array:
            print(item)
    
    def ls_current_node(self):
        print('ls dir:')
        for item in self.myTree.child_directory:            
            print("\t {name} - {level}".format(name=item.name, level=item.level))    

    def rm_node(self, name):
        for item in self.myTree.child_directory:            
            if item.name == name:
                self.myTree.child_directory.remove(item)

    def print_all_node(self):
        print("Print all node:")
        self.myTree.print_all_node()            

    def print_node(self):
        print('print tree:')
        print("{name} - {level}".format(name=self.myTree.name, level=self.myTree.level))       