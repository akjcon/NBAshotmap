import PIL
from PIL import ImageColor, Image, ImageDraw, ImageFont
import pandas as pd
import sys
from colorsys import rgb_to_hls, hls_to_rgb
import urllib.request

## BUG: grabimage needs a permanent fix for player image URL date

class Boxes:
    """The class boxes creates a different box object at each spot on the basketball court."""

    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.shotlist = []

    def missedshots(self):
        """returns a fraction of shots missed over shots taken"""
        return ((self.shotlist.count('Missed')) / len(self.shotlist))

    def totalshotsinbox(self):
        """returns the total amount of shots taken"""
        return (len(self.shotlist))


    def madeshots(self):
        """returns a fraction of shots made over shots taken"""
        return ((self.shotlist.count('Made')) / len(self.shotlist))

    def rgbnum(self):
        """Customizes color for each individual box"""
        return (int(255*madeshots()), 255, 255)



def grabimage(formattedname):
    """Grabs the players image off of Basketball-Reference"""
    urllib.request.urlretrieve("https://d2cwpp38twqe55.cloudfront.net/req/201902151/images/players/" + formattedname.lower() + ".jpg", "playerpic.png")
    
def addshots(filename,maptype):
    """Creates square box objects every 20 pixels, colors, and maps them onto the court."""
    im = Image.open('nbahalfcourt.png') #base half court map
    boxlist = []
    x1 = 0
    y1 = 0
    x2 = 20
    y2 = 20
    for i in range(0,500,20):
        for i in range(0,500,20):
            boxlist.append(Boxes(x1, x2, y1, y2))
            x1 += 0
            y1 += 20
            x2 += 0
            y2 += 20
        x1 += 20
        y1 = 0
        x2 += 20
        y2 = 20
    df = pd.read_csv(filename) #using pandas to iterate through coords
    ycoords = list(df.from_top)
    xcoords = list(df.left)
    shot = list(df.missed_or_made)
    zipped = zip(xcoords,ycoords,shot)
    for a,b,c in zipped:
        for box in boxlist:
            if a in range(box.xmin, box.xmax) and b in range(box.ymin, box.ymax):
                box.shotlist.append(c)
    drawsquares = ImageDraw.Draw(im)
    for box in boxlist:
        if len(box.shotlist) != 0:
            hue = int(2*((box.madeshots()) * 255))
            hue2 = int(2*(box.missedshots()) * 255)
            totalshots = 0
            with open(filename) as f:
                totalshots = sum(1 for _ in f)
            hue3 = int(255*(box.totalshotsinbox()/totalshots)*150)
            if maptype == "heat":
                rgbnum =(hue3,22,140)
            elif maptype == "shot":
                rgbnum = (hue2,hue,0)
            drawsquares.rectangle([(box.xmin,box.ymin),(box.xmax,box.ymax)], fill=(rgbnum),outline = None)
        else:
            drawsquares.rectangle([(box.xmin,box.ymin),(box.xmax,box.ymax)], fill=(255,255,255),outline = None)
    im2 = Image.open('nbahalfcourt.png')
    im.paste(im2, (0,0), im2)
    return im

def make_poster(filename,playername):
    """Takes the two maps created and formats them along with the keys, player image, and text into one final image."""
    background = Image.new("RGBA", (1000,800),(255,255,255))
    grabimage(filename)
    arialname = ImageFont.truetype('Arial.ttf', 40)
    arialkey = ImageFont.truetype('Arial.ttf', 20)
    playerpicmask = Image.open('playerpic.png').convert('RGBA')
    playerpic = Image.open('playerpic.png')
    background.paste((addshots(filename,"heat")), (0,327), (addshots(filename,"heat")))
    background.paste((addshots(filename,"shot")), (500,327), (addshots(filename,"shot")))
    background.paste(playerpic,(440,142), playerpicmask)
    draw = ImageDraw.Draw(background)
    draw.text((400,85),playername,fill = "black", font = arialname)
    draw.text((82,230),"Infrequent <------> Frequent",fill = "black", font = arialkey)
    x1 = 75
    y1 = 260
    x2 = 80
    y2 = 290
    r = 0
    for i in range(51):
        draw.rectangle([(x1,y1),(x2,y2)], fill = (r,22,140), outline = None)
        x1 += 5
        x2 += 5
        r += 5
    draw.text((670,230),"Made <------------> Missed",fill = "black", font = arialkey)
    x1 = 668
    y1 = 260
    x2 = 673
    y2 = 290
    r = 0
    g = 255
    for i in range(51):
        draw.rectangle([(x1,y1),(x2,y2)], fill = (r,g,0), outline = None)
        x1 += 5
        x2 += 5
        r += 5
        g -= 5
    background.show()




if __name__ == '__main__':
    grabimage(sys.argv[1])
