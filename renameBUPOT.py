import pdfplumber
import pandas as pd
import os
import csv

pathToPdfs = os.getcwd()+"/dropPdfHere/"

# year = input("What year is this BUPOT? Eg: 2021, 2022 etc")
# month = input("What month is this BUPOT? Eg: 01,05,12 etc")

def printText(list_of_texts):
    counter = 0
    for text in list_of_texts:
        print(counter)
        print(text)
        counter += 1

for _, _, files in os.walk(pathToPdfs):
    for filename in files:
        if '.pdf' in filename:
            print ("Renaming " + filename)
            
            pdf = pdfplumber.open(pathToPdfs + filename)
            page = pdf.pages[0] # get the page
            texts = page.extract_text()
            list_of_texts = texts.split('\n')
            
            bupot = list_of_texts[6].split(':')[-1]
            masa_pajak = list_of_texts[24].split(' ')[0]
            month = "{:02d}".format(int(masa_pajak.split('-')[0])) # make the month has leading 0 if single digit
            year = masa_pajak.split('-')[1]
            entity = list_of_texts[33].split('Wajib Pajak : ')[-1]

            # printText(list_of_texts)
            old_file_directory = pathToPdfs + filename
            new_name = year + '-' + month + '-' + bupot + '-' + entity+'.pdf'
            new_file_directory = pathToPdfs + new_name

            pdf.close()
            
            os.rename(old_file_directory, new_file_directory)
            print ("Success! " + filename + " has been renamed to " + new_name)
