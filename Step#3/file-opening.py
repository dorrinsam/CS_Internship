# Needed modules
import requests
import urllib.request
import zipfile
import xlrd
import datetime

# Downloading...
url = 'https://www.histdata.com/download-free-forex-historical-data/?/excel/1-minute-bar-quotes/eurusd/2018'
urllib.request.urlretrieve(url, 'TEST.txt')

url = 'https://s17.picofile.com/d/8428234626/92fce4fb-232e-4624-87cf-338e4c444148/BarsaServiceClient.zip'
get_url = requests.get(url, stream=True)

# Unzipping and extraction...
z = zipfile.ZipFile('HISTDATA_COM_XLSX_EURUSD_M12018.zip')
z.extractall()

# Decoding part ...
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

workbook = xlrd.open_workbook('DAT_XLSX_EURUSD_M1_2018.xlsx')
worksheet = workbook.sheet_by_index(0)
num_of_rows = worksheet.nrows
num_of_columns = worksheet.ncols

for i in range(0, 15):
    r = worksheet.row_values(i, start_colx=0, end_colx=None)
    r[0] = datetime.datetime(*xlrd.xldate_as_tuple(r[0], workbook.datemode)).strftime('%Y-%m-%d %H:%M:%S')
    print(r)

# The most ANOYYING fact of this task is:
# Using Python ----> """version 3.7"""
# and
# xlrd module ----> """version 1.2.0"""
# are 2 MUSTS :)
