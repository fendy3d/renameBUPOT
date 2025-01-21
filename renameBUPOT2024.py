import pdfplumber
import pandas as pd
import os
import csv

pathToPdfs = os.getcwd()+"/dropPdfHere/"
userUnderstand = input("\n!!! WARNING !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")

while userUnderstand != 'y':
    userUnderstand = input("\n!!! I REPEAT !!!\nPlease make sure that all pdf in the folder are ALL OF THE SAME TYPE.\nPress 'y' if you have done this.")    

typeOfBupot = input("What BUPOT is this? Press\n'1' for pph 21/26 Formulir 1721-VI\n'2' for pph 21/26 Formulir 1721-A1\n'3' for pph 4/15/22/23\n'4' for pph 23 Formulir 1724 - III\n'5' for pph 23 Formulir 1724 - III (version2)\n'6' for Formulir BPBS (has 'areastaples' and NPWP is boxes)\n'7' for Formulir BPBS(text overflows)\n'8' for FORMULIR 1721 - VIII\n'9' for FORMULIR BPBS (does not have 'areastaples')\n'10' for Formulir BPBS (has 'areastaples' and NPWP is lines)\n'11' for Formulir 1721-VIII (NPWP is lines)\n'12' for FPK (2025 onwards) \nAnswer: ")

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
            # print ("Old name: " + filename)
            
            pdf = pdfplumber.open(pathToPdfs + filename)
            num_pages = len(pdf.pages)
            
            # printText(list_of_texts)
            if (typeOfBupot == '1'): # if it's pph 21/26 (Tidak Final)
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[7].split(': ')[-1].split(" - ")
                month = masa_pajak[0]
                year = masa_pajak[1]
                
                name = list_of_texts[11].split(': ')[-1]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = name + '-PPH21BUPOT-' + year + '-' + month + '.pdf'
                new_file_directory = pathToPdfs + new_name

                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '2'): # if it's pph 21/26 (Pegawai Tetap)

                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                year = '20' + list_of_texts[0].split(' ')[1]
                name = list_of_texts[5].split(' ')[0]

                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = name + '-PPH21BUPOT-' + year + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '3'): # if it's pph 4/15/22/23

                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                entity_code = 2 # Entity code: 1 (for old BUPOT), 2 (for new BUPOT)
                if(entity_code == 1):
                    nomor_bupot = list_of_texts[6].split(':')[-1]
                    masa_pajak = list_of_texts[24].split(' ')[0]
                    month = "{:02d}".format(int(masa_pajak.split('-')[0])) # make the month has leading 0 if single digit
                    year = masa_pajak.split('-')[1]
                    entity = list_of_texts[33].split('Wajib Pajak : ')[-1]

                elif(entity_code == 2):
                    nomor_bupot = list_of_texts[4].split(':')[-1].split(" H.4")[0].replace(" ", "")
                    masa_pajak = list_of_texts[15].split(' ')[0]
                    month, year = masa_pajak.split('-')
                    month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                    entity = list_of_texts[10].split(' : ')[-1]

                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = entity + '-' + year + '-' + month + '-' + nomor_bupot+ '.pdf'
                new_file_directory = pathToPdfs + new_name
                
                os.rename(old_file_directory, new_file_directory)
            
            elif (typeOfBupot == '4'): # if it's pph 23 (FORM 1724 - III) - 2022 format
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[25].split(' ')[0]
                nomor_bupot = list_of_texts[6].split(' : ')[-1]
                month, year = masa_pajak.split('-')
                month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                name = list_of_texts[13].split(': ')[-1]

                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = name + '-PPH23BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '5'): # if it's pph 23 (FORM 1724 - III) - 2021 format
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[24].split(' ')[0]
                nomor_bupot = list_of_texts[6].split(':')[-1]
                month, year = masa_pajak.split('-')
                month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                name = list_of_texts[12].split(': ')[-1]

                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = name + '-PPH23BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '6'): # if it's Formulir BPBS
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[16].split(' ')[0]
                kode_pajak = list_of_texts[16].split(' ')[1]
                nomor_bupot = list_of_texts[4].split(': ')[-1].split(' H')[0].replace(' ', '')
                month, year = masa_pajak.split('-')
                month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                name = list_of_texts[11].split(': ')[-1]
                firstTwelveLettersOfName = name.replace(' ','')[:12]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                # new_name = firstTwelveLettersOfName + '-PPH4(2)BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_name = firstTwelveLettersOfName + "_" +kode_pajak + "_" + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '7'): # if it's Formulir BPBS (text overflows)
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[17].split(' ')[0]
                kode_pajak = list_of_texts[17].split(' ')[1]
                nomor_bupot = list_of_texts[4].split(': ')[-1].split(' H')[0].replace(' ', '')
                month, year = masa_pajak.split('-')
                month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                name = list_of_texts[10].split(': ')[-1]
                firstTwelveLettersOfName = name.replace(' ','')[:12]
                
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                # new_name = firstTwelveLettersOfName + '-PPH4(2)BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_name = firstTwelveLettersOfName + "_" +kode_pajak + "_" + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)
            
            elif (typeOfBupot == '8'): # if it's FORMULIR 1721 - VIII
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[4].split(': ')[-1].split(" - ")
                month = masa_pajak[0]
                year = masa_pajak[1]
                name = list_of_texts[7].split(': ')[-1]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = name + '-PPH21BUPOT-' + year + '-' + month + '.pdf'
                new_file_directory = pathToPdfs + new_name

                os.rename(old_file_directory, new_file_directory)
            
            elif (typeOfBupot == '9'): # if it's Formulir BPBS version 2
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[14].split(' ')[0]
                kode_pajak = list_of_texts[14].split(' ')[1]
                nomor_bupot = list_of_texts[3].split(': ')[-1].split(' H')[0].replace(' ', '')
                month, year = masa_pajak.split('-')
                month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                name = list_of_texts[8].split(': ')[-1]
                firstTwelveLettersOfName = name.replace(' ','')[:12]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = firstTwelveLettersOfName + "_" +kode_pajak + "_" + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '10'): # if it's Formulir BPBS (has 'areastaples' and NPWP is lines)
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[15].split(' ')[0]
                kode_pajak = list_of_texts[15].split(' ')[1]
                nomor_bupot = list_of_texts[4].split(': ')[-1].split(' H')[0].replace(' ', '')
                month, year = masa_pajak.split('-')
                month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                name = list_of_texts[10].split(': ')[-1]
                firstTwelveLettersOfName = name.replace(' ','')[:12]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                # new_name = firstTwelveLettersOfName + '-PPH4(2)BUPOT-' + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_name = firstTwelveLettersOfName + "_" +kode_pajak + "_" + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '11'): # if it's Formulir 1721-VIII (NPWP is lines)
                
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')

                masa_pajak = list_of_texts[4].split(' : ')[-1]
                kode_pajak = list_of_texts[16].split(' ')[0]
                nomor_bupot = list_of_texts[4].split(': ')[1].split(' ')[0]
                month, year = masa_pajak.split(' - ')
                month = "{:02d}".format(int(month)) # make the month has leading 0 if single digit
                name = list_of_texts[8].split(': ')[-1]
                # firstTwelveLettersOfName = name.replace(' ','')[:12]
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                # new_name = firstTwelveLettersOfName + "_" +kode_pajak + "_" + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_name = name + "-" + "PPH21BUPOT" + "-" + year + '-' + month + '-' + nomor_bupot + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)

            elif (typeOfBupot == '12'): # if it's FPK (2025 onwards)
                list_of_texts = []
                for page_number in range(num_pages):
                    page = pdf.pages[page_number] # get the page
                    texts = page.extract_text()
                    list_of_texts += texts.split('\n')
                tax_invoice_number = next((line for line in list_of_texts if 'Kode dan Nomor Seri Faktur Pajak' in line), None).split(': ')[1]
                invoice_number = next((line for line in list_of_texts if 'Referensi:' in line), None).split(': ')[1].replace(")", "")
                day,month,year = next((line for line in list_of_texts if 'KOTA ADM. JAKARTA UTARA, ' in line), None).split(', ')[1].split(" ")
                month = month_name_to_number(month)
                
                pdf.close()
                old_file_directory = pathToPdfs + filename
                new_name = tax_invoice_number + "-" + year + '-' + month + '-' + invoice_number + '.pdf'
                new_file_directory = pathToPdfs + new_name
                os.rename(old_file_directory, new_file_directory)


            
            else:
                print ("Code not updated yet. Contact Fendy.")
            
            pdf.close()
            
