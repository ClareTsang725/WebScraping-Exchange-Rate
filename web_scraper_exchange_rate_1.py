from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# read worksheet by panda
df = pd.read_csv('web_scraper\\webscraper_worksheet.csv')
print(df)

# version one
# manipulate the path to get the exchange rate
print('webscraping...')
output_array = []
for i in range(df.shape[0]):
    row_info = df.loc[i]
    # create driver using chrome
    driver = webdriver.Chrome(executable_path=r'C:\Users\ClareTsang\Desktop\python\chromedriver.exe')

    # obtain information from dataframe
    from_currency = row_info['from_currency']
    to_currency = row_info['to_currency']
    amount = str(row_info['amount_from_curr'])

    print('from currency:', from_currency)
    print('to currency:', to_currency)

    # open the path with driver
    path = 'https://www.x-rates.com/calculator/?from='+from_currency+'&to='+to_currency+'&amount='+amount
    driver.get(path)

    # get the exchange rate/amount
    field1 = driver.find_element(By.XPATH, './/span[@class = "ccOutputRslt"]').text
    field1 = field1.split(' ')
    output = field1[0]
    output_array.append(output)

# change df
df['amount_to_curr'] = output_array
df['time'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# print the output of of the worksheet
df.to_csv('web_scraper\\webscraper_worksheet_ouput.csv', index=False)
print('finish printing output file.')


