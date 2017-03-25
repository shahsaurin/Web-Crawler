from bs4 import BeautifulSoup
import urllib2
import requests
import time
import os

#os.mkdir("----Enter your path here------\Saurin_Shah\Task1")
#os.chdir("----Enter your path here------\Saurin_Shah\Task1")

seed = "https://en.wikipedia.org/wiki/Sustainable_energy"
list2=[]
list3=[]
list4=[]
list5=[]
urlcounter = 0

time.sleep(1)
r = requests.get(seed)
data =  r.text
parsed_page = BeautifulSoup(data, "html.parser")                       # getting page in HTML format

file_url = open("url_list.txt", "a+")
file_url.write(seed + "\n")
file_url.close()
urlcounter = urlcounter + 1                                              # Check if seed is not in the URLlist then add it and also make a raw data file for it
file_rawdata = open("crawler_file_"+str(urlcounter)+".txt", "a+")
rawdata_to_string = str(parsed_page)
file_rawdata.write(rawdata_to_string)
file_rawdata.close()

for link in parsed_page.body.find_all('a',href=True):
    temp = str(link.get('href').encode('utf-8'))
    temp1 = temp.split('/')
    if '#' not in temp :
        if (len(temp1)>1 and temp1[1] == "wiki" and ":" not in temp):
            temp = "https://en.wikipedia.org" + temp
            temp2 = str(link.contents)
            if ("solar" in temp.lower() or "solar" in temp2.lower()):
                list2.append(temp)

for p2 in list2:
    file_url = open("url_list.txt", "a+")
    url_file_contents = file_url.read()
    file_url.close();
    time.sleep(1)
    r = requests.get(p2)
    data = r.text
    parsed_page = BeautifulSoup(data, "html.parser")

    if urlcounter <= 999:
        if (p2 not in url_file_contents):
            file_url3 = open("url_list.txt", "a+")
            file_url3.write(p2 + "\n")
            file_url3.close()
            urlcounter = urlcounter + 1                 # Check if seed is not in the URLlist then add it and also make a raw data file for it
            file_rawdata = open("crawler_file_" + str(urlcounter) + ".txt", "a+")
            rawdata_to_string = str(parsed_page)
            file_rawdata.write(rawdata_to_string)
            file_rawdata.close()
            print p2


        for link in parsed_page.body.find_all('a',href=True):
            temp = str(link.get('href'))
            temp1 = temp.split('/')
            if '#' not in temp:
                if (len(temp1) > 1 and temp1[1] == "wiki" and ":" not in temp):
                    temp = "https://en.wikipedia.org" + temp
                    # print temp
                    temp2 = str(link.contents)
                    if ("solar" in temp.lower() or "solar" in temp2.lower()):
                        list3.append(temp)

        for p3 in list3:
            file_url = open("url_list.txt", "a+")
            url_file_contents = file_url.read()
            file_url.close();

            time.sleep(1)
            r = requests.get(p3)
            data = r.text
            parsed_page = BeautifulSoup(data, "html.parser")
            if urlcounter <= 999:
                if (p3 not in url_file_contents):
                    file_url3 = open("url_list.txt", "a+")
                    file_url3.write(p3 + "\n")
                    file_url3.close()
                    urlcounter = urlcounter + 1  # Check if seed is not in the URLlist then add it and also make a raw data file for it
                    file_rawdata = open("crawler_file_" + str(urlcounter) + ".txt", "a+")
                    rawdata_to_string = str(parsed_page)
                    file_rawdata.write(rawdata_to_string)
                    file_rawdata.close()
                    print p3


                for link in parsed_page.body.find_all('a', href=True):
                    temp = str(link.get('href'))
                    temp1 = temp.split('/')
                    if '#' not in temp:
                        if (len(temp1) > 1 and temp1[1] == "wiki" and ":" not in temp):
                            temp = "https://en.wikipedia.org" + temp
                            # print temp
                            temp2 = str(link.contents)
                            if ("solar" in temp.lower() or "solar" in temp2.lower()):
                                list4.append(temp)

                for p4 in list4:
                    file_url = open("url_list.txt", "a+")
                    url_file_contents = file_url.read()
                    file_url.close();

                    time.sleep(1)
                    r = requests.get(p4)
                    data = r.text
                    parsed_page = BeautifulSoup(data, "html.parser")
                    if urlcounter <= 999:
                        if (p4 not in url_file_contents):
                            file_url3 = open("url_list.txt", "a+")
                            file_url3.write(p4 + "\n")
                            file_url3.close()
                            urlcounter = urlcounter + 1  # Check if seed is not in the URLlist then add it and also make a raw data file for it
                            file_rawdata = open("crawler_file_" + str(urlcounter) + ".txt", "a+")
                            rawdata_to_string = str(parsed_page)
                            file_rawdata.write(rawdata_to_string)
                            file_rawdata.close()
                            print p4


                        for link in parsed_page.body.find_all('a', href=True):
                            temp = str(link.get('href'))
                            temp1 = temp.split('/')
                            if '#' not in temp:
                                if (len(temp1) > 1 and temp1[1] == "wiki" and ":" not in temp):
                                    temp = "https://en.wikipedia.org" + temp
                                    # print temp
                                    temp2 = str(link.contents)
                                    if ("solar" in temp.lower() or "solar" in temp2.lower()):
                                        list5.append(temp)

                        for p5 in list5:
                            file_url = open("url_list.txt", "a+")
                            url_file_contents = file_url.read()
                            file_url.close();

                            time.sleep(1)
                            r = requests.get(p5)
                            data = r.text
                            parsed_page = BeautifulSoup(data, "html.parser")
                            if urlcounter <= 999:
                                if (p5 not in url_file_contents):
                                    file_url3 = open("url_list.txt", "a+")
                                    file_url3.write(p5 + "\n")
                                    file_url3.close()
                                    urlcounter = urlcounter + 1  # Check if seed is not in the URLlist then add it and also make a raw data file for it
                                    file_rawdata = open("crawler_file_" + str(urlcounter) + ".txt", "a+")
                                    rawdata_to_string = str(parsed_page)
                                    file_rawdata.write(rawdata_to_string)
                                    file_rawdata.close()
                                    print p5
