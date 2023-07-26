# Mitochondrial Genome Filtering Script

## Author Information
**Written by:** Dieter van der Westhuizen  
**Date:** 2023

## Overview
This script is designed for filtering mitochondrial genome data in a bioinformatics pipeline. Given an input `.txt` file containing filter criteria and a `.tsv` file containing the dataset, the script filters the dataset based on the specified criteria and outputs the filtered data to a new CSV file.

## Main Features

- **User-friendly interface**: Provides a list of available `.txt` and `.tsv` files in the current working directory for the user to select.
- **Separator detection**: Dynamically detects the separator used in the input files (such as comma, semicolon, pipe, or tab) for accurate reading.
- **Filtering mechanism**: Efficiently filters the `.tsv` dataset using criteria specified in the `.txt` file and merges additional information from the filter list into the final result.
- **CSV output**: Exports the filtered dataset to a new CSV file, which is named by combining the names of the `.txt` and `.tsv` files.

## Usage Instructions

1. Place the script in a directory containing your `.txt` and `.tsv` files.
2. Run the script. You'll first be prompted to select a `.txt` file containing your filter criteria.
3. Next, you'll be prompted to select a `.tsv` file containing the dataset.
4. The script will then detect the separators, filter the dataset, and save the result to a new CSV file in the same directory.
5. Check the newly generated CSV file for your filtered results.

## Script Requirements

- Python environment with the `pandas` library installed.
- Ensure that the `.txt` file contains a column named "Gene Symbol" and the `.tsv` file has a column named "SYMBOL" for the filtering to work correctly.

## Running the Script with Anaconda

### Setting Up Anaconda

1. If you haven't installed Anaconda yet, download and install it from the [official website](https://www.anaconda.com/products/distribution#download-section).
2. Open Anaconda Navigator or the Anaconda terminal.

### Creating and Activating a New Environment

1. Create a new environment with the desired Python version (e.g., `3.8`):  
    ```bash
   conda create --name mito_filtering python=3.8
2. Activate the environment:
    ```bash
    conda activate mito_filtering
3. Installing Dependencies
Install the required pandas library:
    ```bash
    conda install pandas
4. Running the Script
Navigate to the script directory:
    ```bash
    cd path_to_your_script_directory
5. Run the script:
    ```bash
    python mitochondrial_analysis.py
6. Closing Anaconda
Once done, you can deactivate the Anaconda environment:
    ```bash
    conda deactivate

## Running the Script as a Jupyter Notebook
###Setting Up Jupyter Notebook in Anaconda
Ensure you've activated the Anaconda environment where you have the required dependencies installed. If you haven't, refer to the instructions in the "Setting Up Anaconda" and "Creating and Activating a New Environment" sections above.

Install jupyter within the environment:

    ```bash
      conda install jupyter

Launch Jupyter Notebook:

    ```bash
    jupyter notebook

## Running the Script in the Jupyter Notebook
You can run each cell by selecting the cell and clicking the "Run" button or by pressing Shift + Enter.
Make sure you run the cells in order, especially if they have dependencies on previous cells.
You'll see the outputs (e.g., print statements) right below each cell after you run it.
If you want to save the outputs, click on "File" and then "Save and Checkpoint".
Once you're done, you can close the Jupyter Notebook browser tab and stop the Jupyter server in your terminal by pressing Ctrl + C twice.
