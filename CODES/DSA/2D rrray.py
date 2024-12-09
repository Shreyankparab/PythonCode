def display(matrix):
    if len(matrix) == 0:
        print("Matrix is empty.")
    else:
        for row in matrix:
            for elem in row:
                print(elem, end=" ")
            print()

def insert_element(matrix, row, col, element):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        matrix[row][col] = element
    else:
        print("Invalid position!")

def delete_row(matrix, row):
    if 0 <= row < len(matrix):
        # Create a new matrix with the row deleted
        new_matrix = [matrix[i] for i in range(len(matrix)) if i != row]
        return new_matrix
    else:
        print("Invalid row index.")
        return matrix

def delete_column(matrix, col):
    if 0 <= col < len(matrix[0]):
        # Create a new matrix with the column deleted
        new_matrix = []
        for row in matrix:
            new_row = [row[i] for i in range(len(row)) if i != col]
            new_matrix.append(new_row)
        return new_matrix
    else:
        print("Invalid column index.")
        return matrix

def search_element(matrix, element):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return i, j
    return -1, -1

def update_element(matrix, row, col, element):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        matrix[row][col] = element
    else:
        print("Invalid position!")

def menu():
    matrix = []
    
    while True:
        print("\nMenu:")
        print("1. Input Matrix")
        print("2. Display Matrix")
        print("3. Insert Element")
        print("4. Delete Row")
        print("5. Delete Column")
        print("6. Search Element")
        print("7. Update Element")
        print("8. Exit")
        
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            matrix = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    element = int(input(f"Enter element at position ({i},{j}): "))
                    row.append(element)
                matrix.append(row)
        
        elif choice == 2:
            print("Matrix:")
            display(matrix)
        
        elif choice == 3:
            row = int(input("Enter row to insert element (0-indexed): "))
            col = int(input("Enter column to insert element (0-indexed): "))
            element = int(input("Enter the element: "))
            insert_element(matrix, row, col, element)
        
        elif choice == 4:
            row = int(input("Enter the row to delete (0-indexed): "))
            matrix = delete_row(matrix, row)
            print("Row deleted successfully.")
        
        elif choice == 5:
            col = int(input("Enter the column to delete (0-indexed): "))
            matrix = delete_column(matrix, col)
            print("Column deleted successfully.")
        
        elif choice == 6:
            element = int(input("Enter element to search: "))
            row, col = search_element(matrix, element)
            if row != -1:
                print(f"Element found at position ({row},{col}).")
            else:
                print("Element not found.")
        
        elif choice == 7:
            row = int(input("Enter row to update (0-indexed): "))
            col = int(input("Enter column to update (0-indexed): "))
            element = int(input("Enter the new element: "))
            update_element(matrix, row, col, element)
            print("Element updated successfully.")
        
        elif choice == 8:
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
