"""A binary-tree company directory with a simple command-line menu."""


class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        """Insert a direct report under the named manager, using recursion."""
        if self.root is None:
            print("Tree is empty. Add a team lead first.")
            return False

        side = side.strip().lower()
        if side not in ("left", "right"):
            print("Invalid side. Please enter left or right.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if getattr(current_node, side) is not None:
                print(f"{manager_name} already has a {side} direct report.")
                return False
            setattr(current_node, side, EmployeeNode(employee_name))
            print(f"{employee_name} added to the {side.upper()} of {manager_name}.")
            return True

        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True
        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        if current_node is self.root:
            print(f"Manager '{manager_name}' was not found in the team.")
        return False

    def print_tree(self, node=None, level=0):
        """Display each employee, indenting reports beneath managers."""
        if node is None:
            if level == 0:
                node = self.root
            else:
                return
        if node is None:
            print("The team directory is empty.")
            return

        print("    " * level + "- " + node.name)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if tree.root is not None:
                print("⚠️ Team lead already exists.")
                continue
            name = input("Enter team lead's name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            tree.root = EmployeeNode(name)
            print(f"✅ {name} added as the team lead.")
        elif choice == "2":
            if tree.root is None:
                print("Add a team lead first.")
                continue
            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ").strip()
            if not manager or not employee:
                print("Manager and employee names cannot be empty.")
                continue
            tree.insert(manager, employee, side)
        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()
        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    company_directory()
