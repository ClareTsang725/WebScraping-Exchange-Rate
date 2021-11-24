from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd

# read worksheet by panda
df = pd.read_csv('web_scraper\\webscraper_worksheet.csv')
print(df)

# version one
# manipulate the path to get the exchange rate
print('webscraping...')
output_array = []
for i in range(df.shape[0]):
    row_info = df.loc[i]
    driver = webdriver.Chrome(executable_path=r'C:\Users\ClareTsang\Desktop\python\chromedriver.exe')
    from_currency = row_info['from_currency']
    to_currency = row_info['to_currency']
    amount = str(row_info['amount_from_curr'])
    path = 'https://www.x-rates.com/calculator/?from='+from_currency+'&to='+to_currency+'&amount='+amount
    driver.get(path)
    field1 = driver.find_element(By.XPATH, './/span[@class = "ccOutputRslt"]').text
    field1 = field1.split(' ')
    output = field1[0]
    output_array.append(output)
df['amount_to_curr'] = output_array
# print the output of of the worksheet
df.to_csv('web_scraper\\webscraper_worksheet_ouput.csv', index = False)
print('finish printing output file.')

# download exchange rate
from_currency = 'AUD - AU Dollar'
to_currency = 'USD - US Dollar'

driver = webdriver.Chrome(executable_path=r'C:\Users\ClareTsang\Desktop\python\chromedriver.exe')
path = 'https://www.x-rates.com/calculator/?from=AUD&to=EUR&amount=1'
driver.get(path)
# version 2 select from drop down list
field1 = driver.find_element(By.ID, "from")
field1.click()
field1.send_keys(from_currency)
field1.send_keys(Keys.ENTER)
driver.refresh()

field2 = driver.find_element(By.ID, "to")
field2.send_keys(to_currency)
field2.send_keys(Keys.ENTER)




