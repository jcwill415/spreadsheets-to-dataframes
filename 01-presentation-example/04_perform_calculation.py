
import csv
from datetime import datetime

filename = r'data\WMT_US.csv'

records = []

with open(filename, 'r') as f:
    rows = csv.reader(f)

    # skip header row
    header = next(f)

    for row in rows:
        # print(row)
        # ['WMT US', 'WAL-MART STORES INC', '12/31/2014', '476293988352', '460271988736']

        # convert string to date object
        row_date = datetime.strptime(row[2], "%m/%d/%Y")
        # print(row_date)
        # 2003-12-31 00:00:00
        # gives us ability to ask for year
        row_date_year = row_date.year

        # need to convert sales and expenses values from string to integer
        # so can perform mathmatical operations
        row_sales = int(row[3])
        row_expenses = int(row[4])

        # perform profit calculation
        profit = row_sales - row_expenses

        print(f"{row_date_year} Profit = {profit:,}")

"""
Output:

    2014 Profit = 16,021,999,616
    2013 Profit = 16,999,000,064
    2012 Profit = 15,699,000,320
    2011 Profit = 16,389,000,192
    2010 Profit = 14,334,999,552
    2009 Profit = 13,400,000,512
    2008 Profit = 12,730,999,808
    2007 Profit = 11,283,999,744
    2006 Profit = 11,230,999,552
    2005 Profit = 10,266,999,808
    2004 Profit = 9,054,000,128
    2003 Profit = 7,954,999,808
"""

