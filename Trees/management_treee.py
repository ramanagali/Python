class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while(p):
            level += 1
            p = p.parent
        return level

    def print_tree(self, prop_name):
        if(prop_name == 'both'):
            value = self.name + '(' + self.designation + ')'
        elif(prop_name == 'name'):
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        # Ternary Operator in Python
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)

        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(prop_name)


def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels", "HR Head")

    peter = TreeNode("Peter", "Recruitment Manager")
    waqas = TreeNode("Waqas", "Policy Manager")

    hr_head.add_child(peter)
    hr_head.add_child(waqas)

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    print('CEO level', ceo.get_level())
    print('CTO level', cto.get_level())
    print('HR - Peter level', peter.get_level())
    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")
