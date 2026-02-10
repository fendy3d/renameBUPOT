import pdfplumber
import pandas as pd
import os
import csv

pathToPdfs = os.getcwd()+"/dropPdfHere/"
userUnderstand = input("\n!!! WARNING !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")

while userUnderstand != 'y':
    userUnderstand = input("\n!!! I REPEAT !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")    

typeOfBupot = input("What BUPOT is this? Press\n'1' for BP21\n'2' for BPPU (Made by UJK)\n'3' for BPPU (Made by customer) \nAnswer: ")

def printText(list_of_texts):
    counter = 0
    
    for text in list_of_texts:
        print(str(counter) + ": " + text)
        counter += 1

def month_name_to_number(month_name):
    
    month_name = month_name.upper() #uppercase all letteres

    # Dictionary mapping Bahasa month names to their numbers
    month_mapping = {
        "JANUARI": "01",
        "FEBRUARI": "02",
        "MARET": "03",
        "APRIL": "04",
        "MEI": "05",
        "JUNI": "06",
        "JULI": "07",
        "AGUSTUS": "08",
        "SEPTEMBER": "09",
        "OKTOBER": "10",
        "NOVEMBER": "11",
        "DESEMBER": "12"
    }
    
    # Convert month name to its number
    return month_mapping.get(month_name, "Invalid month name")

for _, _, files in os.walk(pathToPdfs):
    for filename in files:
        if '.pdf' in filename:
            
            pdf = pdfplumber.open(pathToPdfs + filename)
            num_pages = len(pdf.pages)
            list_of_texts = []
            for page_number in range(num_pages):
                page = pdf.pages[page_number] # get the page
                texts = page.extract_text()
                list_of_texts += texts.split('\n')
                list_of_texts = [item for item in list_of_texts if item and str(item).strip()] # remove all empty breakline

            # printText(list_of_texts)

            if (typeOfBupot == '1'): # if it's BP21
                
                name = list_of_texts[9].split(': ')[-1]
                
                document_number = list_of_texts[6].split(' ')[0]
                month, year = list_of_texts[6].split(' ')[1].split("-")
                
                old_file_directory = pathToPdfs + filename
                new_name = name + '-BP21-' + year + '-' + month + '-' + document_number + '.pdf'
                new_file_directory = pathToPdfs + new_name
                
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '2'): # if it's BPPU (made by UJK)

                name = list_of_texts[9].split(': ')[-1] # Name of dipotong
                
                document_number = list_of_texts[6].split(' ')[0]
                month, year = list_of_texts[6].split(' ')[1].split("-")
                
                old_file_directory = pathToPdfs + filename
                new_name = year + '-' + month + '-' + '-BPPU-' + name + '_' + document_number + '.pdf'
                new_file_directory = pathToPdfs + new_name
                
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '3'): # if it's BPPU (made by customer)

                name = list_of_texts[35].split(': ')[-1] # Name of dipotong
                
                document_number = list_of_texts[6].split(' ')[0]
                month, year = list_of_texts[6].split(' ')[1].split("-")
                
                old_file_directory = pathToPdfs + filename
                new_name = year + '-' + month + '-BPPU-' + name + '_' + document_number + '.pdf'
                new_file_directory = pathToPdfs + new_name
                
                os.rename(old_file_directory, new_file_directory)

            else:
                print ("Code not updated yet. Contact Fendy.")
            
            pdf.close()
            
