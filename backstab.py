
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image

def grabImage(url, name, webElement = None):
    # Here Chrome  will be used

    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    # URL of website
    url = url 
    
    # Opening the website
    driver.get(url)

    #Find the map and get its size and location
    if(webElement != None):
        element = driver.find_element(By.ID, webElement)
        location = element.location
        size = element.size

        #Get the positional data so we can crop it
        x = location['x']
        y = location['y']
        width = location['x']+size['width']+200
        height = location['y']+size['height']+200
    driver.save_screenshot("image.png")
    # Loading the image and croping it
    image = Image.open("image.png")
    if(webElement != None):
        image = image.crop((int(x), int(y), int(width), int(height)))
    
    # Showing the image
    image.show()

    # Save the cropped png in a location for later
    image.save("C:/Users/alexz/Documents/AAA_PROXY/Programs/DisasterBot/Backstab/"+ str(name) +".png", "PNG")
    
    #return image

#grabImage("https://www.backstabbr.com/game/Disaster-Hole-Round-2/6313078592503808", 1, "map_container")