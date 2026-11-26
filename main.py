def extract_unique_letters(name):

    letters = []
    for char in name.upper():
        if char.isalpha() and char not in letters:
            letters.append(char)
    return letters


def bubble_sort(arr):

    data = arr.copy()  # keep the unsorted array untouched
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:  # already sorted, stop early
            break
    return data


def main():
    full_name = "Alexa Auditor"

    unsorted_array = extract_unique_letters(full_name)
    sorted_array = bubble_sort(unsorted_array)

    print("Full Name:      ", full_name)
    print("Unsorted Array: ", unsorted_array)
    print("Sorted Array:   ", sorted_array)


if __name__ == "__main__":
    main()
