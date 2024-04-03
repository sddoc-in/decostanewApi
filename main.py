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
    session_id = 'ebd92aac-acb3-4849-bdf9-07c006f7a8eb'
    cookies = {
          'datr': 'A_75ZXVRLwPOHZCoh5VoaAOp',
    'ps_l': '0',
    'ps_n': '0',
    'fr': '0mJw0jQtGWqhsahy3..BmDauY..AAA.0.0.BmDauY.AWWn1zRCiUI',
    'sb': 'mKsNZtLOeCo5ltTbXTwlBhxv',
    'wd': '1470x545',
    }
    headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=tshirts&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&start_date[min]=2024-04-01&start_date[max]=&search_type=keyword_unordered&media_type=all',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-LSD': 'AVoTOvODzRQ',
    'X-ASBD-ID': '129477',
    'Origin': 'https://www.facebook.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'datr=A_75ZXVRLwPOHZCoh5VoaAOp; ps_l=0; ps_n=0; fr=0mJw0jQtGWqhsahy3..BmDauY..AAA.0.0.BmDauY.AWWn1zRCiUI; sb=mKsNZtLOeCo5ltTbXTwlBhxv; wd=1470x545',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }

    data = {
        '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': '1c',
    '__hs': '19816.BP:DEFAULT.2.0..0.0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1012513638',
    '__s': 'vh0cux:vpn7jw:ugczaj',
    '__hsi': '7353723192418828437',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
    '__csr': '',
    'lsd': 'AVoTOvODzRQ',
    'jazoest': '2975',
    '__spin_r': '1012513638',
    '__spin_b': 'trunk',
    '__spin_t': '1712172104',
    '__jssesw': '1',
    }
    
    if page == 1:
        # url =    f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id=15b5fb0b-2d87-4f6c-93a9-d56031103033&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'

        url = rf'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&verify=3edca362&session_id={session_id}&count=30&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&publisher_platforms[0]={publisher_platforms}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&search_type=keyword_unordered'


        response = await fetch(session, url, headers=headers, cookies=cookies, data=data)
        # response = requests.post(
        #     cookies=cookies,
        #     headers=headers,
        #     data=data,
        # )
        return json.loads(response[9:])  
    else:
        
        cookies = {
           'datr': 'A_75ZXVRLwPOHZCoh5VoaAOp',
            'ps_l': '0',
            'ps_n': '0',
            'fr': '0mJw0jQtGWqhsahy3..BmDauY..AAA.0.0.BmDauY.AWWn1zRCiUI',
            'sb': 'mKsNZtLOeCo5ltTbXTwlBhxv',
            'wd': '1470x545',
            'dpr': '2',
        }
        
        data = {
               '__aaid': '0',
                '__user': '0',
                '__a': '1',
                '__req': 'v',
                '__hs': '19816.BP:DEFAULT.2.0..0.0',
                'dpr': '2',
                '__ccg': 'GOOD',
                '__rev': '1012513638',
                '__s': '0sc7ne:vpn7jw:2yq92u',
                '__hsi': '7353724726806358308',
                '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
                '__csr': '',
                'lsd': 'AVoTOvODQ6c',
                'jazoest': '2924',
                '__spin_r': '1012513638',
                '__spin_b': 'trunk',
                '__spin_t': '1712172461',
                '__jssesw': '1',
         }

        # url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&{backward_cursor}=&session_id={session_id}&collation_token={collation_token}&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'
        url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&verify=3edca362&forward_cursor={forward_cursor}&backward_cursor={backward_cursor}&session_id={session_id}&collation_token={collation_token}&count=30&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered'
        
        
        response = await fetch(session,  url, headers=headers,cookies=cookies, data=data)

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
           'datr': 'A_75ZXVRLwPOHZCoh5VoaAOp',
    'ps_l': '0',
    'ps_n': '0',
    'fr': '0mJw0jQtGWqhsahy3..BmDauY..AAA.0.0.BmDauY.AWWn1zRCiUI',
    'sb': 'mKsNZtLOeCo5ltTbXTwlBhxv',
    'wd': '1470x545',
    'dpr': '2',
    }


    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=tshirts&start_date[min]=2024-04-01&start_date[max]=&search_type=keyword_unordered&media_type=all',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Friendly-Name': 'AdLibraryAdDetailsV2Query',
    'X-FB-LSD': 'AVoTOvODQ6c',
    'X-ASBD-ID': '129477',
    'Origin': 'https://www.facebook.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'datr=A_75ZXVRLwPOHZCoh5VoaAOp; ps_l=0; ps_n=0; fr=0mJw0jQtGWqhsahy3..BmDauY..AAA.0.0.BmDauY.AWWn1zRCiUI; sb=mKsNZtLOeCo5ltTbXTwlBhxv; wd=1470x545; dpr=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }
    
    variables = {
        "adArchiveID": adArchiveID,
        "pageID": pageID,
        "country": countary,
        "sessionID": "f2aa2f22-b20a-467d-9531-8eeb996b364f",
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
    '__req': '1g',
    '__hs': '19816.BP:DEFAULT.2.0..0.0',
    'dpr': '2',
    '__ccg': 'GOOD',
    '__rev': '1012513638',
    '__s': 'swhmpi:vpn7jw:2yq92u',
    '__hsi': '7353724726806358308',
    '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
    '__csr': '',
    'lsd': 'AVoTOvODQ6c',
    'jazoest': '2924',
    '__spin_r': '1012513638',
    '__spin_b': 'trunk',
    '__spin_t': '1712172461',
    '__jssesw': '1',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'AdLibraryAdDetailsV2Query',
        'variables':variables_json, 
        'server_timestamps': 'true',
        'doc_id': '6635716889819821'
    }
    response = await fetch(session, 'https://www.facebook.com/api/graphql/', headers=headers, cookies=cookies, data=data)
    # response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
    return json.loads(response)




async def getPageAds(session, page, countary,querry,filtterStart_date, filtterEnd_date,Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, ad_status_type, ad_type, media_type, content_languages , publisher_platforms):
    data = await searchAds(session, page,countary ,querry, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token, filtterEnd_date, filtterEnd_date, ad_status_type, ad_type, media_type, content_languages , publisher_platforms)
    # print(data)
    forward_cursor = data['payload']['forwardCursor']
    backward_cursor = data['payload']['backwardCursor']
    collation_token = data['payload']['collationToken']
    totalAdcount = data['payload']['totalCount']
    pageData = {"forward_cursor": forward_cursor, "backward_cursor": backward_cursor, "collation_token": collation_token, "totalAdcount": totalAdcount}
    Adresult = []
    for ads in data['payload']['results']:
        
        for ad in ads:
            adArchiveID = ad["adArchiveID"]
            pageID = ad["pageID"]
            start_date = ad["startDate"]
            end_date = ad["endDate"]
            numberOfActiveDay = (end_date - start_date)//86400
            start_date = await epoch_to_timestamp(start_date)
            end_date = await epoch_to_timestamp(end_date)
        
            # if filtterStart_date <= start_date <= filtterEnd_date or filtterStart_date <= end_date <= filtterEnd_date:
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
            adsdata =await viewad(session, adArchiveID, pageID, countary)
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
