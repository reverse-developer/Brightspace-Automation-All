from selenium import webdriver

# from selenium.webdriver.opera.options import Options
URL1 = 'https://sts.algomau.ca/adfs/ls/?SAMLRequest=jdFNS8QwEAbgu%2bB%2fKLk3aWObpqFdWPSysF521YMXSZvpbqFNaiYVf75ZF9Gjt%2fnghYeZZruGsz3A%2bwoYkt1DS1DPk7%2f2b7nOpRmk6HldF2BKzXmpocxNld9BKTuSvIDH0dmWcJqRZIe4ws5i0DbEUcbzNJNpVj3lQpWV4pIWkueikK8k2SKCDzF77yyuM%2fgj%2bI%2bxh%2bfDviXnEBZUjHmYXQCqp5Ob9Up7zQyf2LQwHdlscqfRsgt4f6lo3JHkc54stmT1VjmNIyqrZ0AVenXcPu5VdKrFu%2bB6N5HN7U2SNN9q%2f5%2bg%2fjGTzY9QDEYWmRZpJweRFrWpUimKOpXZIEohjDFdRgPYeBGknR9P54CL7oH2bv6lN%2byKiKCG%2fX3J5gs%3d&RelayState=%2fd2l%2fhome'
URL2 = 'https://remote.algomau.ca/d2l/le/content/8072/viewContent/62610/View'
driver = webdriver.Opera()
driver.get(URL1)

userbox = driver.find_element_by_xpath('//*[@id="userNameInput"]')
userbox.send_keys('giridharan@universitymail.ca')

passbox = driver.find_element_by_xpath('//*[@id="passwordInput"]')
passbox.send_keys('abc123')

loginLink = driver.find_element_by_xpath('//*[@id="submitButton"]')
loginLink.click()

# driver.implicitly_wait(1)

driver.get(URL2)
loginLink = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div/div/a[2]')
loginLink.click()

res = 1

while res < 15:
    owl = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div/div/a[2]')
    owl.click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div/div/a[2]').click()
    res = res + 1