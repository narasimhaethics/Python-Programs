import csv

def calculate_average(csv_file, column_name):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            
            # Check if the specified column exists in the CSV file
            if column_name not in reader.fieldnames:
                print(f"Column '{column_name}' not found in the CSV file.")
                return None

            # Initialize variables for calculating the average
            total = 0
            count = 0

            # Iterate through rows and calculate the sum
            for row in reader:
                try:
                    value = float(row[column_name])
                    total += value
                    count += 1
                except ValueError:
                    print(f"Skipping row {reader.line_num}: Invalid value in column '{column_name}'.")
            
            # Check if there are valid values in the column
            if count == 0:
                print(f"No valid values found in column '{column_name}'.")
                return None

            # Calculate the average
            average = total / count
            return average

    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
        return None

# Example usage:
csv_file_path = 'your_file.csv'  # Replace with the path to your CSV file
column_to_calculate = 'column_name'  # Replace with the column name you want to calculate the average for

result = calculate_average(csv_file_path, column_to_calculate)

if result is not None:
    print(f"The average value in column '{column_to_calculate}' is: {result}")
