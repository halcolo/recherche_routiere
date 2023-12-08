import os
import csv
import pandas as pd
import numpy as np
import csv
import re
import matplotlib.pyplot as plt



def clean_csv(input_file:str, output_file:str) -> None:
    """
    Clean a CSV file by removing colons, semicolons, and quotes from each field.
    
    Parameters:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output CSV file.
    
    Returns:
        None
    """

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')

        # Create a new CSV file to write the cleaned data
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for row in reader:
                # Cleaning
                row = [re.sub(r'[^\x00-\x7F]+', '', field) for field in row]
                row = [field.replace('"', '').replace("'", "").replace(' ', '') for field in row]
                row = [field.replace(';', '').replace(',', '.') for field in row]

                # Cleaned row write
                writer.writerow(row)
                
def filter_columns(df:pd.DataFrame, column_list:list) -> pd.DataFrame:
    return df.drop(columns=column_list)