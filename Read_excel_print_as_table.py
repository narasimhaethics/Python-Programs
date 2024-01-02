import pandas as pd

def read_and_print_excel(file_path):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Print the data in tabular format
    print(df)

if __name__ == "__main__":
    # Provide the path to your Excel file
    excel_file_path = "path/to/your/excel/file.xlsx"

    # Call the function to read and print the Excel file data
    read_and_print_excel(excel_file_path)
