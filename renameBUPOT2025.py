import pdfplumber
import pandas as pd
import os
import csv

pathToPdfs = os.getcwd()+"/dropPdfHere/"
userUnderstand = input("\n!!! WARNING !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")

while userUnderstand != 'y':
    userUnderstand = input("\n!!! I REPEAT !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")    

typeOfBupot = input("What BUPOT is this? Press\n'1' for BP21\n'2' for BPPU (Made by UJK)\n'3' for BPPU (Made by customer) \n'4' for SPT PPN\n'5' for FPK \nAnswer: ")

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

            printText(list_of_texts)

            pdf.close()
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

            elif (typeOfBupot == '4'): # if it's SPT PPN

                month, year = list_of_texts[6].split(' ')[0:2]
                month = month_name_to_number(month)
                
                
                old_file_directory = pathToPdfs + filename
                new_name = year + '-' + month + '-SPT_PPN.pdf'
                new_file_directory = pathToPdfs + new_name
                
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '5'): # if it's FPK
                
                document_number = list_of_texts[5].split(': ')[-1]
                date = [item for item in list_of_texts if "KOTA ADM. JAKARTA UTARA" in item][-1]
                
                month, year = date.split(', ')[1].split(' ')[1:3]
                month = month_name_to_number(month)
                # reference_number = list_of_texts[39].split(': ')[-1].replace(')','')
                reference_number = [item for item in list_of_texts if "(Referensi" in item][-1].split(': ')[-1].replace(')','')
                                
                old_file_directory = pathToPdfs + filename
                new_name = year + '-' + month + '-' + document_number + '-' + reference_number +'.pdf'
                new_file_directory = pathToPdfs + new_name
                print(new_name)
                
                os.rename(old_file_directory, new_file_directory)

            else:
                print ("Code not updated yet. Contact Fendy.")
            
            
            
