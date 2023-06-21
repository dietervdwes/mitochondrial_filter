"""
Written by Dieter van der Westhuizen
2023
"""
import pandas as pd
import os


    
# Get the .txt file to filter from
# Get the list of files in the current working directory
file_list2 = [file for file in os.listdir() if file.lower().endswith('.txt')]

# Print the available CSV files for selection
print("Available TXT files:")
for i, file_name in enumerate(file_list2):
    print(f"{i+1}. {file_name}")

# Prompt the user for input
selection = input("Select a TXT file by entering the corresponding number: ")

# Check if the user input is valid
if selection.isdigit() and 1 <= int(selection) <= len(file_list2):
    # Get the selected CSV file based on the user's input
    selected_file2 = file_list2[int(selection) - 1]
    print(f"You selected: {selected_file2}")
else:
    print("Invalid selection. Please try again.")
    

# Get the list of files in the current working directory
file_list = [file for file in os.listdir() if file.lower().endswith('.tsv')]

# Print the available CSV files for selection
print("Available TSV files:")
for i, file_name in enumerate(file_list):
    print(f"{i+1}. {file_name}")

# Prompt the user for input
selection = input("Select a CSV file by entering the corresponding number: ")

# Check if the user input is valid
if selection.isdigit() and 1 <= int(selection) <= len(file_list):
    # Get the selected CSV file based on the user's input
    selected_file = file_list[int(selection) - 1]
    print(f"You selected: {selected_file}")
else:
    print("Invalid selection. Please try again.")


# Read the episode number file into a pandas dataframe

# filepath = "C:/Users/User/Documents/A-Flash-Disc/Data Extracts/Result_Listing_Extract_Vertical_41916_phumla.ndamane2023-03-15and1650.csv"
filepath = selected_file
filepath = filepath.replace("\\", "/")

filepath2 = selected_file2
filepath2 = filepath2.replace("\\", "/")


def detect_csv_separator(file_path2):
    with open(file_path2, 'r', newline='') as file:
        # Read a few lines from the file
        sample_lines = [file.readline() for _ in range(0,2)]
    # Define a list of possible separators to check
    separators = [',', ';','|', '\t']
    # Iterate through each separator and count the occurrences in the sample lines
    separator_counts = {}
    for separator in separators:
        counts = [line.count(separator) for line in sample_lines]
        total_count = sum(counts)
        separator_counts[separator] = total_count
    # Determine the separator with the highest count
    max_separator = max(separator_counts, key=separator_counts.get)
    return max_separator

csv_file = filepath2
separator = detect_csv_separator(csv_file)
print(f"The detected separator in the file is '{separator}'")


# Read the filter list in by using the read_csv function in pandas
df = pd.read_csv(filepath2, sep=separator)

# filepath = r"C:\Users\User\Documents\A-Flash-Disc\Bioinformatics\Mitochondrial disorder with complex I deficiency.tsv"
csv_file = filepath
separator = detect_csv_separator(csv_file)
print(f"The detected separator in the file is '{separator}'")

df_filtering = pd.read_csv(filepath, sep=separator)

# Filter the df dataframe "SYMBOL" column using the df_filter "Gene Symbol" column
filter_list = df_filtering["Gene Symbol"].tolist()

df_filtered = df[df["SYMBOL"].isin(filter_list)]
print(df_filtered)

# merge the df_filtering["Sources(; seperated)"] column with the df_filtered dataframe
df_full_dataset = pd.merge(df_filtered, df_filtering, left_on="SYMBOL", right_on="Gene Symbol")

# send the df_filtered dataframe to a csv file
df_full_dataset.to_csv(f"{selected_file2}_and_{selected_file}.csv", index=False)