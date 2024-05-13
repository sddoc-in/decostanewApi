from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import pandas as pd
options = Options()

options.add_argument("--disable-gpu")
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-software-rasterizer")
# Enable automation features to make the browser look more like a real user
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)


numScrolls = 3
query = "korting"
active_status = "active" # active or inactive
countary = "NL" # Country code
media_type = "all"
url = f"https://www.facebook.com/ads/library/?active_status={query}&ad_type=all&country={countary}&q={query}&search_type=keyword_unordered&media_type={media_type}"

driver.get(url)




import random
def randDealy(min, max):
    time.sleep(random.randint(min, max))



def get_like_follow(pageProfileUrl):
    original_window = driver.window_handles[0]
    driver.switch_to.new_window('tab')
    driver.get(pageProfileUrl)
    randDealy(3, 5)
    driver.find_element(By.XPATH, "//div[@aria-label='Close']//i[@data-visualcompletion='css-img']").click()
    likes_element = driver.find_element(By.XPATH ,"//a[contains(@href, 'friends_likes')]")
    likes = likes_element.text
    followers = driver.find_element(By.XPATH ,"//a[contains(@href, 'followers')]").text.replace("followers", "").strip()
    pageName  =  driver.find_element(By.XPATH, "*//span//h1").text.strip()
    driver.close()
    driver.switch_to.window(original_window)
    return likes, followers , pageName



def scrollpage():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




def extractData(numScrolls):
    for i in range(numScrolls):
        scrollpage()
        randDealy(3, 5)

    allads = driver.find_elements(By.XPATH, "//div[contains(text(), 'details')]")
    AddList = []
    for ad  in allads:
        try:
            ad.click()
        except:
            continue
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'versions')]")))
            driver.find_element(By.XPATH, "//body/div[@data-visualcompletion='ignore']/div/div[@data-visualcompletion='ignore']/div/div[@role='dialog']/div/div/div/div/span/div[1]").click()
            continue
        except:
            pass

        ad_details = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-visualcompletion='ignore']//div//div[@role='dialog']//div[@class='x3nfvp2 x1e56ztr']")))

        adArchiveID  = ad_details[0].text.split(":")[1].strip()
        adUrl = f"https://www.facebook.com/ads/library/?id={adArchiveID}"
        ad_status_type = ad_details[1].text
        try:
            duplicate = ad_details[4].text
        except:
            duplicate = None
        if "inactive" in ad_status_type.lower():
            date_range = ad_details[2].text
            start_date_str, end_date_str = date_range.split('-')
            start_date = datetime.strptime(start_date_str.strip(), "%d %b %Y")
            end_date = datetime.strptime(end_date_str.strip(), "%d %b %Y")
        else:
            start_date = ad_details[2].text
            start_date  = " ".join(start_date .split()[3:])  # Extract the date part from the string
            start_date  = datetime.strptime(start_date ,"%d %b %Y")  # Parse the date
            end_date = None

        if end_date is not None:
            numberOfActiveDay = (end_date - start_date).days
        else:
            numberOfActiveDay = (datetime.now() - start_date).days
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-visualcompletion='ignore']//div//div[@role='dialog']//div[contains(text(),'European Union transparency')]"))).click()

        
        totalreach = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='x8t9es0 x10d9sdx xo1l8bm xrohxju x108nfp6 xq9mrsl x1h4wwuj xeuugli'])[3]")))

        driver.execute_script("arguments[0].scrollIntoView();", totalreach)
        totalreach = totalreach.text
        aboutTheAdervetiser =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-visualcompletion='ignore']//div//div[@role='dialog']//div[contains(text(),'About the advertiser')]")))
        driver.execute_script("arguments[0].scrollIntoView();", aboutTheAdervetiser)
        aboutTheAdervetiser.click()

        pageProfileUrl = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"*//div[@data-visualcompletion='ignore']//div//div[@role='dialog']//div[contains(text(), 'ID')]" ))).text
        pageProfileUrl = "https://www.facebook.com/"+pageProfileUrl.split(":")[1].strip()
        currentpageLike, followers , pageName =  get_like_follow(pageProfileUrl)
        try:
            dscription =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-visualcompletion='ignore']//div//div[@role='dialog']//div[@class='_7jyg _7jyi']//div[@class='_7jyr']"))).text.strip()
        except:
            dscription = 'content blocked'

        CallToActionButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@data-visualcompletion='ignore']//div//div[@role='dialog']//div[@style='grid-area: adCardColumn;']//div[@aria-busy='false'])[2]")))
        productUrl = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-visualcompletion='ignore']//div//div[@role='dialog']//div[@style='grid-area: adCardColumn;']//div/a[@data-lynx-mode='hover']"))).get_attribute("href")
        adict = {'adArchiveID':adArchiveID,'page_name': pageName  , 'adUrl':adUrl, 'ad_status_type':ad_status_type, 'start_date':start_date, 'end_date':end_date, 'numberOfActiveDay':numberOfActiveDay, 'totalreach':totalreach, 'pageProfileUrl':pageProfileUrl,'product_url': productUrl , 'currentpageLike':currentpageLike, 'followers':followers, 'dscription':dscription, 'CallToActionButton':CallToActionButton.text, 'duplicate':duplicate}
        print(adict)
        AddList.append(adict)
        df = pd.DataFrame(AddList)
        df.to_excel("output.xlsx", index=False)
        driver.find_element(By.XPATH, "//body/div[@data-visualcompletion='ignore']/div/div[@data-visualcompletion='ignore']/div/div[@role='dialog']/div/div/div/div/span/div[1]").click()




extractData(numScrolls)
