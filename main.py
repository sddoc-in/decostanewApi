from datetime import datetime
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse  
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import aiohttp , asyncio, json

app = FastAPI()

origins = [
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


async def searchAds(session, page, querry, forward_cursor, backward_cursor, collation_token) :
    cookies = {
        'datr': 'ZyxNZbilHpbTxXpxf2VtHnPd',
        'sb': 'cixNZdyC4kZX4AXOgluRFqAL',
        'fr': '1dA3xEB8mCGNbT0S5.AWUGAXyGo1hCKJ5oXR6FpUJGlH8.Bl2vbh..AAA.0.0.Bl2vbh.AWXGDaLTqwU',
        'c_user': '100068654010842',
        'xs': '23%3AwaIWGTAT56i-Tg%3A2%3A1703702739%3A-1%3A1093%3A%3AAcUCkgyscd0nkP7QThlsookowzLahuOJRdFhqdDm5eo',
        'ps_n': '0',
        'ps_l': '0',
        'wd': '1760x445',
        'dpr': '1.0909090909090908',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=50%25%20korting&search_type=keyword_unordered&media_type=all',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-FB-LSD': 'xQ4h19qS8SlHtTePF6kgZz',
        'X-ASBD-ID': '129477',
        'Origin': 'https://www.facebook.com',
        'Alt-Used': 'www.facebook.com',
        'Connection': 'keep-alive',
        # 'Cookie': 'datr=ZyxNZbilHpbTxXpxf2VtHnPd; sb=cixNZdyC4kZX4AXOgluRFqAL; fr=1dA3xEB8mCGNbT0S5.AWUGAXyGo1hCKJ5oXR6FpUJGlH8.Bl2vbh..AAA.0.0.Bl2vbh.AWXGDaLTqwU; c_user=100068654010842; xs=23%3AwaIWGTAT56i-Tg%3A2%3A1703702739%3A-1%3A1093%3A%3AAcUCkgyscd0nkP7QThlsookowzLahuOJRdFhqdDm5eo; ps_n=0; ps_l=0; wd=1760x445; dpr=1.0909090909090908',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = {
        '__aaid': '0',
        '__user': '100068654010842',
        '__a': '1',
        '__req': '2',
        '__hs': '19778.BP:DEFAULT.2.0..0.0',
        'dpr': '1.5',
        '__ccg': 'UNKNOWN',
        '__rev': '1011640432',
        '__s': '1mordp:t2lw2d:r46w9g',
        '__hsi': '7339452381923427595',
        '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11xmfz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
        '__csr': '',
        'fb_dtsg': 'NAcNf8P85mdRDhPlvF-OjcVJWHQPx60KU9FkhZDF-yNxejxJFnX9H2A:23:1703702739',
        'jazoest': '25276',
        'lsd': 'xQ4h19qS8SlHtTePF6kgZz',
        '__spin_r': '1011640432',
        '__spin_b': 'trunk',
        '__spin_t': '1708849421',
        '__jssesw': '1',
    }

    if page == 1:
        url =    f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id=1928765f-6d75-4606-8988-417d3b37d2ea&count=30&active_status=all&ad_type=all&countries[0]=NL&media_type=all&search_type=keyword_unordered'
        response = await fetch(session, url, headers=headers, cookies=cookies, data=data)
        # response = requests.post(
        #     cookies=cookies,
        #     headers=headers,
        #     data=data,
        # )
        return json.loads(response[9:])  
    else:
        url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&{backward_cursor}=&session_id=1928765f-6d75-4606-8988-417d3b37d2ea&collation_token={collation_token}&count=30&active_status=all&ad_type=all&countries[0]=NL&media_type=all&search_type=keyword_unordered'
        response = await fetch(session,  url, headers=headers,cookies=cookies, data=data)
        # response = requests.post(url, cookies=cookies, headers=headers, data=data)
        return json.loads(response.text[9:])  


async def epoch_to_timestamp(epoch_time):
    try:
        timestamp = datetime.fromtimestamp(epoch_time)
        # return timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return timestamp.strptime(timestamp.strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return f"Error: {e}"

async def viewad(session, adArchiveID, pageID):
    cookies = {
        'datr': 'ZyxNZbilHpbTxXpxf2VtHnPd',
        'sb': 'cixNZdyC4kZX4AXOgluRFqAL',
        'fr': '1dA3xEB8mCGNbT0S5.AWUGAXyGo1hCKJ5oXR6FpUJGlH8.Bl2vbh..AAA.0.0.Bl2vbh.AWXGDaLTqwU',
        'c_user': '100068654010842',
        'xs': '23%3AwaIWGTAT56i-Tg%3A2%3A1703702739%3A-1%3A1093%3A%3AAcUCkgyscd0nkP7QThlsookowzLahuOJRdFhqdDm5eo',
        'ps_n': '0',
        'ps_l': '0',
        'wd': '1760x650',
        'dpr': '1.0909090909090908',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=50%25%20korting&search_type=keyword_unordered&media_type=all',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-FB-Friendly-Name': 'AdLibraryAdDetailsV2Query',
        'X-FB-LSD': 'xQ4h19qS8SlHtTePF6kgZz',
        'X-ASBD-ID': '129477',
        'Origin': 'https://www.facebook.com',
        'Connection': 'keep-alive',
        # 'Cookie': 'datr=ZyxNZbilHpbTxXpxf2VtHnPd; sb=cixNZdyC4kZX4AXOgluRFqAL; fr=1dA3xEB8mCGNbT0S5.AWUGAXyGo1hCKJ5oXR6FpUJGlH8.Bl2vbh..AAA.0.0.Bl2vbh.AWXGDaLTqwU; c_user=100068654010842; xs=23%3AwaIWGTAT56i-Tg%3A2%3A1703702739%3A-1%3A1093%3A%3AAcUCkgyscd0nkP7QThlsookowzLahuOJRdFhqdDm5eo; ps_n=0; ps_l=0; wd=1760x650; dpr=1.0909090909090908',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    
    variables = {
        "adArchiveID": adArchiveID,
        "pageID": pageID,
        "country": "NL",
        "sessionID": "1928765f-6d75-4606-8988-417d3b37d2ea",
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
        '__req': '10',
        '__hs': '19778.BP:DEFAULT.2.0..0.0',
        'dpr': '1.5',
        '__ccg': 'UNKNOWN',
        '__rev': '1011640432',
        '__s': 'rhex4p:t2lw2d:r46w9g',
        '__hsi': '7339452381923427595',
        '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11xmfz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
        '__csr': '',
        'fb_dtsg': 'NAcNf8P85mdRDhPlvF-OjcVJWHQPx60KU9FkhZDF-yNxejxJFnX9H2A:23:1703702739',
        'jazoest': '25276',
        'lsd': 'xQ4h19qS8SlHtTePF6kgZz',
        '__spin_r': '1011640432',
        '__spin_b': 'trunk',
        '__spin_t': '1708849421',
        '__jssesw': '1',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'AdLibraryAdDetailsV2Query',
        # 'variables': '{"adArchiveID":"3330326767267271","pageID":"103483832005367","country":"NL","sessionID":"1928765f-6d75-4606-8988-417d3b37d2ea","source":null,"isAdNonPolitical":true,"isAdNotAAAEligible":false}',
        'variables': variables_json,
        'server_timestamps': 'true',
        'doc_id': '6635716889819821',
    }
    response = await fetch(session, 'https://www.facebook.com/api/graphql/', headers=headers, cookies=cookies, data=data)
    # response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
    return json.loads(response)




async def getPageAds(session, page, querry,filtterStart_date, filtterEnd_date,Nextforward_cursor, Nextbackward_cursor, Nextcollation_token):
    data = await searchAds(session, page, querry, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token)
    forward_cursor = data['payload']['forwardCursor']
    backward_cursor = data['payload']['backwardCursor']
    collation_token = data['payload']['collationToken']
    totalAdcount = data['payload']['totalCount']
    pageData = {"forward_cursor": forward_cursor, "backward_cursor": backward_cursor, "collation_token": collation_token, "totalAdcount": totalAdcount}
    Adresult = []
    for ads in data['payload']['results']:
        adArchiveID = ads[0]["adArchiveID"]
        pageID = ads[0]["pageID"]
        start_date = ads[0]["startDate"]
        end_date = ads[0]["endDate"]
        numberOfActiveDay = (end_date - start_date)//86400
        start_date = await epoch_to_timestamp(start_date)
        end_date = await epoch_to_timestamp(end_date)
        if filtterStart_date <= start_date <= filtterEnd_date or filtterStart_date <= end_date <= filtterEnd_date:
            isActive = ads[0]["isActive"]
            pageName = ads[0]["pageName"]
            currentpageLike = ads[0]["snapshot"]["page_like_count"]
            pageProfileUrl = ads[0]["snapshot"]["page_profile_uri"]
            adcreativeId = ads[0]["snapshot"]["ad_creative_id"]
            CallToActionButton = ads[0]["snapshot"]["cta_text"]
            linkUrl = ads[0]["snapshot"]["link_url"]
            description = ads[0]["snapshot"]["body"]['markup']['__html']
            adUrl = f"https://www.facebook.com/ads/library/?id={adArchiveID}"
            adsdata =await viewad(session, adArchiveID, pageID)
            totalreach = adsdata['data']['ad_library_main']['ad_details']['aaa_info']['eu_total_reach']
            dataDict ={"pageName": pageName, "currentpageLike": currentpageLike, "pageProfileUrl": pageProfileUrl, 'description' : description ,"adcreativeId": adcreativeId,'adArchiveID' : adArchiveID , 'pageId': pageID, "CallToActionButton": CallToActionButton, "linkUrl": linkUrl, "adUrl": adUrl, "isActive": isActive,'TotalReach': totalreach ,"start_date": start_date, "end_date": end_date, "numberOfActiveDay": numberOfActiveDay}
            Adresult.append(dataDict)
  
    return {'results': Adresult, 'pageData': pageData}



@app.get("/ads", response_class=JSONResponse)
async def read_item(page: int = Query(..., description="Minimum page number"), querry: str = Query(..., description="Querry"), filtterStart_date: datetime = Query(None), filtterEnd_date: datetime = Query(None), Nextforward_cursor: str = Query(None), Nextbackward_cursor: str = Query(None), Nextcollation_token: str = Query(None)):
    async with aiohttp.ClientSession() as session:
        data = await getPageAds(session,page, querry, filtterStart_date,  filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token)
        return data
    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)