'''
Basic Course Catalog Parser
Created by Christian Moua

To be used by URI Enrollment Services to categorize
and organize old course catalogs from years 1974+
'''

#   import modules needed
import PyPDF2
import os
import re
import regex

#   List the name of the pdf files in the file 'catalogs/'
catalogs = os.listdir('catalogs/')

#   Compile regular expressions for course year, abbreviation, number, title,
#   and credits
course_year = re.compile('[0-9]{4}')
course_abbrev = re.compile('\([A-Z]{3}\)')
course_num = re.compile('[0-9]{3},?')
course_title = re.compile('.+?(?=I )')
course_units = re.compile('\d')
course_pattern = r"(?:^.* \(([A-Z]{3})\).*|\G(?!^))(?:\r?\n(?!\d{3} |.* \([A-Z]{3}\)[^\S\r\n]*$).*)*\r?\n(\d{3}) (.*?) I, (\d+)"



#   Helper function to obtain course abbreviation from each page
def scanAbbrev(pdfReader, numPages, courseInfo):
    #   print(numPages)
    
    return courseInfo

'''
So far, does everything.  Will try to streamline later.
Finds the year from the course catalog filenames, sorts information
by year in dictionary that shows 
'''
def main():
    #   year dictionary, key is year:allCourses[] is value
    year = {}
    #   allCourses is list of courseInfo lists
    allCourses = []
    #   courseInfo lists course abbreviation, course num, course title, and units
    courseInfo = ['', '', '', '']
    numPages = 0
    
    for log in catalogs:
        #   Retrieves year number from PDF file name
        yearNum = course_year.search(log)
        yearNum.group()
        cat = 'catalogs/' + log
        #   Create PDF file obj
        pdfFileObj = open(cat, 'rb')

        #   Create PDF reader obj
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        #   retrieve number of pages per catalog, send num to scanning func
        if pdfFileObj != None:
            numPages = pdfReader.numPages
            text = ''

            #   search through each page
            for i in range(numPages):
                pageObj = pdfReader.getPage(i)

                text = ''.join(pageObj.extractText())
                
                #   find any matching abbreviation format: (AAA) on page
                #abbreviation = course_abbrev.findall(pageObj.extractText())

                #if abbreviation != []:
                    #   place each abbrev course into a courseInfo[0]
                    #for j in range(len(abbreviation)):
                        #number = course_num.search
                    #print(yearNum.group())
                    #print(i)
                    #print(pageObj.extractText())

            print(text)
        
        else:
            print("ERROR: No file read or cannot be read.")
        
        #   Close PDF file obj
        pdfFileObj.close()

main()
