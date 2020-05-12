import sys
import os
import camelot
import pandas as pd
from pandas import ExcelWriter


argInput = sys.argv[1]

def makeDF(fileName):
    tables = camelot.read_pdf(fileName, pages = '1-end')
    columnToData = dict()
    for table in tables:
        data = table.df.loc[1:,:]
        header = table.df.loc[0,:].to_string()
        
        try:
            columnToData[header] = pd.concat([columnToData[header], data], ignore_index = True)
        except KeyError:
            columnToData[header] = table.df
    return columnToData, os.path.splitext(fileName)[0] + '.xlsx'


def save_xls(dict_df, path):
    """
    Save a dictionary of dataframes to an excel file, with each dataframe as a seperate page
    """
    writer = ExcelWriter(path)
    for i, key in enumerate(dict_df):
        dict_df[key].to_excel(writer, str(i), index = False)

    writer.save()


# Script methods if the input argument is a directory
if os.path.isdir( argInput):
    # Set script directory to directory of pdf files
    os.chdir(argInput)
    #get all files in direcctory
    files = []
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        files.extend(filenames)
        break

    for f in files:
        head, tail = os.path.splitext(f)
        if tail == '.pdf':
            dict_df, path = makeDF(f)
            save_xls(dict_df, path)

# Script methods if the input argument is an individual pdf file
else:
    dict_df, path = makeDF(argInput)
    save_xls(dict_df, path)
