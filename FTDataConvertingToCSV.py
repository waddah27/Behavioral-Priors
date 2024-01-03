import pandas as pd
import csv
import os
TXT_PATH = './Mocap FT data/FT sensor records/txt/'
CSV_PATH = './Mocap FT data/FT sensor records/csv/'
TXT_FILES = os.listdir(TXT_PATH)
CSV_FILES = os.listdir(CSV_PATH)

def txt_to_csv(file_path: str, output_path: str) -> None:
  """Convert txt files to csv
  """
  with open(file_path, 'r') as file:
    lines = file.readlines()

  # Process the data and split values (assuming space-separated values)
  data = [line.strip().split(',') for line in lines]  # Change delimiter if needed

  # Write data to a CSV file
  csv_file_path = output_path  # Replace with the desired CSV file path

  with open(csv_file_path, 'w', newline='') as csv_file:
      csv_writer = csv.writer(csv_file)
      csv_writer.writerows(data)

  print(f"File '{csv_file_path}' created successfully.")

def numerize_df(df_path: str, output_path: str) -> None:
  """To convert string values in a csv file to floats
  """
  df = pd.read_csv(df_path)
  cols_to_keep = [ ' F/T Sequence', ' Fx', ' Fy', ' Fz', ' Tx', ' Ty']
  cols_rename = [' Fx', ' Fy', ' Fz', ' Tx', ' Ty', ' Tz']
  df = df[cols_to_keep]
  df.columns = cols_rename
  for col in df.columns:
      df[col] = df[col].apply(lambda x: float(x.replace('"', '')))
      df.head()
      df.to_csv(output_path)


for f in TXT_FILES:
    f_name = f.split('.')[0]
    f_name_csv = CSV_PATH+f_name+'.csv'
    txt_to_csv(TXT_PATH+f,CSV_PATH+f_name+'.csv' )
    numerize_df(f_name_csv, f_name_csv)
