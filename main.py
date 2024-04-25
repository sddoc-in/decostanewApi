from datetime import datetime
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse  
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import aiohttp , asyncio, json

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
    session_id = '38eb3c9c-f592-41e7-9f91-b7e4f0c517d7'
    cookies = {
    'sb': 'jMUbZpAnpJIEGIzQ7YKsNeWh',
    'datr': 'jMUbZmw50f4H67U3Cb9MZmfu',
    'ps_n': '1',
    'ps_l': '1',
    'wd': '1470x395',
    'c_user': '100077032827932',
    'xs': '11%3AnqfspYpAOHydgQ%3A2%3A1714038568%3A-1%3A-1',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1714038574235%2C%22v%22%3A1%7D',
    'fr': '1yYlDJpk07nObb0qb.AWVtOX-_JzTwYc5uIFgE28Z1iuc.BmJ-Eb..AAA.0.0.BmKicy.AWWyvoeSBDY',
    }


    headers = {
     'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=jMUbZpAnpJIEGIzQ7YKsNeWh; datr=jMUbZmw50f4H67U3Cb9MZmfu; ps_n=1; ps_l=1; wd=1470x395; c_user=100077032827932; xs=11%3AnqfspYpAOHydgQ%3A2%3A1714038568%3A-1%3A-1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1714038574235%2C%22v%22%3A1%7D; fr=1yYlDJpk07nObb0qb.AWVtOX-_JzTwYc5uIFgE28Z1iuc.BmJ-Eb..AAA.0.0.BmKicy.AWWyvoeSBDY',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=tshirts&search_type=keyword_unordered&media_type=all',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.62", "Google Chrome";v="124.0.6367.62", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.4.1"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': '4Fq7YzQzXxljRd2CEkUuqu',
    }

    data = {
     '__aaid': '0',
    '__user': '100077032827932',
    '__a': '1',
    '__req': '2',
    '__hs': '19838.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1013042036',
    '__s': 'faojz9:6l25xm:b7dkbl',
    '__hsi': '7361739638691407599',
    '__dyn': '7xe6Eiw_K9zo5ObwKBAgc9o2exu13wqojyUW3qi4EoxW4E7SewXwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBw5Zx62G3i1ywdl0Fw4Hwp8kwyx2cwAxq1yK1LwPxe3C0D8sKUbobEaUiyE725U4q0N8G0iS2S3qazo11E2XU6-1FwLw8O1pwr86C0gi1QwtU',
    '__csr': '',
    'fb_dtsg': 'NAcOJk_QRDynn0smo4qWif7qtMpFTJxZmU1nPk9Ryp9inQ7Q-M_w-2g:11:1714038568',
    'jazoest': '25594',
    'lsd': '4Fq7YzQzXxljRd2CEkUuqu',
    '__spin_r': '1013042036',
    '__spin_b': 'trunk',
    '__spin_t': '1714038578',
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
        return json.loads(response[9:])  
    else:
        
        cookies = {
         'sb': 'jMUbZpAnpJIEGIzQ7YKsNeWh',
    'datr': 'jMUbZmw50f4H67U3Cb9MZmfu',
    'ps_n': '1',
    'ps_l': '1',
    'wd': '1470x395',
    'c_user': '100077032827932',
    'xs': '11%3AnqfspYpAOHydgQ%3A2%3A1714038568%3A-1%3A-1',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1714038574235%2C%22v%22%3A1%7D',
    'fr': '1yYlDJpk07nObb0qb.AWVtOX-_JzTwYc5uIFgE28Z1iuc.BmJ-Eb..AAA.0.0.BmKicy.AWWyvoeSBDY',
        }

        data = {
        '__aaid': '0',
    '__user': '100077032827932',
    '__a': '1',
    '__req': '17',
    '__hs': '19838.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1013042036',
    '__s': '8ui8w2:6l25xm:b7dkbl',
    '__hsi': '7361739638691407599',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u',
    '__csr': '',
    'fb_dtsg': 'NAcOJk_QRDynn0smo4qWif7qtMpFTJxZmU1nPk9Ryp9inQ7Q-M_w-2g:11:1714038568',
    'jazoest': '25594',
    'lsd': '4Fq7YzQzXxljRd2CEkUuqu',
    '__spin_r': '1013042036',
    '__spin_b': 'trunk',
    '__spin_t': '1714038578',
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
    'c_user': '100077032827932',
    'xs': '48%3Ao1TL66iCBAHlOA%3A2%3A1713551109%3A-1%3A-1%3A%3AAcV4_cdPkPeY0JsHZkEGbdPy3LPNocPK_Acr6Mj8xg',
    'fr': '1yYlDJpk07nObb0qb.AWXlc3NpkO3qnY-fNjMeqmmHvVY.BmJ-Eb..AAA.0.0.BmJ-Eb.AWW95qqGG1c',
    'wd': '1470x395',
    }

    headers = {
     'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=jMUbZpAnpJIEGIzQ7YKsNeWh; datr=jMUbZmw50f4H67U3Cb9MZmfu; ps_n=1; ps_l=1; wd=1470x395; c_user=100077032827932; xs=11%3AnqfspYpAOHydgQ%3A2%3A1714038568%3A-1%3A-1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1714038574235%2C%22v%22%3A1%7D; fr=1yYlDJpk07nObb0qb.AWVtOX-_JzTwYc5uIFgE28Z1iuc.BmJ-Eb..AAA.0.0.BmKicy.AWWyvoeSBDY',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=tshirts&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.62", "Google Chrome";v="124.0.6367.62", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.4.1"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'AdLibraryAdDetailsV2Query',
    'x-fb-lsd': '4Fq7YzQzXxljRd2CEkUuqu',
    }
    
    variables = {
        "adArchiveID": adArchiveID,
        "pageID": pageID,
        "country": countary,
        "sessionID": "38eb3c9c-f592-41e7-9f91-b7e4f0c517d7",
        "source": None,
        "isAdNonPolitical": True,
        "isAdNotAAAEligible": False,
    }

    # Convert variables to JSON string
    variables_json = json.dumps(variables)
    data = {
       'av': '100077032827932',
    '__aaid': '0',
    '__user': '100077032827932',
    '__a': '1',
    '__req': '1p',
    '__hs': '19838.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1013042036',
    '__s': 'edy7ls:6l25xm:b7dkbl',
    '__hsi': '7361739638691407599',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u',
    '__csr': '',
    'fb_dtsg': 'NAcOJk_QRDynn0smo4qWif7qtMpFTJxZmU1nPk9Ryp9inQ7Q-M_w-2g:11:1714038568',
    'jazoest': '25594',
    'lsd': '4Fq7YzQzXxljRd2CEkUuqu',
    '__spin_r': '1013042036',
    '__spin_b': 'trunk',
    '__spin_t': '1714038578',
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



@app.get("/ads", response_class=JSONResponse)
async def read_item(country:str = Query(...), page: int = Query(..., description="Minimum page number"), querry: str = Query(..., description="Querry"), filtterStart_date: datetime = Query(None), filtterEnd_date: datetime = Query(None), Nextforward_cursor: str = Query(None), Nextbackward_cursor: str = Query(None), Nextcollation_token: str = Query(None) , ad_status_type: str = Query(...), ad_type: str = Query(...), media_type: str = Query(...), content_languages: str = Query(None), publisher_platforms: str = Query(None)):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        data = await getPageAds(session,page, country , querry, filtterStart_date,  filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages , publisher_platforms)
        return data
    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)
