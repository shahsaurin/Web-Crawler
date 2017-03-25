
from bs4 import BeautifulSoup
import urllib2
import requests
import time
import os

#os.mkdir("----Enter your path here------\Saurin_Shah\Task1")
#os.chdir("----Enter your path here------\Saurin_Shah\Task1")

queue = ["https://en.wikipedia.org/wiki/Sustainable_energy"]
i=0
urlcounter = 0
depth = [1]

while(1):
    time.sleep(1)
    r = requests.get(queue[i])
    data =  r.text
    parsed_page = BeautifulSoup(data, "html.parser")                       # getting page in HTML format

    file_url = open("url_list.txt", "a+")
    url_file_contents = file_url.read()
    file_url.close();
    #if (queue[i] not in url_file_contents) and urlcounter <= 999:
    if urlcounter <= 999:
        if(queue[i] not in url_file_contents):
            file_url3 = open("url_list.txt", "a+")
            file_url3.write(queue[i]+"\n")
            file_url3.close()
            #depth.append(i+1)
            urlcounter = urlcounter + 1                                              # Check if seed is not in the URLlist then add it and also make a raw data file for it
            file_rawdata = open("crawler_file_"+str(urlcounter)+".txt", "a+")
            rawdata_to_string = str(parsed_page)
            file_rawdata.write(rawdata_to_string)
            file_rawdata.close()

        for link in parsed_page.body.find_all('a',href=True):
            temp = str(link['href'].encode('utf-8'))
            temp1 = temp.split('/')
            if '#' not in temp :
                if (len(temp1)>1 and temp1[1] == "wiki" and ":" not in temp):
                    temp = "https://en.wikipedia.org" + temp
                    #print temp
                    temp2 = str(link.contents)
                    if ("solar" in temp.lower() or "solar" in temp2.lower()):
                        file_url2 = open("url_list.txt", "a+")
                        url_file_contents2 = file_url2.read()
                        file_url2.close()
                        if (temp not in url_file_contents2 and urlcounter<=999):
                            file_url4 = open("url_list.txt","a+")
                            file_url4.write(temp + "\n")
                            file_url4.close()
                            urlcounter = urlcounter + 1         # Check if seed is not in the URLlist then add it and also make a raw data file for it

                            print temp

                            time.sleep(1)
                            r2 = requests.get(temp)
                            data2 = r2.text
                            parsed_page2 = BeautifulSoup(data2, "html.parser")


                            file_rawdata2 = open("crawler_file_" + str(urlcounter) + ".txt", "w+")
                            rawdata_to_string = str(parsed_page2)
                            file_rawdata2.write(rawdata_to_string)
                            file_rawdata2.close()
                            queue.append(temp)
                            depth.append (depth[i]+1)


        i = i+1

    else:                                                   #  Added later on. delete if reqd
        if urlcounter > 999:                                 #  Added later on. delete if reqd
            break                                           #  Added later on. delete if reqd
        else:                                               #  Added later on. delete if reqd
            print queue
            i = i + 1
            print i                                         #  Added later on. delete if reqd
            print "in ELse part"
            continue                                        #  Added later on. delete if reqd