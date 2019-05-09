import sys
import requests
import re
import datetime
from progress.bar import Bar

def __init__(self):
    self._playername = ""

def player_list(name):
    ''' name = string, "first name, space, last name"
    returns a list of properly formatted names to use in the URL,
    ex: Lebron James turns into jamesle01 '''
    urlname = name.split()
    first = urlname[0]
    last = urlname[1]
    return last[:5] + first[:2] + "01"

def get_data_page(formattedname,year):
    url = "http://www.basketball-reference.com/players/" + formattedname[0] + "/" + formattedname + "/shooting/20" + str(year).zfill(2) #find real url format when on internet
    #print("Loading data from: 20" + str(year).zfill(2))
    r = requests.get(url) #get page info
    if r.status_code != requests.codes.ok: # bad HTTP code
        return None
    pagetext = r.text # make readable, parse text
    return pagetext

def validate_data(shooting_data):
    REGEXcheck = "No shooting splits using these criteria"
    regexcheck = re.compile(REGEXcheck)
    regexchecker = re.findall(REGEXcheck, shooting_data)
    if regexchecker != []: #if player was not active during 2016
        #print("Player does not have shooting data")
        return False
    return True

def write_data(pagetext,fout):
    REGEXdata = '''<div style="top:([0-9]{1,3})px;left:([0-9]{1,3})px;"\stip="[a-zA-Z]{3}\s[0-9]{1,2},\s20[0-9]{2},\s[a-zA-Z\s]{10}<br>[0-9a-zA-Z\s]{7},\s[0-9:]{4,5}\sremaining<br>(Missed|Made)''' # get text of locations from website source code
    #print("i should be writing")
    REGEXdata = re.compile(REGEXdata)
    poslist = re.finditer(REGEXdata, pagetext)
    i = 0
    # isEmpty
    for positiondata in poslist:
        output = "{},{},{}\n".format(positiondata.group(1),positiondata.group(2),positiondata.group(3))
        fout.write(output)



def get_postions(formattedname):
    '''formattedname is a name like "jamesle01"s for the name inputted
    writes a file for the player titled the players name. each file has the positional
    and all other data in it'''

    with open(formattedname, "w") as fout: #writes a file with the name of the player in arg for with all the data in it
        fout.write("from_top,left,missed_or_made\n")
        curryear = datetime.datetime.now().year % 100 #gets last three digits of year
        bar = Bar('Loading Player Data', max=curryear)
        for i in range(curryear): #from 2000-2xxx
            pagetext = get_data_page(formattedname,i)
            bar.next()
            if validate_data(pagetext):
                #print("validated")
                write_data(pagetext,fout)
        bar.finish()
        print("Creating Shotmap...")
if __name__ == '__main__':
    get_postions(sys.argv[1])
