class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
    def add_child(self, child_node):
        self.children.append(child_node)
    def display(self, level=0):
        print(" " * (level * 4) + f"- {self.name}")
        for child in self.children:
            child.display(level + 1)  
    def find(self, name):
        if self.name == name:
            return self
        for child in self.children:
            result = child.find(name)
            if result:
                return result
        return None
root = TreeNode("Maintenance Requests")
building_a = TreeNode("Building A")
building_b = TreeNode("Building B")
root.add_child(building_a)
root.add_child(building_b)
floor_1 = TreeNode("Floor 1")
floor_2 = TreeNode("Floor 2")
building_a.add_child(floor_1)
building_a.add_child(floor_2)

floor_3 = TreeNode("Floor 3")
floor_4 = TreeNode("Floor 4")
building_b.add_child(floor_3)
building_b.add_child(floor_4)
floor_1.add_child(TreeNode("Fix broken elevator"))
floor_1.add_child(TreeNode("Repair water leak in Apartment 101"))
floor_2.add_child(TreeNode("Replace hallway lights"))
floor_2.add_child(TreeNode("Service HVAC system"))
floor_3.add_child(TreeNode("Clean rooftop water tank"))
floor_3.add_child(TreeNode("Repair parking gate"))
floor_4.add_child(TreeNode("Fix broken windows in Apartment 405"))
print("Maintenance Request Hierarchy:")
root.display()
search_result = root.find("Replace hallway lights")
if search_result:
    print(f"\nFound: {search_result.name}")
else:
    print("\nRequest not found.")
