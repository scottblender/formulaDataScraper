import sys
import camelot
import pandas as pd

tables = camelot.read_pdf(sys.argv[1], pages = '1-end')


columnToData = dict()
for table in tables:
    data = table.df.loc[1:,:]
    header = table.df.loc[0,:].to_string()
    
    try:
        columnToData[header] = pd.concat([columnToData[header], data], ignore_index = True)
    except KeyError:
        columnToData[header] = table.df

from pandas import ExcelWriter

def save_xls(dict_df, path):
    """
    Save a dictionary of dataframes to an excel file, with each dataframe as a seperate page
    """
    writer = ExcelWriter(path)
    for i, key in enumerate(dict_df):
        dict_df[key].to_excel(writer, str(i), index = False)

    writer.save()


save_xls(columnToData,'results.xlsx')
