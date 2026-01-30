def get_marks():
    marks = []
    n = int(input("Enter number of students: "))

    for i in range(n):
        while True:
            try:
                mark = float(input(f"Enter marks for student {i + 1}: "))
                if mark < 0:
                    print("Marks cannot be negative. Try again.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return marks


def calculate_average(marks):
    return sum(marks) / len(marks)


def find_highest(marks):
    return max(marks)


def find_lowest(marks):
    return min(marks)


def main():
    print("=== Student Marks Analyzer ===")

    marks = get_marks()

    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)

    print("\nResults:")
    print(f"Average Marks : {average:.2f}")
    print(f"Highest Marks : {highest}")
    print(f"Lowest Marks  : {lowest}")


if __name__ == "__main__":
    main()