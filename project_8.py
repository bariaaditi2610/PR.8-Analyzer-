import numpy as np

current_array = None

def get_elements(count, prompt):
    while True:
        try:
            raw = input(prompt).strip().split()
            if len(raw) != count:
                print(f"Error: Expected {count} elements, but got {len(raw)}. Try again.")
                continue
            elements = [float(x) if '.' in x else int(x) for x in raw]
            return elements
        except ValueError:
            print("Invalid input. Please enter numbers separated by space.")

def create_array():
    global current_array
    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        n = int(input("Enter number of elements: "))
        elems = get_elements(n, f"Enter {n} elements separated by space: ")
        current_array = np.array(elems)
    elif choice == '2':
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        total = rows * cols
        elems = get_elements(total, f"Enter {total} elements for the array separated by space: ")
        current_array = np.array(elems).reshape((rows, cols))
    elif choice == '3':
        d1 = int(input("Enter dimension 1: "))
        d2 = int(input("Enter dimension 2 (rows): "))
        d3 = int(input("Enter dimension 3 (cols): "))
        total = d1 * d2 * d3
        elems = get_elements(total, f"Enter {total} elements for the array separated by space: ")
        current_array = np.array(elems).reshape((d1, d2, d3))
    else:
        print("Invalid choice.")
        return

    print("\nArray created successfully:")
    print(current_array)

    # Sub-menu for Indexing / Slicing if array is 2D/multi-dimensional
    if current_array.ndim >= 2:
        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        op_choice = input("Enter your choice: ").strip()

        if op_choice == '1':
            r = int(input("Enter row index: "))
            c = int(input("Enter column index: "))
            print(f"\nElement at [{r}, {c}]: {current_array[r, c]}")
        elif op_choice == '2':
            r_range = input("Enter the row range (start:end): ").strip().split(':')
            c_range = input("Enter the column range (start:end): ").strip().split(':')
            r_start, r_end = int(r_range[0]), int(r_range[1])
            c_start, c_end = int(c_range[0]), int(c_range[1])
            sliced = current_array[r_start:r_end, c_start:c_end]
            print("\nSliced Array:")
            print(sliced)

def mathematical_operations():
    global current_array
    if current_array is None:
        print("\nPlease create an array first (Option 1).")
        return

    print("\nChoose a mathematical operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice: ").strip()

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice.")
        return

    total = current_array.size
    prompt = f"Enter the same-size array elements ({total} elements separated by space): "
    elems = get_elements(total, prompt)
    second_array = np.array(elems).reshape(current_array.shape)

    print("\nOriginal Array:")
    print(current_array)
    print("\nSecond Array:")
    print(second_array)

    if choice == '1':
        res = current_array + second_array
        print("\nResult of Addition:")
    elif choice == '2':
        res = current_array - second_array
        print("\nResult of Subtraction:")
    elif choice == '3':
        res = current_array * second_array
        print("\nResult of Multiplication:")
    elif choice == '4':
        res = current_array / second_array
        print("\nResult of Division:")
    print(res)

def combine_or_split():
    global current_array
    if current_array is None:
        print("\nPlease create an array first (Option 1).")
        return

    print("\nChoose an option:")
    print("1. Combine Arrays")
    print("2. Split Array")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        total = current_array.size
        prompt = f"Enter the elements of another array to combine ({total} elements separated by space): "
        elems = get_elements(total, prompt)
        second_array = np.array(elems).reshape(current_array.shape)

        print("\nOriginal Array:")
        print(current_array)
        print("\nSecond Array:")
        print(second_array)

        # Stacking vertically (row-wise) matching assignment sample
        combined = np.vstack((current_array, second_array))
        print("\nCombined Array (Vertical Stack):")
        print(combined)

    elif choice == '2':
        sections = int(input("Enter number of splits: "))
        axis = int(input("Enter axis to split along (0 for rows, 1 for cols): "))
        try:
            splits = np.split(current_array, sections, axis=axis)
            print("\nSplit Arrays:")
            for idx, part in enumerate(splits, 1):
                print(f"Part {idx}:\n{part}")
        except ValueError as e:
            print("Split error:", e)

def search_sort_filter():
    global current_array
    if current_array is None:
        print("\nPlease create an array first (Option 1).")
        return

    print("\nChoose an option:")
    print("1. Search a value")
    print("2. Sort array")
    print("3. Filter array (condition: > value)")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        val = float(input("Enter value to search: "))
        indices = np.where(current_array == val)
        if len(indices[0]) > 0:
            print(f"Value found at index/indices: {list(zip(*indices))}")
        else:
            print("Value not found in array.")
    elif choice == '2':
        sorted_arr = np.sort(current_array, axis=None)
        print("\nSorted Array (flattened):")
        print(sorted_arr)
    elif choice == '3':
        threshold = float(input("Filter elements greater than: "))
        filtered = current_array[current_array > threshold]
        print("\nFiltered Elements:")
        print(filtered)

def compute_aggregates():
    global current_array
    if current_array is None:
        print("\nPlease create an array first (Option 1).")
        return

    print("\nChoose an aggregate/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")
    choice = input("Enter your choice: ").strip()

    print("\nOriginal Array:")
    print(current_array)

    if choice == '1':
        print(f"\nSum of Array: {np.sum(current_array)}")
    elif choice == '2':
        print(f"\nMean of Array: {np.mean(current_array)}")
    elif choice == '3':
        print(f"\nMedian of Array: {float(np.median(current_array))}")
    elif choice == '4':
        print(f"\nStandard Deviation of Array: {np.std(current_array)}")
    elif choice == '5':
        print(f"\nVariance of Array: {np.var(current_array)}")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("====================================")
        print("Choose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_array()
        elif choice == '2':
            mathematical_operations()
        elif choice == '3':
            combine_or_split()
        elif choice == '4':
            search_sort_filter()
        elif choice == '5':
            compute_aggregates()
        elif choice == '6':
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 6.")

if __name__ == "__main__":
    main()