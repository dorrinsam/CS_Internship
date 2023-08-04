# Task#3 of Step#4

import xlrd
import datetime
import warnings
import zipfile
import requests
import urllib
import io


url = 'https://www.histdata.com/download-free-forex-historical-data/?/excel/1-minute-bar-quotes/eurusd/2018'

# mahze mohkal karii
urllib.request.urlretrieve(url, 'TEST.txt')
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
url = 'https://s17.picofile.com/d/8428234626/92fce4fb-232e-4624-87cf-338e4c444148/BarsaServiceClient.zip'
url_1 = requests.get(url, stream=True)
io.BytesIO(url_1.content)
zipp = zipfile.ZipFile('HISTDATA_COM_XLSX_EURUSD_M12018.zip')
zipp.extractall()

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True
workbook = xlrd.open_workbook('DAT_XLSX_EURUSD_M1_2018.xlsx')
worksheet = workbook.sheet_by_index(0)
num_of_rows = worksheet.nrows
num_of_columns = worksheet.ncols

# last part ...
for i in range(0, 10):
    r = worksheet.row_values(i, start_colx=0, end_colx=None)
    r[0] = datetime.datetime(*xlrd.xldate_as_tuple(r[0], workbook.datemode)).strftime('%Y-%m-%d %H:%M:%S')
    print(r)