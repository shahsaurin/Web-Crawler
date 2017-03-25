
WEB CRAWLER


********** External Third party libraries used ***********************

1) BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/)
2) requests (http://docs.python-requests.org/en/master/user/install/#install)



**********  Setting up the current directory for file output*********

In every program file (.py) there is are 2 commented lines on top of the code. You may create and select the required directory at the required path so that the output files may be created at that location. The said commented lines in the code are like:
------------------------------------------------------------------
#os.mkdir("----Enter your path here------\Saurin_Shah\Task1")
#os.chdir("----Enter your path here------\Saurin_Shah\Task1")
------------------------------------------------------------------


***NOTE:- After running the programs, two types of files will be created (total of maximum 1001 files)

    1) 'url_list.txt' that contains unique links of at the most 1000 webpages that the crawler has crawled.
    2) 'crawler_file_<no>.txt' are the files containing the raw data of all the URLs (individually) mentioned in the 'url_list.txt' file          (maximum 1000 files).



************ Running the programs*******************

The programs may be run using either of these options:

1) Using a suitable Python editor (like PyCharm)
2) Using command prompt
3) Double clicking on the progam file (.py extension)
