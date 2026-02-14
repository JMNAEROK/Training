class TreeNode :
    def __init__ (self, value, left=None, right=None) :
        self.value = value
        self.left_child = left
        self.right_child = right

node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)

def search (search_value, node) :
    if not node or node.value == search_value :
        return node
    
    elif search_value < node.value :
        return search(search_value, node.left_child)
    
    else :
        return search(search_value, node.right_child)
    
def insert (value, node) :
    if value < node.value :

        if not node.left_child :
            node.left_child = TreeNode(value)
        else :
            insert (value, node.left_child)
        
    elif value > node.value :
        if not node.right_child :
            node.right_child = TreeNode(value)
        else :
            insert(value, node.right_child)


def replace_with_successor_node (node) :
    successor_node = node.right_child

    if not successor_node.left_child :
        node.value = successor_node.value
        node.right_child = successor_node.right_child
        return
    
    while successor_node.left_child :
        parent_of_successor_node = successor_node
        successor_node = successor_node.left_child
    
    if successor_node.right_child :
        parent_of_successor_node.left_child = successor_node.right_child
    else :
        parent_of_successor_node.left_child = None

    node.value = successor_node.value
    return successor_node

def delete (value_to_delete, node) :
    current_node = node
    parent_of_current_node = None
    node_to_delete = None

    while current_node :
        if current_node.value == value_to_delete :
            node_to_delete = current_node
            break
        
        parent_of_current_node = current_node
        if value_to_delete < current_node.value :
            current_node = current_node.left_child
        elif value_to_delete > current_node.value :
            current_node = current_node.right_child

    if not node_to_delete :
        return None
    
    if node_to_delete.left_child and node_to_delete.right_child :
        replace_with_successor_node (node_to_delete)
    else : #삭제된 노드에 자식이 0 또는 1개 있는 경우

        child_of_deleted_node = (node_to_delete.left_child or node_to_delete.right_child)

        if not parent_of_current_node :
            node_to_delete.value = child_of_deleted_node.value
            node_to_delete.left_child = child_of_deleted_node.left_child
            node_to_delete.right_child = child_of_deleted_node.right_child
        elif node_to_delete == parent_of_current_node.left_child :
            parent_of_current_node.left_child = child_of_deleted_node
        elif node_to_delete == parent_of_current_node.right_child :
            parent_of_current_node.right_child = child_of_deleted_node

    return node_to_delete

def traverse_and_print (node) :
    if not node :
        return
    traverse_and_print(node.left_child)
    print(node.value)
    traverse_and_print(node.right_child)