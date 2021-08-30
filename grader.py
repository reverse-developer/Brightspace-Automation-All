import time
from selenium import webdriver

# from selenium.webdriver.opera.options import Options
URL1 = 'https://sts.algomau.ca/adfs/ls/?SAMLRequest=jdFNS8QwEAbgu%2bB%2fKLk3aWObpqFdWPSysF521YMXSZvpbqFNaiYVf75ZF9Gjt%2fnghYeZZruGsz3A%2bwoYkt1DS1DPk7%2f2b7nOpRmk6HldF2BKzXmpocxNld9BKTuSvIDH0dmWcJqRZIe4ws5i0DbEUcbzNJNpVj3lQpWV4pIWkueikK8k2SKCDzF77yyuM%2fgj%2bI%2bxh%2bfDviXnEBZUjHmYXQCqp5Ob9Up7zQyf2LQwHdlscqfRsgt4f6lo3JHkc54stmT1VjmNIyqrZ0AVenXcPu5VdKrFu%2bB6N5HN7U2SNN9q%2f5%2bg%2fjGTzY9QDEYWmRZpJweRFrWpUimKOpXZIEohjDFdRgPYeBGknR9P54CL7oH2bv6lN%2byKiKCG%2fX3J5gs%3d&RelayState=%2fd2l%2fhome'
URL2 = 'https://remote.algomau.ca/d2l/lms/grades/my_grades/main.d2l?ou=8130'
driver = webdriver.Opera()
driver.get(URL1)

fname='ethuku.csv'
f = open(fname, 'a', encoding='utf-8')

userbox = driver.find_element_by_xpath('//*[@id="userNameInput"]')
userbox.send_keys('giridharan@university.ca')

passbox = driver.find_element_by_xpath('//*[@id="passwordInput"]')
passbox.send_keys('abcd123')

loginLink = driver.find_element_by_xpath('//*[@id="submitButton"]')
loginLink.click()

# driver.implicitly_wait(1)
time.sleep(5)
driver.get(URL2)
perc = driver.find_element_by_xpath('//*[@id="z_a"]/tbody/tr[3]/td[4]/div/div')
perce = perc.text
print (perce)

if len(perce) > 99:
    print ('you received max grade')

perct = driver.find_element_by_xpath('//*[@id="d_content_inner"]')
percet = perct.text
print (percet)

f.write(percet)
