import requests
import webbrowser
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
import time

def PrintFirstResponse(var):
    string = var + " in Bhagavad Gita chapter and verse"
    newUrl = "https://www.google.com/search?q="+string
    req = requests.get("https://www.google.com/search?q="+string)
    soup = BeautifulSoup(req.content, "html.parser")
    firstSearch = None
    if soup.find('h3'):
        firstSearch = soup.find('h3').text
    return firstSearch

kar = pd.read_excel('data2.xlsx', sheet_name="Sheet1")

print("\nWELCOME!! \n\nThis program will search the Chapter and Verse \nof a set of sanskrit words from the google search \nand print it in a file with its name provided by you...\n\n")
time.sleep(4)
# data_file = input("Enter the file name which contains the words \n(excel sheet downloaded from \"Ancient Text Translation\" Google Sheets\nEnter without the extension '.xlsx' =>  ")
kar = pd.read_excel("data2.xlsx", sheet_name="Sheet1")
start = int(input("Enter starting index(as per data2.xlsx)[start from 2 and onwards]: "))
end = int(input("Enter ending index(as per AncientTextTranslation.xlsx): "))
file_name = input("Enter file name to store the searched information: ")


for i in range(start, end+1):
        file = open(file_name+".txt","a")
        variable = kar["Word List"][i-2]
        variable = variable.replace("[", "")
        variable = variable.replace("]", "")
        returnedStatement = PrintFirstResponse(variable)
        if returnedStatement==None:
            returnedStatement = "NOT FOUND"
        print(str(i)+": " +variable)
        file.write(str(i)+"  "+returnedStatement+"\n")

print("\n\nThank You, Please check: ",file_name+".txt")
