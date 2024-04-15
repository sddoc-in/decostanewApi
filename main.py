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
    session_id = 'fe0143d7-8a38-40a2-b4bc-d513a6c540de'
    cookies = {
    'sb': 'jMUbZpAnpJIEGIzQ7YKsNeWh',
    'datr': 'jMUbZmw50f4H67U3Cb9MZmfu',
    'dpr': '2',
    'ps_l': '0',
    'ps_n': '0',
    'locale': 'en_GB',
    'wd': '1470x387',
    'c_user': '100077032827932',
    'xs': '26%3ACyoK_IgNyDRvqg%3A2%3A1713209445%3A-1%3A-1',
    'fr': '1E2UekTIuoNouDwBd.AWUpcX8O57zlwp43Dtmj6hS-NOM.BmHNKv..AAA.0.0.BmHYBn.AWUTOqLvnnM',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1713209450220%2C%22v%22%3A1%7D',
    }

    headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=jMUbZpAnpJIEGIzQ7YKsNeWh; datr=jMUbZmw50f4H67U3Cb9MZmfu; dpr=2; ps_l=0; ps_n=0; locale=en_GB; wd=1470x387; c_user=100077032827932; xs=26%3ACyoK_IgNyDRvqg%3A2%3A1713209445%3A-1%3A-1; fr=1E2UekTIuoNouDwBd.AWUpcX8O57zlwp43Dtmj6hS-NOM.BmHNKv..AAA.0.0.BmHYBn.AWUTOqLvnnM; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1713209450220%2C%22v%22%3A1%7D',
    'dpr': '2',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=tshirt&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.123", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.4.1"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'viewport-width': '1470',
    'x-asbd-id': '129477',
    'x-fb-lsd': '6ZnT2OUWVKCpbXXc7CcgVF',
    }

    data = {
    '__aaid': '0',
    '__user': '100077032827932',
    '__a': '1',
    '__req': 'j',
    '__hs': '19828.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'GOOD',
    '__rev': '1012780108',
    '__s': 'zdx5l3:m4ootu:5gtcmj',
    '__hsi': '7358178637906972205',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u',
    '__csr': '',
    'fb_dtsg': 'NAcOYuiN87FtGB9I2T0quxj1LdTh5ZjeSNloubvEPl01hrtT0P0XHtw:26:1713209445',
    'jazoest': '25467',
    'lsd': '6ZnT2OUWVKCpbXXc7CcgVF',
    '__spin_r': '1012780108',
    '__spin_b': 'trunk',
    '__spin_t': '1713209468',
    '__jssesw': '1',
    }

    
    if page == 1:
        # url =    f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id=15b5fb0b-2d87-4f6c-93a9-d56031103033&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'

        url = rf'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id={session_id}&count=30&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&publisher_platforms[0]={publisher_platforms}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&search_type=keyword_unordered'


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
        'dpr': '2',
        'ps_l': '0',
        'ps_n': '0',
        'locale': 'en_GB',
        'wd': '1470x387',
        'c_user': '100077032827932',
        'xs': '26%3ACyoK_IgNyDRvqg%3A2%3A1713209445%3A-1%3A-1',
        'fr': '1E2UekTIuoNouDwBd.AWUpcX8O57zlwp43Dtmj6hS-NOM.BmHNKv..AAA.0.0.BmHYBn.AWUTOqLvnnM',
        'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1713209450220%2C%22v%22%3A1%7D',
        }

        data = {
        '__aaid': '0',
        '__user': '100077032827932',
        '__a': '1',
        '__req': '17',
        '__hs': '19828.BP:DEFAULT.2.0..0.0',
        'dpr': '2',
        '__ccg': 'GOOD',
        '__rev': '1012780108',
        '__s': '9fsnzp:m4ootu:5gtcmj',
        '__hsi': '7358178637906972205',
        '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u',
        '__csr': '',
        'fb_dtsg': 'NAcOYuiN87FtGB9I2T0quxj1LdTh5ZjeSNloubvEPl01hrtT0P0XHtw:26:1713209445',
        'jazoest': '25467',
        'lsd': '6ZnT2OUWVKCpbXXc7CcgVF',
        '__spin_r': '1012780108',
        '__spin_b': 'trunk',
        '__spin_t': '1713209468',
        '__jssesw': '1',
        }

        # url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&{backward_cursor}=&session_id={session_id}&collation_token={collation_token}&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'
        url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&backward_cursor={backward_cursor}&session_id={session_id}&collation_token={collation_token}&count=30&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered'
        
        
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
    'dpr': '2',
    'ps_l': '0',
    'ps_n': '0',
    'locale': 'en_GB',
    'wd': '1470x387',
    'c_user': '100077032827932',
    'xs': '26%3ACyoK_IgNyDRvqg%3A2%3A1713209445%3A-1%3A-1',
    'fr': '1E2UekTIuoNouDwBd.AWUpcX8O57zlwp43Dtmj6hS-NOM.BmHNKv..AAA.0.0.BmHYBn.AWUTOqLvnnM',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1713209450220%2C%22v%22%3A1%7D',
    }

    headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=jMUbZpAnpJIEGIzQ7YKsNeWh; datr=jMUbZmw50f4H67U3Cb9MZmfu; dpr=2; ps_l=0; ps_n=0; locale=en_GB; wd=1470x387; c_user=100077032827932; xs=26%3ACyoK_IgNyDRvqg%3A2%3A1713209445%3A-1%3A-1; fr=1E2UekTIuoNouDwBd.AWUpcX8O57zlwp43Dtmj6hS-NOM.BmHNKv..AAA.0.0.BmHYBn.AWUTOqLvnnM; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1713209450220%2C%22v%22%3A1%7D',
    'dpr': '2',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=tshirt&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.123", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.4.1"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'viewport-width': '1470',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'AdLibraryAdDetailsV2Query',
    'x-fb-lsd': '6ZnT2OUWVKCpbXXc7CcgVF',
    }
    
    variables = {
        "adArchiveID": adArchiveID,
        "pageID": pageID,
        "country": countary,
        "sessionID": "fe0143d7-8a38-40a2-b4bc-d513a6c540de",
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
    '__req': '1u',
    '__hs': '19828.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'GOOD',
    '__rev': '1012780108',
    '__s': '60imj1:m4ootu:5gtcmj',
    '__hsi': '7358178637906972205',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egz898mwkE-U6-3e4Ueo2sxOXwJwKwHxaaws8nwhE2Lxiaw4JwJwSyES0gq0K-1LwqobU2cwmo6O1Fw44wt87u',
    '__csr': '',
    'fb_dtsg': 'NAcOYuiN87FtGB9I2T0quxj1LdTh5ZjeSNloubvEPl01hrtT0P0XHtw:26:1713209445',
    'jazoest': '25467',
    'lsd': '6ZnT2OUWVKCpbXXc7CcgVF',
    '__spin_r': '1012780108',
    '__spin_b': 'trunk',
    '__spin_t': '1713209468',
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
