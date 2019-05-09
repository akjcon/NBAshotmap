# Final Project Proposal
*Essentially we will be taking positional data of NBA player's basketball shots and creating a map of their shots, colored red or green gradient based on how often they make the shots *

## Data Plan
*Since positional data isn't available for the average person, only for the NBA, we will be scraping the data from a shotmap on basketball-reference.com. This will be in CSV format, and we will parse this for the information we need using regex expressions.*

## Implementation Plan
*We will be starting from scratch, and first using the requests library to build a function to scrape the data from basketball-reference.com for NBA players. With this data we receive positional data in the form of y = (distance from top)px and y = (distance from left)px. We will then store this data in files associated with the players' names. We will then build a clipart image (or use and attribute one) using matplotlib, and build a function to parse the data, and based on how close the points are, overlay the image with squares sized according to the amount of shots taken from that area. The squares will be colored a gradient based on how often the person misses or makes shots from that area. The end result will be a program that you can run from terminal and has one argument, the players name. When you run the program with the name, it should return you two shot maps (one of where the player shoots from the most and one of his misses and makes blended together) with his image and two keys for each map. *

### External Libraries
- requests
- re
- Pillow
- Pandas

### Milestones
- Getting the data from the website
- Creating the boxes
- Coloring the boxes according to the data
- Drawing the images
- Creating the keys and name and image of the player.


## Deliverables
- Deliverable 1 = One image that shows where the player shoots from the most
- Deliverable 2 = One image that shows where the player makes and misses shots from.
- Deliverable 3 = The players name, image and two color keys for each image on the original image.

# Final Project Report
* Why our project is interesting?
    Answer: By returning two graphs, the images are able to convey meaningful information about the players game, strengths, and weaknesses. For example one graph shows the where a player (e.g. Lebron James) shoots from the most. From there one can look at the second graph and decipher where the player shoots the highest percentage form. Someone using this code could extrapolate that a player is best from the left side of the court just inside the three point line, or driving to the rim from an angle from the right side of the court. He or she could also tell whether a player should more or less shots from a certain place given his conversion rate.

* What were the challenges?
    Answer: Creating the boxes on a saved image was very difficult. When we first tried to create boxes we would often get very strange lines. It was very difficult to write the code to draw each individual box. After we had drawn each individual box, we attempted to color it which turned out to be really difficult as well. You should have seen are first few results! Even after we had gotten the colors to blend we realized that they blacked out the basketball court which was another problem. The keys were hard given the weird blends of colors we received in our images.
    However, looking back the part of the code we spent the most time on was most definitely coloring the boxes.

* What were your findings?
    Answer: At first we tried to create the colors on the images using HSL but we couldn't really figure out a way to input a constantly changing variable into HSL parameters. We switched to RGB which with a little work turned out to be a lot easier. We also realized that once the data was extrapolated, we could do a lot with the graphs given our already written code. Our initial thought for the project was just to create one graph of where the player shoots from the most, but then we though it would be cool if our code somehow could be used to show where a player could improve.

* What questions still remain?
    Answer: We really wanted to use HSL but we couldn't figure out a way to do it. I think another big question of ours was how we could've approached the problem using matplotlib. Lastly, how could we incorporate freethrows into our data?

## Instructions to run the code
    Once the repository is cloned, you must install/have installed the following dependencies (you can 'pip install foo' to install these'):
    - Pillow
    - requests
    - pandas

    Then to create the visualization:

    python3 makeshotmap.py "First Last"


    with first being a players first name and last being their surname. It may take a while to grab the data, probably two or three minutes, but after that you're set!

---

# Final Project Grading

## Functionality: 10/10

The functionality is as advertised, except that the directions say to use ```python3 picturemaker.py "First Last"``` when it should have been ```python3 makeshotmap.py ...``` instead.

## Challenge and Endurance: 10/10

I know that you faced quite a few hurdles along the way---grabbing data, plotting it on the map, grabbing phots---but you endured and ended up with a great final project.

## Code Quality: 10/10

Your code organization, structure, and level of abstraction was top-notch.  There were a few places where I thought you might want to use somse string constants but otherwise it was clean.

## Final Product: 10/10

Just beautiful.  There's not much to write because everything was done so well.

Overall: 40/40
