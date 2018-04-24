from tree.lib import manager_node
from tree.node import node

def main():       
    new_tree = manager_node()
    new_tree.print_node()
    d_home = node(name='home')    
    d_download = node(name='download')
    new_tree.add_node(d_home)
    new_tree.add_node(d_download)
    new_tree.ls_current_node()
    
    new_tree.cd_child_node('home')
    new_tree.print_node()
    new_tree.add_node(node('Pictures'))
    new_tree.add_node(node('Download'))
    new_tree.ls_current_node()
    new_tree.cd_parent_node()
    new_tree.print_all_node()
    new_tree.rm_node('home')
    new_tree.print_all_node()
if __name__ == '__main__':
    main() 