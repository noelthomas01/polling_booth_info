# polling_booth_info
Scrapped the tables from a website to store it as a .csv file.
I was assigned this task by an NGO as a test. I used selenium to to extract the data since i had to automate the website, and used the find_element_by_xpath extensively 
to get the data. I had to unhide some of the html text since it was not accessible directly, so i used the 'driver.execute_script' command to unhide the hidden html text.

Then i extracted the tables and i saved individual tables as .csv files and also, made a master .csv file which would save all the tables in one table using pd.concat
