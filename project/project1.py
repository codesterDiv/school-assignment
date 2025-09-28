# write a program that displayes option for inserting or deleting elements in a list. if the user chooses a deletion option display a submenu and ask if the element is to be deleted with value or by using its position or a list slice is to be deleted.
def display_menu():
    print("Menu:")
    print()
    print("1. Insert an element")
    print()
    print("2. Delete an element")
    print()
    print("3. Exit")
    print()

def display_delete_menu():
    print("Delete Menu:")
    print()
    print("1. Delete by value")
    print()
    print("2. Delete by position")
    print()
    print("3. Delete a slice")
    print()

def main():
    lst = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            elem = input("Enter element to insert: ")
            lst.append(elem)
            print("List:", lst)
            print()
        elif choice == '2':
            display_delete_menu()
            del_choice = input("Enter your choice: ")
            if del_choice == '1':
                val = input("Enter value to delete: ")
                try:
                    lst.remove(val)
                    print("Deleted", val)
                    print()
                except ValueError:
                    print("Value not found.")
                    print()
            elif del_choice == '2':
                pos = input("Enter position to delete (0-based index): ")
                try:
                    pos = int(pos)
                    removed = lst.pop(pos)
                    print("Deleted", removed)
                    print()
                except (IndexError, ValueError):
                    print("Invalid position.")
                    print()
            elif del_choice == '3':
                start = input("Enter start index: ")
                end = input("Enter end index: ")
                try:
                    start = int(start)
                    end = int(end)
                    del lst[start:end]
                    print("Deleted slice from", start, "to", end)
                    print()
                except ValueError:
                    print("Invalid indices.")
                    print()
            else:
                print("Invalid delete option.")
                print()
            print("List:", lst)
            print()
        elif choice == '3':
            print("Exiting.")
            print()
            break
        else:
            print("Invalid option.")
            print()

if __name__ == "__main__":
    main()