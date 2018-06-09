import sys
import webscraper
import picturemaker

if __name__ == '__main__':
    name = sys.argv[1]
    formattedname = webscraper.player_list(name)
    webscraper.get_postions(formattedname.lower())
    picturemaker.make_poster(formattedname,name)
