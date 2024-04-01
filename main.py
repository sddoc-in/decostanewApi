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
    session_id = 'ccb3a562-2f22-4d7b-876f-7b40382ab4bf'
    cookies = {
       'wd': '1470x524',
        'fr': '19e137gJzUtNE35uL.AWXHjduWc40mhy86vR3QIWZfVA0.BmColY..AAA.0.0.BmComG.AWX-QGXc9lM',
        'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1711966554568%2C%22v%22%3A1%7D',
        'c_user': '100077032827932',
        'xs': '1%3A4sihRnxP-i1adQ%3A2%3A1711718431%3A-1%3A-1%3A%3AAcXuwPr6V8bRBBvnrMwhtXQmVDHmiz75C5cn7PhBrA',
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
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15',
        'Referer': 'https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=car&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&start_date[min]=2024-04-01&start_date[max]=&search_type=keyword_unordered&media_type=all',
        # 'Content-Length': '590',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        # 'Cookie': 'wd=1470x524; fr=19e137gJzUtNE35uL.AWXHjduWc40mhy86vR3QIWZfVA0.BmColY..AAA.0.0.BmComG.AWX-QGXc9lM; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1711966554568%2C%22v%22%3A1%7D; c_user=100077032827932; xs=1%3A4sihRnxP-i1adQ%3A2%3A1711718431%3A-1%3A-1%3A%3AAcXuwPr6V8bRBBvnrMwhtXQmVDHmiz75C5cn7PhBrA; sb=fMb5ZeOdkMH3vrgtLFC2fAxx; locale=en_GB; dpr=2; ps_l=0; ps_n=0; datr=ZY32ZYVf1hlBh3gAthGa1xZX',
        'X-FB-LSD': 'qhQnkrIohUFWMb4VWKX2i_',
        'X-ASBD-ID': '129477',
    }

    data = {
        '__aaid': '0',
        '__user': '100077032827932',
        '__a': '1',
        '__req': '11',
        '__hs': '19814.BP:DEFAULT.2.0..0.0',
        'dpr': '2',
        '__ccg': 'EXCELLENT',
        '__rev': '1012446745',
        '__s': 'myoz3c:qgz4kn:p04cwv',
        '__hsi': '7352841675553804076',
        '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
        '__csr': '',
        'fb_dtsg': 'NAcNggZitJj97tyzlQUUs9vBJnh1cWyCQpShGX5RuuHpWJ3NU9_OfjQ:1:1711718431',
        'jazoest': '25580',
        'lsd': 'qhQnkrIohUFWMb4VWKX2i_',
        '__spin_r': '1012446745',
        '__spin_b': 'trunk',
        '__spin_t': '1711966860',
        '__jssesw': '1',
    }
    
    if page == 1:
        # url =    f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id=15b5fb0b-2d87-4f6c-93a9-d56031103033&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'

        url = rf'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&session_id={session_id}&count=30&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&publisher_platforms[0]={publisher_platforms}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&search_type=keyword_unordered'


        response = await fetch(session, url, headers=headers, cookies=cookies, data=data)
        # response = requests.post(
        #     cookies=cookies,
        #     headers=headers,
        #     data=data,
        # )
        return json.loads(response[9:])  
    else:
        
        cookies = {
            'wd': '1470x524',
            'fr': '19e137gJzUtNE35uL.AWXHjduWc40mhy86vR3QIWZfVA0.BmColY..AAA.0.0.BmComG.AWX-QGXc9lM',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1711966554568%2C%22v%22%3A1%7D',
            'c_user': '100077032827932',
            'xs': '1%3A4sihRnxP-i1adQ%3A2%3A1711718431%3A-1%3A-1%3A%3AAcXuwPr6V8bRBBvnrMwhtXQmVDHmiz75C5cn7PhBrA',
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
            '__req': '2d',
            '__hs': '19814.BP:DEFAULT.2.0..0.0',
            'dpr': '2',
            '__ccg': 'EXCELLENT',
            '__rev': '1012446745',
            '__s': 'ulaxsa:qgz4kn:p04cwv',
            '__hsi': '7352841675553804076',
            '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
            '__csr': '',
            'fb_dtsg': 'NAcNggZitJj97tyzlQUUs9vBJnh1cWyCQpShGX5RuuHpWJ3NU9_OfjQ:1:1711718431',
            'jazoest': '25580',
            'lsd': 'qhQnkrIohUFWMb4VWKX2i_',
            '__spin_r': '1012446745',
            '__spin_b': 'trunk',
            '__spin_t': '1711966860',
            '__jssesw': '1',
         }

        # url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&{backward_cursor}=&session_id={session_id}&collation_token={collation_token}&count=30&active_status=all&ad_type=all&countries[0]={countary}&media_type=all&search_type=keyword_unordered'
        url = f'https://www.facebook.com/ads/library/async/search_ads/?q={querry}&forward_cursor={forward_cursor}&backward_cursor={backward_cursor}&session_id={session_id}&collation_token={collation_token}&count=30&active_status={ad_status_type}&ad_type={ad_type}&countries[0]={countary}&start_date[min]={start_date}&start_date[max]={end_date}&media_type={media_type}&content_languages[0]={content_languages}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered'
        
        
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
         'wd': '1467x525',
        'fr': '19e137gJzUtNE35uL.AWUzbwcgip9uZkI8NyY4A1jDjf8.BmColY..AAA.0.0.BmCtdA.AWV1ySAheu8',
        'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1711966554568%2C%22v%22%3A1%7D',
        'c_user': '100077032827932',
        'xs': '1%3A4sihRnxP-i1adQ%3A2%3A1711718431%3A-1%3A-1%3A%3AAcXuwPr6V8bRBBvnrMwhtXQmVDHmiz75C5cn7PhBrA',
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
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15',
        'Referer': 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=NL&q=korting&search_type=keyword_unordered&media_type=all',
        # 'Content-Length': '1014',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        # 'Cookie': 'wd=1470x414; fr=1QXa8HCZpV8e3QuMZ.AWUDaYo6oCpvLdoc6jjVbicBII8.Bl-gav..AAA.0.0.BmBsKS.AWVCuu_Qw8o; c_user=100077032827932; sb=fMb5ZeOdkMH3vrgtLFC2fAxx; xs=1%3A4sihRnxP-i1adQ%3A2%3A1711718431%3A-1%3A-1; locale=en_GB; dpr=2; ps_l=0; ps_n=0; datr=ZY32ZYVf1hlBh3gAthGa1xZX',
        'X-FB-LSD': '1L_LMRQOPL7nrHRSCeN4G6',
        'X-ASBD-ID': '129477',
        'X-FB-Friendly-Name': 'AdLibraryAdDetailsV2Query',
        'Priority': 'u=3, i'
    }
    
    variables = {
        "adArchiveID": adArchiveID,
        "pageID": pageID,
        "country": countary,
        "sessionID": "15b5fb0b-2d87-4f6c-93a9-d56031103033",
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
        '__req': '18',
        '__hs': '19814.BP:DEFAULT.2.0..0.0',
        'dpr': '2',
        '__ccg': 'GOOD',
        '__rev': '1012447370',
        '__s': 'xyr5ev:jfv7zj:3i6the',
        '__hsi': '7352926059470857207',
        '__dyn': '7xeUmxa3-Q8zo5ObwKBAgc9o9E6u5U4e1FxebzEdF8ixy7EiwvoWdwJwCwfW7oqx60Vo1upEK12wvk1bwbG78b87C2m3K2y11wBz81s8hwGwQwoE2LwBgao884y0Mo6i588Egze2a5E5afK1LwPxe3C0D8sKUbobEaUiyE725U4q0HUkyE1bobodEGdw46wbLwrU6C2-0z85C1Iwqo1187i',
        '__csr': '',
        'fb_dtsg': 'NAcMPSwpeZJHyrYuvCPAMc8-H8EosKzXCj9MawBXCWIPk7KTlSsqImA:1:1711718431',
        'jazoest': '25456',
        'lsd': 'GQjLGyy741OiKxyn2jsti6',
        '__spin_r': '1012447370',
        '__spin_b': 'trunk',
        '__spin_t': '1711986507',
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
