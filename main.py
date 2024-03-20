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


async def searchAds(session, page, countary,querry, forward_cursor, backward_cursor, collation_token) :
    cookies = {
        'wd': '1470x421',
        'fr': '1iyV8uKbKJuVDYXyp.AWXfkkcP_AFXFgpO21AARO5Hweo.Bl-d3P..AAA.0.0.Bl-fdZ.AWW-LFf1urE',
        'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1710880599740%2C%22v%22%3A1%7D',
        'c_user': '100077032827932',
        'xs': '19%3AbpxrFGOJGO81kA%3A2%3A1710871286%3A-1%3A-1%3A%3AAcXjDz2j5QIv7FjtTQaJYRstG7DAi0pge2NtEj0iMw',
        'sb': 'fMb5ZeOdkMH3vrgtLFC2fAxx',
        'locale': 'en_GB',
        'dpr': '2',
        'ps_l': '0',
        'ps_n': '0',
        'datr': 'ZY32ZYVf1hlBh3gAthGa1xZX',
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'en-IN,en-GB;q=0.9,en;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'cors',
        'Host': 'www.facebook.com',
        'Origin': 'https://www.facebook.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15',
        'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=Korting&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all',
        # 'Content-Length': '590',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        # 'Cookie': 'wd=1470x421; fr=1iyV8uKbKJuVDYXyp.AWXfkkcP_AFXFgpO21AARO5Hweo.Bl-d3P..AAA.0.0.Bl-fdZ.AWW-LFf1urE; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1710880599740%2C%22v%22%3A1%7D; c_user=100077032827932; xs=19%3AbpxrFGOJGO81kA%3A2%3A1710871286%3A-1%3A-1%3A%3AAcXjDz2j5QIv7FjtTQaJYRstG7DAi0pge2NtEj0iMw; sb=fMb5ZeOdkMH3vrgtLFC2fAxx; locale=en_GB; dpr=2; ps_l=0; ps_n=0; datr=ZY32ZYVf1hlBh3gAthGa1xZX',
        'X-FB-LSD': 'ykyyFHX5xv6SfTInSwCFUT',
        'X-ASBD-ID': '129477',
    }

    data = {
        '__aaid': '0',
        '__user': '100077032827932',
        '__a': '1',
        '__req': 'z',
        '__hs': '19801.BP:DEFAULT.2.0..0.0',
        'dpr': '2',
        '__ccg': 'EXCELLENT',
        '__rev': '1012156934',
        '__s': 'qhn5b7:90s2u2:q14sxp',
        '__hsi': '7348177097495137663',
        '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
        '__csr': '',
        'fb_dtsg': 'NAcPIY1ANeP5VQnCaW_h3eqfflJMuw88gVL7Jqk2GgpRtwvGqcVsK1Q:19:1710871286',
        'jazoest': '25530',
        'lsd': 'ykyyFHX5xv6SfTInSwCFUT',
        '__spin_r': '1012156934',
        '__spin_b': 'trunk',
        '__spin_t': '1710880803',
        '__jssesw': '1',
    }
    
    if page == 1:
        url =    f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id=4d0565dc-7140-422d-8d93-1ae23a1073a0&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'
        response = await fetch(session, url, headers=headers, cookies=cookies, data=data)
        # response = requests.post(
        #     cookies=cookies,
        #     headers=headers,
        #     data=data,
        # )
        return json.loads(response[9:])  
    else:
        
        cookies = {
            'wd': '1470x421',
            'c_user': '100077032827932',
            'fr': '1M0jEGawjFVskXIsL.AWURI49qKaGNbTC5dKhnuFx0q84.Bl-fhr..AAA.0.0.Bl-fhr.AWUqEP3amao',
            'xs': '19%3AbpxrFGOJGO81kA%3A2%3A1710871286%3A-1%3A-1%3A%3AAcVI6RyqlWRSTc72j2LvfCi3S1IVCmrAHAgPnR3UdQ',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1710880599740%2C%22v%22%3A1%7D',
            'sb': 'fMb5ZeOdkMH3vrgtLFC2fAxx',
            'locale': 'en_GB',
            'dpr': '2',
            'ps_l': '0',
            'ps_n': '0',
            'datr': 'ZY32ZYVf1hlBh3gAthGa1xZX',
        }
        
        data = {
            '__aaid': '0',
            '__user': '100077032827932',
            '__a': '1',
            '__req': '1d',
            '__hs': '19801.BP:DEFAULT.2.0..0.0',
            'dpr': '2',
            '__ccg': 'EXCELLENT',
            '__rev': '1012156934',
            '__s': 'eklaxc:90s2u2:q14sxp',
            '__hsi': '7348177097495137663',
            '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
            '__csr': '',
            'fb_dtsg': 'NAcPIY1ANeP5VQnCaW_h3eqfflJMuw88gVL7Jqk2GgpRtwvGqcVsK1Q:19:1710871286',
            'jazoest': '25530',
            'lsd': 'ykyyFHX5xv6SfTInSwCFUT',
            '__spin_r': '1012156934',
            '__spin_b': 'trunk',
            '__spin_t': '1710880803',
            '__jssesw': '1',
         }

        url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&{backward_cursor}=&session_id=4d0565dc-7140-422d-8d93-1ae23a1073a0&collation_token={collation_token}&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'
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
       'wd': '1470x414',
        'c_user': '100077032827932',
        'fr': '1M0jEGawjFVskXIsL.AWURI49qKaGNbTC5dKhnuFx0q84.Bl-fhr..AAA.0.0.Bl-fhr.AWUqEP3amao',
        'xs': '19%3AbpxrFGOJGO81kA%3A2%3A1710871286%3A-1%3A-1%3A%3AAcVI6RyqlWRSTc72j2LvfCi3S1IVCmrAHAgPnR3UdQ',
        'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1710880599740%2C%22v%22%3A1%7D',
        'sb': 'fMb5ZeOdkMH3vrgtLFC2fAxx',
        'locale': 'en_GB',
        'dpr': '2',
        'ps_l': '0',
        'ps_n': '0',
        'datr': 'ZY32ZYVf1hlBh3gAthGa1xZX',
    }


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=50%25%20korting&search_type=keyword_unordered&media_type=all',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-FB-Friendly-Name': 'AdLibraryAdDetailsV2Query',
        'X-FB-LSD': '2O5ojLcFqO2iOvYS8JrGkm',
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
        "sessionID": "4d0565dc-7140-422d-8d93-1ae23a1073a0",
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
        '__req': '1k',
        '__hs': '19801.BP:DEFAULT.2.0..0.0',
        'dpr': '2',
        '__ccg': 'EXCELLENT',
        '__rev': '1012156934',
        '__s': '5szqh1:8d7coo:s6q7g0',
        '__hsi': '7348183746726396245',
        '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
        '__csr': '',
        'fb_dtsg': 'NAcPPN88tRg_cq58GrOh-0LAVhpXhxiHUraZrThF-o7Lk0ZoDR5-FHA:19:1710871286',
        'jazoest': '25301',
        'lsd': '2O5ojLcFqO2iOvYS8JrGkm',
        '__spin_r': '1012156934',
        '__spin_b': 'trunk',
        '__spin_t': '1710882351',
        '__jssesw': '1',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'AdLibraryAdDetailsV2Query',
        'variables':variables_json, 
        'server_timestamps': 'true',
        'doc_id': '6635716889819821',
    }
    response = await fetch(session, 'https://www.facebook.com/api/graphql/', headers=headers, cookies=cookies, data=data)
    # response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
    return json.loads(response)




async def getPageAds(session, page, countary,querry,filtterStart_date, filtterEnd_date,Nextforward_cursor, Nextbackward_cursor, Nextcollation_token):
    data = await searchAds(session, page,countary ,querry, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token)
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
        
            if filtterStart_date <= start_date <= filtterEnd_date or filtterStart_date <= end_date <= filtterEnd_date:
                isActive = ad["isActive"]
                pageName = ad["pageName"]
                currentpageLike = ad["snapshot"]["page_like_count"]
                pageProfileUrl = ad["snapshot"]["page_profile_uri"]
                adcreativeId = ad["snapshot"]["ad_creative_id"]
                CallToActionButton = ad["snapshot"]["cta_text"]
                linkUrl = ad["snapshot"]["link_url"]
                description = ad["snapshot"]["body"]['markup']['__html']
                adUrl = f"https://www.facebook.com/ads/library/?id={adArchiveID}"
                adsdata =await viewad(session, adArchiveID, pageID, countary)
                print(adsdata['data']['ad_library_main']['ad_details']['aaa_info'])
                totalreach = adsdata['data']['ad_library_main']['ad_details']['aaa_info']['eu_total_reach']
                dataDict ={"pageName": pageName, "currentpageLike": currentpageLike, "pageProfileUrl": pageProfileUrl, 'description' : description ,"adcreativeId": adcreativeId,'adArchiveID' : adArchiveID , 'pageId': pageID, "CallToActionButton": CallToActionButton, "linkUrl": linkUrl, "adUrl": adUrl, "isActive": isActive,'TotalReach': totalreach ,"start_date": start_date, "end_date": end_date, "numberOfActiveDay": numberOfActiveDay}
                Adresult.append(dataDict)
  
    return {'results': Adresult, 'pageData': pageData}



@app.get("/ads", response_class=JSONResponse)
async def read_item(country:str = Query(...), page: int = Query(..., description="Minimum page number"), querry: str = Query(..., description="Querry"), filtterStart_date: datetime = Query(None), filtterEnd_date: datetime = Query(None), Nextforward_cursor: str = Query(None), Nextbackward_cursor: str = Query(None), Nextcollation_token: str = Query(None)):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        data = await getPageAds(session,page, country , querry, filtterStart_date,  filtterEnd_date, Nextforward_cursor, Nextbackward_cursor, Nextcollation_token)
        return data
    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)
