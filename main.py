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
    uri = "mongodb+srv://deepak:facebook1ads@cluster0.y7i2s57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

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


async def searchAds(session, page, countary,querry, forward_cursor, backward_cursor, collation_token, start_date , end_date, ad_status_type, ad_type, media_type, content_languages , publisher_platforms) :
    session_id = '123df71d-9ea0-43c9-8a13-c1aeb993d423'
    cookies = {
    'datr': '2p5cZgs2z7aml8cYgBpHtO1T',
    'wd': '1470x378',
    }


    headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=2p5cZgs2z7aml8cYgBpHtO1T; wd=1470x378',
    'dnt': '1',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=korting&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'AVol2jqZlOk',
    }

    data = {
      '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'q',
    '__hs': '19876.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1013917984',
    '__s': 'x3199t:uz3tx9:68d0t9',
    '__hsi': '7375944949067236991',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u1rw',
    '__csr': '',
    'lsd': 'AVol2jqZlOk',
    'jazoest': '21023',
    '__spin_r': '1013917984',
    '__spin_b': 'trunk',
    '__spin_t': '1717346010',
    '__jssesw': '1',
    }

    
    if page == 1:
        url =    f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id={session_id}&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'
        
        # url = rf'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id={session_id}&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&publisher_platforms[0]={publisher_platforms}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&search_type=keyword_unordered'


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
        'datr': '2p5cZgs2z7aml8cYgBpHtO1T',
    'wd': '1470x378',
            }

        data = {
      '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': '1b',
    '__hs': '19876.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1013917984',
    '__s': '7xyosw:uz3tx9:68d0t9',
    '__hsi': '7375944949067236991',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u1rw',
    '__csr': '',
    'lsd': 'AVol2jqZlOk',
    'jazoest': '21023',
    '__spin_r': '1013917984',
    '__spin_b': 'trunk',
    '__spin_t': '1717346010',
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
  'datr': '2p5cZgs2z7aml8cYgBpHtO1T',
    'wd': '1470x378',
    }

    headers = {
   'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=2p5cZgs2z7aml8cYgBpHtO1T; wd=1470x378',
    'dnt': '1',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=korting&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'AdLibraryAdDetailsV2Query',
    'x-fb-lsd': 'AVol2jqZlOk',
    }
    
    variables = {
        "adArchiveID": adArchiveID,
        "pageID": pageID,
        "country": countary,
        "sessionID": "123df71d-9ea0-43c9-8a13-c1aeb993d423",
        "source": None,
        "isAdNonPolitical": True,
        "isAdNotAAAEligible": False,
    }

    # Convert variables to JSON string
    variables_json = json.dumps(variables)
    data = {
       'av': '0',
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': '23',
    '__hs': '19876.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1013917984',
    '__s': '7xyosw:uz3tx9:68d0t9',
    '__hsi': '7375944949067236991',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u1rw',
    '__csr': '',
    'lsd': 'AVol2jqZlOk',
    'jazoest': '21023',
    '__spin_r': '1013917984',
    '__spin_b': 'trunk',
    '__spin_t': '1717346010',
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




async def getPageAds(session, page, countary,querry,filtterStart_date, filtterEnd_date,Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages , publisher_platforms):
    try:
        data = await searchAds(session, page,countary ,querry, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, filtterEnd_date, filtterEnd_date, ad_status_type, ad_type, media_type, content_languages , publisher_platforms)
        
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
    
async def read_item(country, page , querry, filtterStart_date, filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages, publisher_platforms):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        data = await getPageAds(session,page, country , querry, filtterStart_date,  filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages , publisher_platforms)
        return data
    
async def GetTotalRow(data):
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
    data =  await read_item(countary, page, querry, filtterStart_date, filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages, publisher_platforms)
    row = data['pageData']['totalAdcount']
    return row

async def SaveDataToDB(data, SearchUid, row ):
   
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
    for i in range(1, row):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            
            data = await read_item(countary, i, querry, filtterStart_date, filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages, publisher_platforms)
            Nextbackward_cursor = data['pageData']['backward_cursor']
            Nextforward_cursor = data['pageData']['forward_cursor']
            Nextcollation_token = data['pageData']['collation_token']
            print(data)
            for result in data['results']:
                client = connect_db()
                collection = client['facebookads']['results']
                result['SearchUid'] = SearchUid
                result['created_at'] = int(time.time())
                collection.insert_one(result)
                client.close()
            
            

       

    

    



@app.get("/ads", response_class=JSONResponse)
async def getdata(background_tasks: BackgroundTasks, SearchID : str = Query(None)):
    if SearchID:
        client = connect_db()
        db = client['facebookads']
        collection = db['search']
        data = collection.find_one({"searchID": SearchID})
        SearchUid = str(data['_id'])
        row = await GetTotalRow(data)
        try:
            background_tasks.add_task(SaveDataToDB, data, SearchUid, row)
            return {"status": "success"}
        except Exception as e:
            return {"error": f"Error: {e}"}
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)
