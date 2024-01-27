import pdfplumber
import pandas as pd
import os
import csv

pathToPdfs = os.getcwd()+"/dropPdfHere/"
userUnderstand = input("\n!!! WARNING !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")

while userUnderstand != 'y':
    userUnderstand = input("\n!!! I REPEAT !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")    

typeOfBupot = input("What BUPOT is this? Press\n'1' for pph 21/26 Formulir 1721-VI\n'2' for pph 21/26 Formulir 1721-A1\n'3' for pph 4/15/22/23\n'4' for pph 23 Formulir 1724 - III\n'5' for pph 23 Formulir 1724 - III (version2)\n'6' for Formulir BPBS\n'7' for Formulir BPBS(text overflows)\n'8' for FORMULIR 1721 - VIII\nAnswer: ")

def printText(list_of_texts):
    counter = 0
    for text in list_of_texts:
        print(str(counter) + ": " + text)
        counter += 1

for _, _, files in os.walk(pathToPdfs):
    for filename in files:
        if '.pdf' in filename:
            print ("Old name: " + filename)
            
            pdf = pdfplumber.open(pathToPdfs + filename)
            page = pdf.pages[0] # get the page
            texts = page.extract_text()
            list_of_texts = texts.split('\n')
            
            # printText(list_of_texts)
            if (typeOfBupot == '1'): # if it's pph 21/26 (Tidak Final)
                
                masa_pajak = list_of_texts[7].split(': ')[-1].split(" - ")
                month = masa_pajak[0]
                year = masa_pajak[1]
                
                name = list_of_texts[10].split(': ')[-1]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = name + '-PPH21BUPOT-' + year + '-' + month + '.pdf'
                new_file_directory = pathToPdfs + new_name

                os.rename(old_file_directory, new_file_directory)

            # elif (typeOfBupot == '2'): # if it's pph 21/26 (Pegawai Tetap)

                # year = '20' + list_of_texts[0].split(' ')[1]
                # name = list_of_texts[5].split(' ')[0]

                # pdf.close()
                # old_file_directory = pathToPdfs + filename
                # new_name = name + '-PPH21BUPOT-' + year + '.pdf'
                # new_file_directory = pathToPdfs + new_name
                # os.rename(old_file_directory, new_file_directory)

            # elif (typeOfBupot == '3'): # if it's pph 4/15/22/23

            #     entity_code = 2 # Entity code: 1 (for old BUPOT), 2 (for new BUPOT)
            #     if(entity_code == 1):
            #         nomor_bupot = list_of_texts[6].split(':')[-1]
            #         masa_pajak = list_of_texts[24].split(' ')[0]
            #         month = "{:02d}".format(int(masa_pajak.split('-')[0])) # make the month has leading 0 if single digit
            #         year = masa_pajak.split('-')[1]
            #         entity = list_of_texts[33].split('Wajib Pajak : ')[-1]

            #     elif(entity_code == 2):
            #         nomor_bupot = list_of_texts[4].split(':')[-1].split(" H.4")[0].replace(" ", "")
            #         masa_pajak = list_of_texts[15].split(' ')[0]
            #         month, year = masa_pajak.split('-')
            #         month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
            #         entity = list_of_texts[10].split(' : ')[-1]

            #     pdf.close()
            #     old_file_directory = pathToPdfs + filename
            #     new_name = entity + '-' + year + '-' + month + '-' + nomor_bupot+ '.pdf'
            #     new_file_directory = pathToPdfs + new_name
                
            #     os.rename(old_file_directory, new_file_directory)
            
            # elif (typeOfBupot == '4'): # if it's pph 23 (FORM 1724 - III) - 2022 format
                
            #     masa_pajak = list_of_texts[25].split(' ')[0]
            #     nomor_bupot = list_of_texts[6].split(' : ')[-1]
            #     month, year = masa_pajak.split('-')
            #     month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
            #     name = list_of_texts[13].split(': ')[-1]

            #     pdf.close()
            #     old_file_directory = pathToPdfs + filename
            #     new_name = name + '-PPH23BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
            #     new_file_directory = pathToPdfs + new_name
            #     os.rename(old_file_directory, new_file_directory)

            # elif (typeOfBupot == '5'): # if it's pph 23 (FORM 1724 - III) - 2021 format
                
            #     masa_pajak = list_of_texts[24].split(' ')[0]
            #     nomor_bupot = list_of_texts[6].split(':')[-1]
            #     month, year = masa_pajak.split('-')
            #     month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
            #     name = list_of_texts[12].split(': ')[-1]

            #     pdf.close()
            #     old_file_directory = pathToPdfs + filename
            #     new_name = name + '-PPH23BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
            #     new_file_directory = pathToPdfs + new_name
            #     os.rename(old_file_directory, new_file_directory)

            # elif (typeOfBupot == '6'): # if it's Formulir BPBS
                
            #     masa_pajak = list_of_texts[15].split(' ')[0]
            #     nomor_bupot = list_of_texts[4].split(': ')[-1].split(' H')[0].replace(' ', '')
            #     month, year = masa_pajak.split('-')
            #     month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
            #     name = list_of_texts[28].split(': ')[-1]
            #     firstTwelveLettersOfName = name.replace(' ','')[:12]
                
            #     pdf.close()
            #     old_file_directory = pathToPdfs + filename
            #     new_name = firstTwelveLettersOfName + '-PPH23BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
            #     new_file_directory = pathToPdfs + new_name
            #     os.rename(old_file_directory, new_file_directory)

            # elif (typeOfBupot == '7'): # if it's Formulir BPBS (text overflows)
                
            #     masa_pajak = list_of_texts[17].split(' ')[0]
            #     nomor_bupot = list_of_texts[4].split(': ')[-1].split(' H')[0].replace(' ', '')
            #     month, year = masa_pajak.split('-')
            #     month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
            #     name = list_of_texts[30].split(': ')[-1]
            #     firstTwelveLettersOfName = name.replace(' ','')[:12]
                
            #     pdf.close()
            #     old_file_directory = pathToPdfs + filename
            #     new_name = firstTwelveLettersOfName + '-PPH23BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
            #     new_file_directory = pathToPdfs + new_name
            #     os.rename(old_file_directory, new_file_directory)
            
            elif (typeOfBupot == '8'): # if it's FORMULIR 1721 - VIII
                
                masa_pajak = list_of_texts[4].split(': ')[-1].split(" - ")
                month = masa_pajak[0]
                year = masa_pajak[1]
                
                name = list_of_texts[7].split(': ')[-1]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = name + '-PPH21BUPOT-' + year + '-' + month + '.pdf'
                new_file_directory = pathToPdfs + new_name

                os.rename(old_file_directory, new_file_directory)
            
            else:
                print ("Code not updated yet. Contact Fendy.")
            
            pdf.close()
            print ("Success! New name: " + new_name)
            
