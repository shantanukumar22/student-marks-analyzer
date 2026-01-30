def get_marks():
    marks = []

    while True:
        try:
            n = int(input("Enter number of students: "))
            if n < 0:
                print("Number of students cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(n):
        while True:
            try:
                mark = float(input(f"Enter marks for student {i + 1}: "))
                if mark < 0:
                    print("Marks cannot be negative.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return marks


def calculate_average(marks):
    return sum(marks) / len(marks)


def main():
    print("=== Student Marks Analyzer ===")

    marks = get_marks()

    # ✅ EDGE CASE HANDLED
    if len(marks) == 0:
        print("No marks entered. Cannot calculate results.")
        return

    average = calculate_average(marks)
    highest = max(marks)
    lowest = min(marks)

    print("\nResults:")
    print(f"Average Marks : {average:.2f}")
    print(f"Highest Marks : {highest}")
    print(f"Lowest Marks  : {lowest}")


if __name__ == "__main__":
    main()