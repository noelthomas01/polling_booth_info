import selenium
from selenium.webdriver import Firefox
import time
import pandas as pd

path = 'C:/geckodriver.exe'
driver = Firefox(executable_path = path)
url = 'https://chanakyya.com/Election-Results?electionType=Assembly'
driver.get(url)
time.sleep(10)
#unhiding the state selection drop down
hidden = driver.find_element_by_id('state-select')
driver.execute_script("""arguments[0].setAttribute('style', '')""", hidden)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/ng-include/section/div/div[3]/div/div/div/select/option[23]').click()
time.sleep(2)
#unhiding the assembly selection drop down
hidden_assembly = driver.find_element_by_id('assembly-select')
driver.execute_script("""arguments[0].setAttribute('style', '0')""", hidden_assembly)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/ng-include/section/div/div[3]/div[2]/div/div/div/select/option[2]').click()
#unhiding the poll booth selection drop down
hidden_poll = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/ng-include/section/div/div[3]/div[3]/div/div/select')
driver.execute_script("""arguments[0].setAttribute('style', '0')""", hidden_poll)

ass_list = []
parl_list = []
for i in range(331): #as there are polling booths from index(2:332)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/ng-include/section/div/div[3]/div[3]/div/div/select/option[%d]' %(i+2)).click() #this finds the poll booth, i shifts to different booths
    name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/ng-include/section/div/div[3]/div[3]/div/div/select/option[%d]' %(i+2)).text #saves the polling booth name
    df = pd.read_html(driver.page_source) #reads the tables on the site
    #some booths have both parliament and assembly data and some only have assembly data
    if len(df) == 5: #has both parliament and assembly data
        assembly = df[3]
        assembly['Booth'] = name
        ass_list.append(assembly)
        parliament = df[4]
        parliament['Booth'] = name
        parl_list.append(parliament)
    elif len(df) ==3: #has only assembly
        assembly = df[2]
        assembly['Booth'] = name 
        ass_list.append(assembly)
        parliament = pd.DataFrame() #empty dataframe
    assembly.to_csv("Assembly/%s.csv" %name)
    parliament.to_csv("Parliament/%s.csv" %name)
    # print(name," ",i)
final_assembly = pd.concat(ass_list)
final_parliament = pd.concat(parl_list)
final_assembly.to_csv("AssemblyPolls.csv")
final_parliament.to_csv("ParliamentPolls.csv")
