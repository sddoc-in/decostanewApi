from datetime import datetime
from fastapi import FastAPI, Query, BackgroundTasks
from fastapi.responses import HTMLResponse  
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import aiohttp , asyncio, json
import time, logging
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_db():
    # uri = "mongodb+srv://deepak:facebook1ads@cluster0.y7i2s57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    uri ="mongodb+srv://ituser:WqBoDSrSTOw9JSbd@facebook-ads.c6ddcxb.mongodb.net/?retryWrites=true&w=majority&appName=Facebook-Ads"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)

    # Send a ping to confirm a successful connection
    try:
        # client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        return None




app = FastAPI()

origins = [
    "https://facebookads.vercel.app",
    "https://facebookads.vercel.app/",
    "https://ui.sddoc.in",
    "https://ui.sddoc.in/",
    "http://localhost:3000",
    "http://localhost:3000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def fetch(session, url, headers=None, cookies=None, data=None):
    async with session.post(url, headers=headers, cookies= cookies, data = data) as response:
        return await response.text()


async def searchAds(session, page, countary,querry, forward_cursor, backward_cursor, collation_token, start_date , end_date, ad_status_type, ad_type, media_type, content_languages , publisher_platforms, totalFlag) :
    session_id = 'f720b74f-9414-4fcf-a0cb-331eef7de9f5'
    cookies = {
   'sb': 'jMUbZpAnpJIEGIzQ7YKsNeWh',
    'datr': 'jMUbZmw50f4H67U3Cb9MZmfu',
    'ps_n': '1',
    'ps_l': '1',
    'c_user': '100068654010842',
    'xs': '20%3A2lTBjwCwdUu7_Q%3A2%3A1717689763%3A-1%3A7608',
    'fr': '1Iqp1df39eZXdBwas.AWU7FoBHAFdTpiCYYtZpYXBbTHA.BmXvJs..AAA.0.0.BmYd2l.AWU17v7Zftc',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1717689769463%2C%22v%22%3A1%7D',
    'wd': '1470x196',
    }


    headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,fr;q=0.6,gu;q=0.5,de;q=0.4',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=jMUbZpAnpJIEGIzQ7YKsNeWh; datr=jMUbZmw50f4H67U3Cb9MZmfu; ps_n=1; ps_l=1; c_user=100068654010842; xs=20%3A2lTBjwCwdUu7_Q%3A2%3A1717689763%3A-1%3A7608; fr=1Iqp1df39eZXdBwas.AWU7FoBHAFdTpiCYYtZpYXBbTHA.BmXvJs..AAA.0.0.BmYd2l.AWU17v7Zftc; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1717689769463%2C%22v%22%3A1%7D; wd=1470x196',
    'dnt': '1',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=korting&search_type=keyword_unordered&media_type=all',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="125.0.6422.142", "Chromium";v="125.0.6422.142", "Not.A/Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.5.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'RdO5-cnrr9p-uAa6P8AEUR',
    }

    data = {
  '__aaid': '0',
    '__user': '100068654010842',
    '__a': '1',
    '__req': '2',
    '__hs': '19880.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1014024046',
    '__s': 'f7zikj:j0rf5e:oy7gms',
    '__hsi': '7377450112573883033',
    '__dyn': '7xe6Eiw_K9zo5ObwKBAgc9o2exu13wqojyUW3qi4EoxW4E7SewXwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBw5Zx62G3i1ywdl0Fw4Hwp8kwyx2cwAxq1yK1LwPxe3C0D8sKUbobEaUiyE725U4q0N8G0iS2S3qazo11E2XU6-1FAwGw8O1pwr86C0nC1TwmU',
    '__csr': '',
    'fb_dtsg': 'NAcPpa79etSA9J1fEgnFC-oNjwHWbk879WCIqB3tCArphfpS-USQeAw:20:1717689763',
    'jazoest': '25360',
    'lsd': 'RdO5-cnrr9p-uAa6P8AEUR',
    '__spin_r': '1014024046',
    '__spin_b': 'trunk',
    '__spin_t': '1717696458',
    '__jssesw': '1',
    }

    
    if page == 1:
        url =''

        if totalFlag:
            url = rf'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id={session_id}&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&publisher_platforms[0]={publisher_platforms}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&search_type=keyword_unordered'

        else:

            url =    f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id={session_id}&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'


        
        

        response = await fetch(session,  url, headers=headers, cookies=cookies, data=data)
        # response = requests.post(
        #     cookies=cookies,
        #     headers=headers,
        #     data=data,
        # )
        #  (response)
        return json.loads(response[9:])  
    else:
        
        cookies = {
       'sb': 'jMUbZpAnpJIEGIzQ7YKsNeWh',
    'datr': 'jMUbZmw50f4H67U3Cb9MZmfu',
    'ps_n': '1',
    'ps_l': '1',
    'c_user': '100068654010842',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1717689769463%2C%22v%22%3A1%7D',
    'xs': '20%3A2lTBjwCwdUu7_Q%3A2%3A1717689763%3A-1%3A7608%3A%3AAcXcTFUn63gJQ5kJTkJ-Fa8zP9K8BwMJ18xC1bCV0w',
    'fr': '1HDQU7KfGYMggY0zZ.AWWY_W-Ktk9mxPK6cxh0UxgsDcw.BmYffM..AAA.0.0.BmYffM.AWVWHxvNrJs',
    'wd': '1470x392',
            }

        data = {
      '__aaid': '0',
    '__user': '100068654010842',
    '__a': '1',
    '__req': 't',
    '__hs': '19880.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1014024046',
    '__s': 't6did2:j0rf5e:oy7gms',
    '__hsi': '7377450112573883033',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81bo4a4oaEd86a0HU9k2C2218waG5E6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4qxa7o-3qazo8U3ywbLwrU6Ci2G0z85C1Iwqo1uo7u2-2K',
    '__csr': '',
    'fb_dtsg': 'NAcPpa79etSA9J1fEgnFC-oNjwHWbk879WCIqB3tCArphfpS-USQeAw:20:1717689763',
    'jazoest': '25360',
    'lsd': 'RdO5-cnrr9p-uAa6P8AEUR',
    '__spin_r': '1014024046',
    '__spin_b': 'trunk',
    '__spin_t': '1717696458',
    '__jssesw': '1',
            }

        url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&{backward_cursor}=&session_id={session_id}&collation_token={collation_token}&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'
        # url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&verify=21543e81&forward_cursor={forward_cursor}&backward_cursor={backward_cursor}&session_id={session_id}&collation_token={collation_token}&count=30&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered'
        
        
        response = await fetch(session, url, headers=headers,cookies=cookies, data=data)

        # response = requests.post(url, cookies=cookies, headers=headers, data=data)
        return json.loads(response[9:])  


async def epoch_to_timestamp(epoch_time):
    try:
        timestamp = datetime.fromtimestamp(epoch_time)
        # return timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return timestamp.strptime(timestamp.strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return f"Error: {e}"

async def viewad(session, adArchiveID, pageID, countary):
    cookies = {
    'sb': 'jMUbZpAnpJIEGIzQ7YKsNeWh',
    'datr': 'jMUbZmw50f4H67U3Cb9MZmfu',
    'ps_n': '1',
    'ps_l': '1',
    'c_user': '100068654010842',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1717689769463%2C%22v%22%3A1%7D',
    'xs': '20%3A2lTBjwCwdUu7_Q%3A2%3A1717689763%3A-1%3A7608%3A%3AAcXcTFUn63gJQ5kJTkJ-Fa8zP9K8BwMJ18xC1bCV0w',
    'fr': '1HDQU7KfGYMggY0zZ.AWWY_W-Ktk9mxPK6cxh0UxgsDcw.BmYffM..AAA.0.0.BmYffM.AWVWHxvNrJs',
    'wd': '1470x392',
    }

    headers = {
   'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,fr;q=0.6,gu;q=0.5,de;q=0.4',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=jMUbZpAnpJIEGIzQ7YKsNeWh; datr=jMUbZmw50f4H67U3Cb9MZmfu; ps_n=1; ps_l=1; c_user=100068654010842; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1717689769463%2C%22v%22%3A1%7D; xs=20%3A2lTBjwCwdUu7_Q%3A2%3A1717689763%3A-1%3A7608%3A%3AAcXcTFUn63gJQ5kJTkJ-Fa8zP9K8BwMJ18xC1bCV0w; fr=1HDQU7KfGYMggY0zZ.AWWY_W-Ktk9mxPK6cxh0UxgsDcw.BmYffM..AAA.0.0.BmYffM.AWVWHxvNrJs; wd=1470x392',
    'dnt': '1',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=korting&search_type=keyword_unordered&media_type=all',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="125.0.6422.142", "Chromium";v="125.0.6422.142", "Not.A/Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.5.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'AdLibraryAdDetailsV2Query',
    'x-fb-lsd': 'RdO5-cnrr9p-uAa6P8AEUR',
    }
    
    variables = {
        "adArchiveID": adArchiveID,
        "pageID": pageID,
        "country": countary,
        "sessionID": "f720b74f-9414-4fcf-a0cb-331eef7de9f5",
        "source": None,
        "isAdNonPolitical": True,
        "isAdNotAAAEligible": False,
    }

    # Convert variables to JSON string
    variables_json = json.dumps(variables)
    data = {
    'av': '100068654010842',
    '__aaid': '0',
    '__user': '100068654010842',
    '__a': '1',
    '__req': '1i',
    '__hs': '19880.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1014024046',
    '__s': 'v0679i:j0rf5e:oy7gms',
    '__hsi': '7377450112573883033',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81bo4a4oaEd86a0HU9k2C2218waG5E6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4qxa7o-3qazo8U3ywbLwrU6Ci2G0z85C1Iwqo1uo7u2-2K',
    '__csr': '',
    'fb_dtsg': 'NAcPpa79etSA9J1fEgnFC-oNjwHWbk879WCIqB3tCArphfpS-USQeAw:20:1717689763',
    'jazoest': '25360',
    'lsd': 'RdO5-cnrr9p-uAa6P8AEUR',
    '__spin_r': '1014024046',
    '__spin_b': 'trunk',
    '__spin_t': '1717696458',
    '__jssesw': '1',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'AdLibraryAdDetailsV2Query',
        'variables':variables_json, 
        'server_timestamps': 'true',
        'doc_id': '6635716889819821',
        
    }
    response = await fetch(session, 'https://www.facebook.com/api/graphql/', headers=headers, cookies=cookies, data=data)
    # response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
    # print(">>>>>>>>>>>>>>>", response)
    
    return json.loads(response)




async def getPageAds(session, page, countary,querry,filtterStart_date, filtterEnd_date,Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages , publisher_platforms , totalFlag):
    try:
        data = await searchAds(session, page,countary ,querry, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, filtterEnd_date, filtterEnd_date, ad_status_type, ad_type, media_type, content_languages , publisher_platforms, totalFlag)
        
    except Exception as e:
        return {"error": f"Error: {e}"}
    forward_cursor = data['payload']['forwardCursor']
    backward_cursor = data['payload']['backwardCursor']
    collation_token = data['payload']['collationToken']
    totalAdcount = data['payload']['totalCount']
    pageData = {"forward_cursor": forward_cursor, "backward_cursor": backward_cursor, "collation_token": collation_token, "totalAdcount": totalAdcount}
    Adresult = []
    for ads in data['payload']['results']:
        # print(ad)
        for ad in ads:
            adArchiveID = ad["adArchiveID"]
            pageID = ad["pageID"]
            start_date = ad["startDate"]
            end_date = ad["endDate"]
            numberOfActiveDay = (end_date - start_date)//86400
            start_date = await epoch_to_timestamp(start_date)
            end_date = await epoch_to_timestamp(end_date)
        
            if filtterStart_date <= start_date <= filtterEnd_date or filtterStart_date <= end_date <= filtterEnd_date:
                tempActive = False
                # print(ad["isActive"])
                if ad_status_type == 'active' and ad["isActive"] == True:
                    tempActive = True
                elif ad_status_type == 'inactive' and ad["isActive"] == False:
                    tempActive = True
                elif ad_status_type == 'all':
                    tempActive = True
                if tempActive == False:
                    continue
                if tempActive:
                    isActive = ad["isActive"]
                    pageName = ad["pageName"]
                    # currentpageLike = 0
                    try:
                        currentpageLike = ad["snapshot"]["page_like_count"]
                    except:
                        currentpageLike = 0
                        # currentpageLike = 0
                    try:
                        pageProfileUrl = ad["snapshot"]["page_profile_uri"]
                    except:
                        pageProfileUrl = ""
                    try:
                        adcreativeId = ad["snapshot"]["ad_creative_id"]
                    except:
                        adcreativeId = ""
                    try:
                        CallToActionButton = ad["snapshot"]["cta_text"]
                    except:
                        CallToActionButton = ""
                    try:
                        linkUrl = ad["snapshot"]["link_url"]
                    except:
                        linkUrl = ""
                    try:
                        description = ad["snapshot"]["body"]['markup']['__html']
                    except:
                        description = ""
                    adUrl = f"https://www.facebook.com/ads/library/?id={adArchiveID}"
                    try:
                        adsdata =await viewad(session, adArchiveID, pageID, countary)
                    except Exception as e:
                        adsdata = {"error": f"Error"}
                    # print(adsdata['data']['ad_library_main']['ad_details']['aaa_info'])
                    try:
                        totalreach = adsdata['data']['ad_library_main']['ad_details']['aaa_info']['eu_total_reach']
                    except:
                        totalreach = 0
                    dataDict ={"pageName": pageName, "currentpageLike": currentpageLike, "pageProfileUrl": pageProfileUrl, 'description' : description ,"adcreativeId": adcreativeId,'adArchiveID' : adArchiveID , 'pageId': pageID, "CallToActionButton": CallToActionButton, "linkUrl": linkUrl, "adUrl": adUrl, "isActive": isActive,'TotalReach': totalreach ,"start_date": start_date, "end_date": end_date, "numberOfActiveDay": numberOfActiveDay}
                    Adresult.append(dataDict)
  
    return {'results': Adresult, 'pageData': pageData}



# @app.get("/ads", response_class=JSONResponse)
# async def read_item(country:str = Query(...), page: int = Query(..., description="Minimum page number"), querry: str = Query(..., description="Querry"), filtterStart_date: datetime = Query(None), filtterEnd_date: datetime = Query(None), Nextforward_cursor: str = Query(None), Nextbackward_cursor: str = Query(None), Nextcollation_token: str = Query(None) , ad_status_type: str = Query(...), ad_type: str = Query(...), media_type: str = Query(...), content_languages: str = Query(None), publisher_platforms: str = Query(None)):
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
#         data = await getPageAds(session,page, country , querry, filtterStart_date,  filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages , publisher_platforms)
#         return data
    
async def read_item(country, page , querry, filtterStart_date, filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages, publisher_platforms, totalFlag):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        data = await getPageAds(session,page, country , querry, filtterStart_date,  filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages , publisher_platforms, totalFlag)
        return data
    
async def GetTotalRow(data):
    print(data)
    countary = data['country']
    querry = data['querry']
    filtterStart_date = data['filtterStart_date']
    filtterEnd_date = data['filtterEnd_date']
    Nextforward_cursor = data['Nextforward_cursor']
    Nextbackward_cursor = data['Nextbackward_cursor']
    Nextcollation_token = data['Nextcollation_token']
    ad_status_type = data['ad_status_type']
    if ad_status_type == 0:
        ad_status_type = 'all'
    elif ad_status_type == 1:
        ad_status_type = 'active'
    elif ad_status_type == 2:
        ad_status_type = 'inactive'
    ad_type = data['ad_type']
    media_type = data['media_type']
    content_languages = data['content_languages']
    publisher_platforms = data['publisher_platforms']
    page = data['page']
    data =  await read_item(countary, page, querry, filtterStart_date, filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages, publisher_platforms,True)
    row = data['pageData']['totalAdcount']
    return row

async def SaveDataToDB(data, row, SearchID ):
   
    countary = data['country']
    querry = data['querry']
    filtterStart_date = data['filtterStart_date']
    filtterEnd_date = data['filtterEnd_date']
    Nextforward_cursor = data['Nextforward_cursor']
    Nextbackward_cursor = data['Nextbackward_cursor']
    Nextcollation_token = data['Nextcollation_token']
    ad_status_type = data['ad_status_type']
    if ad_status_type == 0:
        ad_status_type = 'all'
    elif ad_status_type == 1:
        ad_status_type = 'active'
    elif ad_status_type == 2:
        ad_status_type = 'inactive'
    ad_type = data['ad_type']
    media_type = data['media_type']
    content_languages = data['content_languages']
    publisher_platforms = data['publisher_platforms']
    page = data['page']
    # print(row)
    for i in range(1, row):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            
            data = await read_item(countary, i, querry, filtterStart_date, filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages, publisher_platforms, False)
            Nextbackward_cursor = data['pageData']['backward_cursor']
            Nextforward_cursor = data['pageData']['forward_cursor']
            Nextcollation_token = data['pageData']['collation_token']
            for result in data['results']:
                client = connect_db()
                collection = client['Master']['results']
                searchCollection = client['Master']['search']
                searchCollection.update_one({"searchId": SearchID}, {"$inc": {"status": 1}})
                result['SearchUid'] = SearchID
                result['created_at'] = int(time.time())
                collection.insert_one(result)
                # print(result)
                client.close()
            
            

@app.get("/total", response_class=JSONResponse)
async def resultRecord(SearchID : str = Query(None)):
    if SearchID:
        client = connect_db()
        db = client['Master']
        collection = db['search']
        data = collection.find_one({"searchId": SearchID})
        client.close()
        try:
            row = await GetTotalRow(data)
        except Exception as e:
            return {"error": f"Error: {e}"}
        return {"total": row}
    else:
        return {"error": "SearchID is required"}

@app.get("/ads", response_class=JSONResponse)
async def getdata(background_tasks: BackgroundTasks, SearchID : str = Query(None)):
    if SearchID:
        client = connect_db()
        db = client['Master']
        collection = db['search']
        data = collection.find_one({"searchId": SearchID})
        row = await GetTotalRow(data)
        try:
            background_tasks.add_task(SaveDataToDB, data, row, SearchID)
            return {"status": "success"}
        except Exception as e:
            return {"error": f"Error: {e}"}
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
