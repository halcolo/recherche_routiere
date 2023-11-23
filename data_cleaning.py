import os
import csv
import pandas as pd
import numpy as np
from numpy import nan 
import csv
# import matplotlib.pyplot as plt

def clean_quotes_semicolon(input_file:str, output_file:str) -> None:
    """
    Clean a CSV file by removing colons, semicolons, and quotes from each field.
    
    Parameters:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output CSV file.
    
    Returns:
        None
    """
    data = list()
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')

        # Create a new CSV file to write the cleaned data
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # reader[0] = reader[0].lower()

            for row in reader:
                # Cleaning
                row = [field.replace('"', '').replace("'", "") for field in row]
                row = [field.replace(';', '').replace(',', '.') for field in row]
                
                # Cleaned row write
                writer.writerow(row)
                
                
if __name__ == '__main__':
    current_path = os.getcwd()
    data_path = current_path + '/data'
    year = '2022'
    
    # Setting up input and output files
    files = {
        "caracteristiques":["carcteristiques-{year}.csv", "carcteristiques-{year}-cleaned.csv"],
        "lieux":["lieux-{year}.csv", "lieux-{year}-cleaned.csv"],
        "usagers":["usagers-{year}.csv", "usagers-{year}-cleaned.csv"],
        "vehicules":["vehicules-{year}.csv", "vehicules-{year}-cleaned.csv"]
    }

    # Run cleaning
    for g_file in files.values():
        input_file = f'{data_path}/2022/{g_file[0].replace("{year}",year)}'  
        output_file = f'{data_path}/cleaned/{year}/{g_file[1].replace("{year}", year)}'    
        clean_quotes_semicolon(input_file=input_file,
                            output_file=output_file)  
        
    # Read cleaned data into dataframes
    caracteristiques = pd.read_csv(filepath_or_buffer=f'{data_path}/cleaned/{year}/{files["caracteristiques"][1].replace("{year}", year)}')
    lieux = pd.read_csv(filepath_or_buffer=f'{data_path}/cleaned/{year}/{files["lieux"][1].replace("{year}", year)}')
    usagers = pd.read_csv(filepath_or_buffer=f'{data_path}/cleaned/{year}/{files["usagers"][1].replace("{year}", year)}')
    vehicules = pd.read_csv(filepath_or_buffer=f'{data_path}/cleaned/{year}/{files["vehicules"][1].replace("{year}", year)}')
    
    # Merge all dataframes
    full_data = caracteristiques.merge(lieux, on="num_acc", how='left')\
        .merge(usagers, on='num_acc', how='left')\
            .merge(vehicules, on='num_acc', how='left')
    
    # Deleting dubs
    full_data_dubs = full_data.duplicated(subset=['num_acc'])
    print('joined data total duplicated: %s / %s' % (len(full_data[full_data_dubs]), len(full_data)))
    full_data = full_data.drop_duplicates(subset=['num_acc'])
    print('Droped duplicates: %s / %s' % (len(full_data[full_data_dubs]), len(full_data)))
    
    full_data = full_data.fillna(nan)
    # Setting up duplicateds using ID as key
    
    #saving to csv
    full_data.to_csv(f'{data_path}/full_data.csv', index=False)