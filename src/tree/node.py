class node(object):    
    def __init__(self, name = None, own_directory = None):
        self.own_directory = own_directory
        self.name = name
        self.child_directory = []
        self.level = 0
       
    def print_all_node(self):
        if self.child_directory:
            print("In {name} - {level}".format(name=self.name, level=self.level))
            for item in self.child_directory:                
                item.print_all_node()
                print('{level} - {name}'.format(name=item.name, level = item.level))    
        
    
            