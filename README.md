Mitochondrial Genome Filtering Script
Written by: Dieter van der Westhuizen
Date: 2023

Description
This script is designed for filtering mitochondrial genome data in a bioinformatics pipeline. Given an input .txt file containing filter criteria and a .tsv file containing the dataset, the script filters the dataset based on the specified criteria and outputs the filtered data to a new CSV file.

Features
User-friendly interface: Provides a list of available .txt and .tsv files in the current working directory for the user to select.

Separator detection: Dynamically detects the separator used in the input files (such as comma, semicolon, pipe, or tab) for accurate reading.

Filtering mechanism: Efficiently filters the .tsv dataset using criteria specified in the .txt file and merges additional information from the filter list into the final result.

CSV output: Exports the filtered dataset to a new CSV file, which is named by combining the names of the .txt and .tsv files.

How to Use
Place the script in a directory containing your .txt and .tsv files.

Run the script. You'll first be prompted to select a .txt file containing your filter criteria:

markdown
Copy code
Available TXT files:
1. criteria.txt
2. another_criteria.txt
Select a TXT file by entering the corresponding number:
Next, you'll be prompted to select a .tsv file containing the dataset:
markdown
Copy code
Available TSV files:
1. dataset.tsv
2. another_dataset.tsv
Select a CSV file by entering the corresponding number:
The script will then detect the separators, filter the dataset, and save the result to a new CSV file in the same directory.

Check the newly generated CSV file for your filtered results.

Requirements
Python environment with the pandas library installed.
Note
Ensure that the .txt file contains a column named "Gene Symbol" and the .tsv file has a column named "SYMBOL" for the filtering to work correctly.

Instructions to Run the Script in Anaconda
1. Install Anaconda
If you haven't installed Anaconda yet:

Visit the Anaconda Individual Edition download page.
Download the appropriate version for your operating system.
Follow the installation instructions for your platform: Windows, macOS, or Linux.
2. Create a New Conda Environment (Recommended)
Although you can use the base environment in Anaconda, it's generally recommended to create a new environment for each project to manage dependencies cleanly.

Open the Anaconda Navigator (a GUI tool included with Anaconda) or the Anaconda prompt/terminal.

Create a new environment:

bash
Copy code
conda create --name mito_filtering python=3.8
Replace mito_filtering with any name you prefer for your environment, and 3.8 with your preferred Python version.

Activate the new environment:

bash
Copy code
conda activate mito_filtering
3. Install Required Libraries
Your script requires the pandas library. Install it in your activated environment:

bash
Copy code
conda install pandas
4. Navigate to Your Script's Directory
Change your current directory to where your script is located:

bash
Copy code
cd path_to_your_script_directory
Replace path_to_your_script_directory with the path to the directory where your script is located.

5. Run Your Script
Execute the script with:

bash
Copy code
python script_name.py
Replace script_name.py with the name of your script.

6. Deactivate the Environment (Optional)
After you're done, you can deactivate the environment:

bash
Copy code
conda deactivate
