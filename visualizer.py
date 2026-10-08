import pandas as pd
import matplotlib.pyplot as plt


# Global variables
data = None
current_plot = None


# ============================================================
#                  MAIN MENU
# ============================================================

def display_menu():
    print("\n")
    print("=" * 60)
    print("        DATA ANALYSIS & VISUALIZATION PROGRAM")
    print("=" * 60)

    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")

    print("=" * 60)


# ============================================================
#                  1. LOAD DATASET
# ============================================================

def load_dataset():

    global data

    print("\n========== Load Dataset ==========")

    file_path = input(
        "Enter the path of the dataset (CSV file): "
    )

    try:
        data = pd.read_csv(file_path)

        print("\nDataset loaded successfully!")

    except FileNotFoundError:
        print("\nError: File not found.")

    except Exception as error:
        print("\nError while loading dataset:", error)


# ============================================================
#                  2. EXPLORE DATA
# ============================================================

def explore_data():

    if data is None:
        print("\nPlease load the dataset first!")
        return

    print("\n========== Explore Data ==========")

    print("1. Display the first 5 rows")
    print("2. Display the last 5 rows")
    print("3. Display column names")
    print("4. Display data types")
    print("5. Display basic info")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\nFirst 5 rows:")
        print(data.head())

    elif choice == "2":

        print("\nLast 5 rows:")
        print(data.tail())

    elif choice == "3":

        print("\nColumn names:")
        print(list(data.columns))

    elif choice == "4":

        print("\nData types:")
        print(data.dtypes)

    elif choice == "5":

        print("\nBasic information:")
        data.info()

    else:

        print("\nInvalid choice!")


# ============================================================
#             3. DATAFRAME OPERATIONS
# ============================================================

def dataframe_operations():

    global data

    if data is None:
        print("\nPlease load the dataset first!")
        return

    print("\n========== DataFrame Operations ==========")

    print("1. Display shape")
    print("2. Display a column")
    print("3. Add a new column")
    print("4. Delete a column")
    print("5. Sort data")

    choice = input("\nEnter your choice: ")

    # Display shape
    if choice == "1":

        print("\nShape of dataset:")
        print(data.shape)

    # Display column
    elif choice == "2":

        column = input("Enter column name: ")

        if column in data.columns:
            print("\nColumn data:")
            print(data[column])
        else:
            print("\nColumn not found!")

    # Add column
    elif choice == "3":

        column = input("Enter new column name: ")
        value = input("Enter value: ")

        data[column] = value

        print("\nNew column added successfully!")
        print(data)

    # Delete column
    elif choice == "4":

        column = input("Enter column name to delete: ")

        if column in data.columns:

            data.drop(column, axis=1, inplace=True)

            print("\nColumn deleted successfully!")

        else:

            print("\nColumn not found!")

    # Sort data
    elif choice == "5":

        column = input("Enter column name to sort: ")

        if column in data.columns:

            data = data.sort_values(by=column)

            print("\nData sorted successfully!")
            print(data)

        else:

            print("\nColumn not found!")

    else:

        print("\nInvalid choice!")


# ============================================================
#                  4. HANDLE MISSING DATA
# ============================================================

def handle_missing_data():

    global data

    if data is None:
        print("\nPlease load the dataset first!")
        return

    print("\n========== Handle Missing Data ==========")

    print("1. Display rows with missing values")
    print("2. Fill missing values with mean")
    print("3. Drop rows with missing values")
    print("4. Replace missing values with a specific value")

    choice = input("\nEnter your choice: ")

    # Display missing values
    if choice == "1":

        missing_rows = data[data.isnull().any(axis=1)]

        if missing_rows.empty:

            print("\nNo missing values found in the dataset!")

        else:

            print("\nRows containing missing values:")
            print(missing_rows)

    # Fill with mean
    elif choice == "2":

        numeric_columns = data.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            data[column] = data[column].fillna(
                data[column].mean()
            )

        print("\nMissing values filled with mean successfully!")

    # Drop rows
    elif choice == "3":

        data.dropna(inplace=True)

        print("\nRows with missing values removed successfully!")

    # Replace with specific value
    elif choice == "4":

        value = input(
            "Enter the value to replace missing values: "
        )

        data.fillna(value, inplace=True)

        print("\nMissing values replaced successfully!")

    else:

        print("\nInvalid choice!")


# ============================================================
#             5. DESCRIPTIVE STATISTICS
# ============================================================

def descriptive_statistics():

    if data is None:
        print("\nPlease load the dataset first!")
        return

    print("\n========== Descriptive Statistics ==========")

    print(data.describe())


# ============================================================
#                  6. DATA VISUALIZATION
# ============================================================

def data_visualization():

    global current_plot

    if data is None:
        print("\nPlease load the dataset first!")
        return

    print("\n========== Data Visualization ==========")

    print("1. Bar Plot")
    print("2. Line Plot")
    print("3. Scatter Plot")
    print("4. Pie Chart")
    print("5. Histogram")
    print("6. Stack Plot")

    choice = input("\nEnter your choice: ")

    # --------------------------------------------------------
    # BAR PLOT
    # --------------------------------------------------------

    if choice == "1":

        print("\n========== Bar Plot ==========")

        x_column = input(
            "Enter x-axis column name: "
        )

        y_column = input(
            "Enter y-axis column name: "
        )

        if x_column not in data.columns or \
           y_column not in data.columns:

            print("\nInvalid column name!")
            return

        plt.figure()

        plt.bar(
            data[x_column].astype(str),
            data[y_column]
        )

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Bar Plot")

        plt.xticks(rotation=45)
        plt.tight_layout()

        current_plot = plt.gcf()

        print("\nGenerating bar plot...")
        plt.show()

        print("Bar plot displayed successfully!")

    # --------------------------------------------------------
    # LINE PLOT
    # --------------------------------------------------------

    elif choice == "2":

        print("\n========== Line Plot ==========")

        x_column = input(
            "Enter x-axis column name: "
        )

        y_column = input(
            "Enter y-axis column name: "
        )

        if x_column not in data.columns or \
           y_column not in data.columns:

            print("\nInvalid column name!")
            return

        plt.figure()

        plt.plot(
            data[x_column],
            data[y_column],
            marker="o"
        )

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Line Plot")

        plt.tight_layout()

        current_plot = plt.gcf()

        print("\nGenerating line plot...")
        plt.show()

        print("Line plot displayed successfully!")

    # --------------------------------------------------------
    # SCATTER PLOT
    # --------------------------------------------------------

    elif choice == "3":

        print("\n========== Scatter Plot ==========")

        x_column = input(
            "Enter x-axis column name: "
        )

        y_column = input(
            "Enter y-axis column name: "
        )

        if x_column not in data.columns or \
           y_column not in data.columns:

            print("\nInvalid column name!")
            return

        plt.figure()

        plt.scatter(
            data[x_column],
            data[y_column]
        )

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Scatter Plot")

        plt.tight_layout()

        current_plot = plt.gcf()

        print("\nGenerating scatter plot...")
        plt.show()

        print("Scatter plot displayed successfully!")

    # --------------------------------------------------------
    # PIE CHART
    # --------------------------------------------------------

    elif choice == "4":

        print("\n========== Pie Chart ==========")

        label_column = input(
            "Enter category column name: "
        )

        value_column = input(
            "Enter values column name: "
        )

        if label_column not in data.columns or \
           value_column not in data.columns:

            print("\nInvalid column name!")
            return

        plt.figure()

        plt.pie(
            data[value_column],
            labels=data[label_column],
            autopct="%1.1f%%"
        )

        plt.title("Pie Chart")

        current_plot = plt.gcf()

        print("\nGenerating pie chart...")
        plt.show()

        print("Pie chart displayed successfully!")

    # --------------------------------------------------------
    # HISTOGRAM
    # --------------------------------------------------------

    elif choice == "5":

        print("\n========== Histogram ==========")

        column = input(
            "Enter column name: "
        )

        if column not in data.columns:

            print("\nInvalid column name!")
            return

        plt.figure()

        plt.hist(
            data[column].dropna(),
            bins=10
        )

        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title("Histogram")

        plt.tight_layout()

        current_plot = plt.gcf()

        print("\nGenerating histogram...")
        plt.show()

        print("Histogram displayed successfully!")

    # --------------------------------------------------------
    # STACK PLOT
    # --------------------------------------------------------

    elif choice == "6":

        print("\n========== Stack Plot ==========")

        x_column = input(
            "Enter x-axis column name: "
        )

        y1_column = input(
            "Enter first y-axis column name: "
        )

        y2_column = input(
            "Enter second y-axis column name: "
        )

        if (
            x_column not in data.columns
            or y1_column not in data.columns
            or y2_column not in data.columns
        ):

            print("\nInvalid column name!")
            return

        plt.figure()

        plt.stackplot(
            data[x_column],
            data[y1_column],
            data[y2_column],
            labels=[
                y1_column,
                y2_column
            ]
        )

        plt.xlabel(x_column)
        plt.ylabel("Values")

        plt.title("Stack Plot")

        plt.legend()

        plt.tight_layout()

        current_plot = plt.gcf()

        print("\nGenerating stack plot...")
        plt.show()

        print("Stack plot displayed successfully!")

    else:

        print("\nInvalid choice!")


# ============================================================
#                7. SAVE VISUALIZATION
# ============================================================

def save_visualization():

    if current_plot is None:

        print("\nPlease create a visualization first!")
        return

    print("\n========== Save Visualization ==========")

    filename = input(
        "Enter file name to save the plot "
        "(e.g., scatter_plot.png): "
    )

    if filename == "":

        print("\nFile name cannot be empty!")
        return

    if not filename.lower().endswith(
        (".png", ".jpg", ".jpeg", ".pdf")
    ):

        filename = filename + ".png"

    current_plot.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    print(
        "\nVisualization saved as "
        + filename
        + " successfully!"
    )


# ============================================================
#                  MAIN PROGRAM
# ============================================================

def main():

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            load_dataset()

        elif choice == "2":

            explore_data()

        elif choice == "3":

            dataframe_operations()

        elif choice == "4":

            handle_missing_data()

        elif choice == "5":

            descriptive_statistics()

        elif choice == "6":

            data_visualization()

        elif choice == "7":

            save_visualization()

        elif choice == "8":

            print("\nThank you for using the program!")
            print("Program exited successfully.")

            break

        else:

            print(
                "\nInvalid choice! "
                "Please enter a number from 1 to 8."
            )


# ============================================================
#                  PROGRAM START
# ============================================================

if _name_ == "_main_":
    main()