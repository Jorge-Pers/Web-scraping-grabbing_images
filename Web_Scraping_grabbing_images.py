print("****Download  images randomly with Web scraping and save it in the pc.****"'\n')

import requests
import bs4
import random

wolves_list = ["The Eurasian wolf","Caspian Sea Wolf","Tibetan Wolf","Tundra wolf"]
def func():
    #Script pick an option randomly.
    select_wolf = random.choice(wolves_list)
    #Find index for each option above.
    index = wolves_list.index(select_wolf)

    #Request.
    res = requests.get("https://sites.google.com/site/helprussianwolves/the-russian-wolves")
    #Apply BeautifulSoup
    soup = bs4.BeautifulSoup(res.text,"lxml")
    #Indexing in the Source HTML page.
    wolves = (soup.select("img")[index]) 
    image_wolf = wolves["src"]
    link_img = requests.get(image_wolf)
    link_img.content
    #Downloading image with wolf'name.
    f= open(f"C://Users/lorel/Desktop/{select_wolf}.jpg","wb")
    f.write(link_img.content)
    f.close()

    #Informing and confirming that the process is done.
    print('\t'f" The image of the {wolves_list[index]} has been download.")

func()




 
    



    
    
 




       
   

    
    
    




