from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# read worksheet by panda
df = pd.read_csv('web_scraper\\webscraper_worksheet.csv')
print(df)
# specify currency column as index
currency_df = pd.read_csv('web_scraper\\currency_option.csv', index_col=0)
print(currency_df)

# version 2  (by dropdown list)
# download exchange rate
print('webscraping...')
output_array = []
for i in range(df.shape[0]):
    row_info = df.loc[i]
    driver = webdriver.Chrome(executable_path=r'C:\Users\ClareTsang\Desktop\python\chromedriver.exe')
    path = 'https://www.x-rates.com/calculator/?from=AUD&to=EUR&amount=1'
    driver.get(path)
    from_currency = row_info['from_currency']+' - '+currency_df.loc[row_info['from_currency'], 'Name']
    print('from currency:', from_currency)
    to_currency = row_info['to_currency']+' - '+currency_df.loc[row_info['to_currency'], 'Name']
    print('to currency:', to_currency)
    amount = int(row_info['amount_from_curr'])
    # version 2 select from drop down list

    field1 = driver.find_element(By.ID, "from")
    field1.click()
    driver.find_element(By.XPATH, "//div[@class='ac_results']/ul/li[.='" + from_currency + "']").click()

    field2 = driver.find_element(By.ID, "to")
    field2.click()
    driver.find_element(By.XPATH, "//div[@class='ac_results']/ul[@id='to_scroller']/li[.='" + to_currency + "']").click()

    # amount
    field3 = driver.find_element(By.XPATH, "//div[@class='converterAmountWrapper']")
    field3.click()
    field4 = driver.find_element(By.XPATH, '//*[@id="amount"]')
    field4.send_keys(amount)
    driver.find_element(By.XPATH, './/span[@class = "contentArrow"]').click()

    # output
    output_text = driver.find_element(By.XPATH, './/span[@class = "ccOutputRslt"]').text
    output_text = output_text.split(' ')
    output = output_text[0]
    output_array.append(output)
print(output_array)
df['amount_to_curr'] = output_array
# print the output of of the worksheet
df.to_csv('web_scraper\\webscraper_worksheet_ouput_v2.csv', index=False)
print('finish printing output file.')



