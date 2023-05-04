try:
    import datetime
    import json
    import os
    import ctypes
    import uuid
    import asyncio
    import random
    import time
    import requests as r
    from colorama import Fore, Style
    from rgbprint import Color
    import aiohttp
#  from fp.fp import FreeProxy
    #import discord_webhook
    #from discord_webhook import DiscordWebhook, DiscordEmbed

except ModuleNotFoundError:
    import os
    print("Missing some libraries, installing them now...")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install aiohttp")
    #os.system("pip install discord-webhook")
   # os.system("pip install free-proxy")
    os.system("pip install rgbprint")

    print("All libraries were installed, you can now start.")
    os.system("pause")
    exit(1)

os.system("cls" if os.name == "nt" else "clear")

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW("UGCatcher")

#linkGet = r.get("https://pastebin.com/raw/9gJ5tbPP")
#linkLCP = "GA"

# if linkGet.status_code != 200:
#   pass

#webhookURI = linkGet.text + linkLCP
# print(webhookURI)

#webhook = DiscordWebhook(url=webhookURI)

# Based on xolo sniper and J3L Sniper but better


class UGCatcher():
    def __init__(self) -> None:
        # Only logs the items buyed by the bot, dont risk
        #self.webhookLogs = webhook
        self.items = self._setItems()

        self.username = str
        self.userID = str
        self.userDisplayName = str
        self.version = "3.0.0"
        self.title = (f"""
{Color(0xdb222a)}██╗░░░██╗░██████╗░░█████╗░░█████╗░████████╗░█████╗░██╗░░██╗███████╗██████╗░░░░░██╗██████╗░░░░░█████╗░
{Color(0xc32530)}██║░░░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░██║██╔════╝██╔══██╗░░░██╔╝╚════██╗░░░██╔══██╗
{Color(0xab2836)}██║░░░██║██║░░██╗░██║░░╚═╝███████║░░░██║░░░██║░░╚═╝███████║█████╗░░██████╔╝░░██╔╝░░█████╔╝░░░██║░░██║
{Color(0x942b3b)}██║░░░██║██║░░╚██╗██║░░██╗██╔══██║░░░██║░░░██║░░██╗██╔══██║██╔══╝░░██╔══██╗░██╔╝░░░╚═══██╗░░░██║░░██║
{Color(0x7c2e41)}╚██████╔╝╚██████╔╝╚█████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██║███████╗██║░░██║██╔╝░░░██████╔╝██╗╚█████╔╝
{Color(0x643047)}░╚═════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░╚═════╝░╚═╝░╚════╝░

{Color(0x4c334d)}| Version {self.version}
""")
        self.checks = 0
        self.buys = 0
        self.request_method = 2
        self.total_ratelimits = 0
        self.last_time = 0
        self.errors = 0
        self.clear = "cls" if os.name == 'nt' else "clear"
        self.task = None
        self.accounts = None
        self.getNewIDS = []
        self.lastFree = {}
#       self.proxylist = open("proxies.txt").read().splitlines()

        self._getVersion()
        self._setAccounts()

       # with open("data/config.json") as file:
        #    config = json.load(file)

        self.actualProxies = []
        #self.enableProxy =  False if not config["proxy"] or config["proxy"]["useProxy"] == False else True
        #self.getProxyCustom = False if not config["proxy"] or config["proxy"]["useCustomProxy"] == False or self.enableProxy == False else open("data/proxies.txt").read().splitlines()
        #self.getProxyRandom = False if not config["proxy"] or config["proxy"]["useCustomProxy"] == True or self.enableProxy == False else FreeProxy(rand=True).get()

        # if self.enableProxy:
        asyncio.run(self.proxyStart())

        asyncio.run(self.start())

    # Proxy support with aiohttp
    async def check(self, proxy):
        try:
            response = r.get('http://httpbin.org/ip',
                             proxies={'http': proxy, 'https': proxy}, timeout=15)
            if response.status_code == 200:
                self.actualProxies.append(proxy)
            elif response.status_code == 504:
                self.task = f"{proxy} proxy has failed, looking for new one..."
                self._UI
            elif response.status_code == 403:
                self.task = f"{proxy} proxy has failed, looking for new one..."
                self._UI
        except r.exceptions.RequestException as e:
            self.task = f"{proxy} proxy has failed with an exception | Error: {e}"
            self._UI
            return

    def _getVersion(self):
        self.task = "Checking version..."
        self._UI()
        response = r.get("https://pastebin.com/raw/mD9PNFV9")

        if response.status_code != 200:
            pass
        # print(response.text)

        # if not response.text == self.version:
         #   print(Style.BRIGHT + f"{Fore.GREEN}Buscando actualizaciones...")
          #  gitcode = r.get("https://raw.githubusercontent.com/Furrycality/UGCatcher/main/main.py").text
           # with open("main.py", "r+") as f:
            #    if f.read() != gitcode:
            #       print(Style.BRIGHT + f"{Fore.RED}Se encontro una nueva versión, actualizando...")
            #      f.write(gitcode)
            #print(Style.BRIGHT + f"{Fore.GREEN}Actualizado correctamente a la version {response.text}...")
            # os.system("pause")
            # exit(0)

    def getWorkingProxy(self):
        if len(self.actualProxies) != 0:
            random.shuffle(self.actualProxies)
            proxy = self.actualProxies[0]
            # print(proxy)
            return proxy

    async def proxyStart(self):
        os.system(self.clear)
        self.task = "Verifying proxies..."
        self._UI()
        coroutines = []

#        if self.enableProxy:
 #           if self.getProxyCustom:
    #              proxy = self.getProxyCustom
   #             coroutines.append(self.check(proxy))
    #        else:
     #           for i in range(10):
      #              proxy = str(self.getProxyRandom)
       #             coroutines.append(self.check(proxy))
        # else:
        proxy = '87.236.197.231:3128'
        coroutines.append(self.check(proxy))

        await asyncio.gather(*coroutines)

    class makeDict(dict):
        def __getattr__(self, attr):
            return self[attr]

    def _setAccounts(self) -> None:
        self.task = "Account Loader"
        self._UI
        cookies = self._setCookies()

        for i in cookies:
            response = asyncio.run(self._getUserID(cookies[i]["cookie"]))
            response2 = asyncio.run(self._getXCSRF(cookies[i]["cookie"]))
            cookies[i]["id"] = response
            cookies[i]["xcsrf_token"] = response2["xcsrf_token"]
            cookies[i]["created"] = response2["created"]
        self.accounts = cookies

    def _setCookies(self) -> dict:
        with open("data/cookies.txt", "r") as f:
            lines = f.read().split('\n')
            getCookies = {}

            for i, line in enumerate(lines):
                if len(line) == 0:
                    continue
                getCookies[str(i+1)] = {}
                getCookies[str(i+1)] = {"cookie": line}
            return getCookies

    def _setItems(self) -> list:
        with open('data/limiteds.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]

    async def _getUserID(self, cookie) -> str:
        response = r.get("https://users.roblox.com/v1/users/authenticated",
                         cookies={".ROBLOSECURITY": cookie}, verify=True)
        data = response.json()
        if data.get('id') == None:
            raise Exception("Could not obtain the ID - Error:", data)
        return data.get('id')

    def _getUserData(self, cookie) -> dict:
        response = r.get("https://users.roblox.com/v1/users/authenticated",
                         cookies={".ROBLOSECURITY": cookie}, verify=True)
        try:
            data = response.json()
            return {"name": data.get('name'), "displayName": data.get('displayName'), "id": data.get('id')}
        except:
            raise Exception("Problem getting user data", data)

    def _addValues(self):
        if self.accounts is not None:
            for i in self.accounts:
                response = self._getUserData(self.accounts[i]["cookie"])
                self.username = response["name"]
                self.userDisplayName = response["displayName"]
                self.userID = response["id"]

    def _UI(self) -> None:
        self._addValues()
        print(Fore.GREEN + Style.BRIGHT + self.title)
        print(Fore.RESET + Style.RESET_ALL)
        print(Style.BRIGHT +
              f" {Fore.RED}{Style.BRIGHT}🚩 This is a preliminary version and may have critical errors and performance issues.{Fore.WHITE}")
        print()
        #print(Style.BRIGHT + f" 🧭 Proxy actual  : {Color(0x5c95ff)}{Style.BRIGHT}{self.getWorkingProxy()}{Fore.WHITE}")
        print(Style.BRIGHT +
              f" ⏱️ Speed     : {Color(0xbfdbf7)}{Style.BRIGHT}{self.last_time}{Fore.WHITE}")
        print("  -----------")
        print(Style.BRIGHT +
              f" 🙍 User       : {Color(0x3f88c5)}{Style.BRIGHT}{self.userID} / {self.username} ({self.userDisplayName}){Fore.WHITE}")
        print("  -----------")
        print(Style.BRIGHT +
              f" 🛒 Purchased       : {Color(0x5c95ff)}{Style.BRIGHT}{self.buys}{Fore.WHITE}")
        print(Style.BRIGHT +
              f" ⚠️ Errors       : {Color(0xd90429)}{Style.BRIGHT}{self.errors}{Fore.WHITE}")
        print(Style.BRIGHT +
              f" 🚗 Rate limits    : {Color(0xb10f2e)}{Style.BRIGHT}{self.total_ratelimits}{Fore.WHITE}")
        print(Style.BRIGHT +
              f" 💻 Revisions    : {Color(0x5c95ff)}{Style.BRIGHT}{self.checks}{Fore.WHITE}")
        print("  -----------")
        print(Style.BRIGHT +
              f" 📌 Current Task  : {Color(0x5c95ff)}{Style.BRIGHT}{self.task}{Fore.WHITE}")
        print("  -----------")

    async def _getXCSRF(self, cookie) -> dict:
        response = r.post("https://accountsettings.roblox.com/v1/email",
                          cookies={".ROBLOSECURITY": cookie}, verify=True)
        xcsrf_token = response.headers.get("x-csrf-token")
        if xcsrf_token is None:
            raise Exception(
                "An error occurred while trying to obtain the X-CSRF-TOKEN key - it may be due to an invalid cookie")
        return {"xcsrf_token": xcsrf_token, "created": datetime.datetime.now()}

    async def _checkXCSRF(self) -> bool:
        if self.accounts is not None:
            for i in self.accounts:
                if self.accounts[i]["xcsrf_token"] is None or \
                        datetime.datetime.now() > (self.accounts[i]["created"] + datetime.timedelta(minutes=10)):
                    try:
                        response = await self._getXCSRF(self.accounts[i]["cookie"])
                        self.accounts[i]["xcsrf_token"] = response["xcsrf_token"]
                        self.accounts[i]["created"] = response["created"]
                        return True
                    except Exception as e:
                        print(f"{e.__class__.__name__}: {e}")
                    return False
                return True
            return False
        return False

    async def buyItem(self, item_id: int, price: int, user_id: int, creator_id: int,
                      product_id: int, cookie: str, x_token: str) -> None:

        """
           Purchase a limited item on Roblox.
           Args:
               item_id (int): ID of the limited to buy.
               price (int): Cost of the Roblox item.
               user_id (int): User ID.
               creator_id (int): User ID of the creator of the limited.
               product_id (int): The ID of the product to which the limited item belongs.
               cookie (str): User's Roblox cookie.
               x_token (str): The X-CSRF-TOKEN associated with the purchase.
               proxy (str): Proxy server address.
        """

        data = {
            "collectibleItemId": item_id,
            "expectedCurrency": 1,
            "expectedPrice": price,
            "expectedPurchaserId": user_id,
            "expectedPurchaserType": "User",
            "expectedSellerId": creator_id,
            "expectedSellerType": "User",
            "idempotencyKey": "random uuid4 string that will be your key or smthn",
            "collectibleProductId": product_id
        }
        total_errors = 0
        async with aiohttp.ClientSession() as client:
            while True:
                if total_errors >= 10:
                    print("Too many errors encountered. Aborting purchase.")
                    return

                data["idempotencyKey"] = str(uuid.uuid4())

                try:
                    response = await client.post(f"https://apis.roblox.com/marketplace-sales/v1/item/{item_id}/purchase-item",
                                                 json=data,
                                                 headers={
                                                     "x-csrf-token": x_token},
                                                 cookies={
                                                     ".ROBLOSECURITY": cookie},
                                                 proxies=self.getWorkingProxy(),
                                                 ssl=False)

                except r.exceptions.RequestException as e:
                    self.errors += 1
                    print(
                        f"An error has occured in the connection: {e}. Retrying...")
                    total_errors += 1
                    continue

                if response.status == 429:
                    print("Rate limit encountered. Retrying purchase in 0.5 seconds...")
                    await self.proxyStart()
                    await asyncio.sleep(0.5)
                    continue

                try:
                    json_response = await response.json()
                except aiohttp.ContentTypeError as e:
                    self.errors += 1
                    print(
                        f"JSON decode error encountered: {e}. Retrying purchase...")
                    total_errors += 1
                    continue

                if not json_response["purchased"]:
                    self.errors += 1
                    print(
                        f"Purchase failed. Response: {json_response}. Retrying purchase...")
                    total_errors += 1
                else:
                    print(f"Purchase successful. Response: {json_response}.")
                    self.buys += 1


#                       if self.webhookLogs:
 #                           if self.accounts is not None:
    #                              currentAccount = self.accounts[str(random.randint(1, len(self.accounts)))]
   #                             headers = {"x-csrf-token": currentAccount['xcsrf_token']}
    #                            cookies = {".ROBLOSECURITY": currentAccount["cookie"]}
     #                           info = r.post("https://catalog.roblox.com/v1/catalog/items/details", json={"items": [{"itemType": "Asset", "id": item_id}]}, headers=headers,  cookies=cookies, proxies=self.getWorkingProxy())
        #                          thumbnail = r.get(f"https://thumbnails.roblox.com/v1/assets?assetIds={item_id}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false", headers=headers, cookies=cookies)

       #                         if info.status_code == 200 and thumbnail.status_code == 200:
            #                            embedContent = {
        #                           "title": f"{info.json()['data'][0]['name']}",
           #                         "url": f"https://rblx.clothing/{item_id}/UGCatcher",
          #                          "color": 65280,

                    # "fields":[ {
                    # "name":"purchaseResult",
                    # "value": f"{json_response['purchaseResult']}",
                    # "inline":True
                    # },
                    # {
                    # "name": "purchased",
                    # "value": f"{json_response['purchased']}",
                    # "inline":True },
                    # {
                    # "name":"errorMessage",
                    # "value":f"{json_response['errorMessage']}"
                    # }],

                    #    "author": {
                    #         "name": "Limited comprado exitosamente"
                    #  },
                    #   "footer": {
                    #     "text": f"UGCatcher {self.version} - by Furrycality"
                #                    },
            #                     "thumbnail": {
            #                          "url": f"{thumbnail.json()['data'][0]['imageUrl']}"
             #                       }
            #                    }

             ##                   r.post(self.webhookLogs, json={"content": None, "embeds": [embedContent]})


    async def getLimiteds(self) -> None:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
            while True:
                try:
                    async with session.get("https://catalog.roblox.com/v1/search/items/details?Keyword=orange%20teal%20cyan%20red%20green%20topaz%20yellow%20wings%20maroon%20space%20dominus%20lime%20mask%20mossy%20wooden%20crimson%20salmon%20brown%20pastel%20%20ruby%20diamond%20creatorname%20follow%20catalog%20link%20rare%20emerald%20chain%20blue%20deep%20expensive%20furry%20hood%20currency%20coin%20royal%20navy%20ocean%20air%20white%20cyber%20ugc%20verified%20black%20purple%20yellow%20violet%20description%20dark%20bright%20rainbow%20pink%20cyber%20roblox%20multicolor%20light%20gradient%20grey%20gold%20cool%20indigo%20test%20hat%20limited2%20headphones%20emo%20edgy%20back%20front%20lava%20horns%20water%20waist%20face%20neck%20shoulders%20collectable&Category=11&Subcategory=19&CurrencyType=3&MaxPrice=0&salesTypeFilter=2&SortType=3&limit=30", ssl=False) as response:
                        response.raise_for_status()

                        items = (json.loads(await response.text())['data'])

                        print('\n')

                        for item in items:
                            if item["id"] not in self.getNewIDS:
                                print(
                                    Style.BRIGHT + f" ⚠️ A free item was found: {Color(0xF7C600)}{item['name']} (ID: {item['id']}){Fore.WHITE}")
                                self.lastFree = item
                                self.getNewIDS.append(item)

                                if self.lastFree.get("priceStatus", "Off Sale") == "Off Sale":
                                    continue

                                if self.lastFree.get("collectibleItemId") is None:
                                    continue

                                productid_response = await session.post("https://apis.roblox.com/marketplace-items/v1/items/details",
                                                                        json={"itemIds": [
                                                                            self.lastFree["collectibleItemId"]]},
                                                                        headers={"x-csrf-token": self.accounts[str(random.randint(
                                                                            1, len(self.accounts)))]["xcsrf_token"], 'Accept': "application/json"},
                                                                        cookies={".ROBLOSECURITY": self.accounts[str(
                                                                            random.randint(1, len(self.accounts)))]["cookie"]},
                                                                        proxy=self.actualProxies,
                                                                        ssl=False)
                                response.raise_for_status()
                                productid_data = json.loads(await productid_response.text())[0]
                                coroutines = [self.buyItem(item_id=self.lastFree["collectibleItemId"], price=0, user_id=self.accounts[i]["id"], creator_id=self.lastFree['creatorTargetId'],
                                                           product_id=productid_data['collectibleProductId'], cookie=self.accounts[i]["cookie"], x_token=self.accounts[i]["xcsrf_token"]) for i in self.accounts]
                                self.task = "Buying the limiteds"
                                await asyncio.gather(*coroutines)

                except aiohttp.client_exceptions.ClientConnectorError as e:
                    print(f"Error connecting to host: {e}")
                    self.errors += 1
                except aiohttp.client_exceptions.ServerDisconnectedError as e:
                    print(f"Server disconnected error: {e}")
                    self.errors += 1
                except aiohttp.client_exceptions.ClientOSError as e:
                    print(f"Client OS error: {e}")
                    self.errors += 1
                except aiohttp.client_exceptions.ClientResponseError as e:
                    if self.enableProxy:
                        asyncio.run(self.proxyStart())
                    print(f"Response Error: {e}")
                    self.errors += 1
                finally:
                    self.checks += 1
                    await asyncio.sleep(5)

    async def snipeID(self):
        while True:
            try:
                self.task = "Buying limiteds / looking for new ones"
                t0 = time.monotonic()

                for currentItem in self.items:
                    if not currentItem.isdigit():
                        raise Exception(f"Invalid limited ID: {currentItem}")

                    currentAccount = self.accounts[str(
                        random.randint(1, len(self.accounts)))]
                    response = r.post("https://catalog.roblox.com/v1/catalog/items/details",
                                      json={
                                          "items": [{"itemType": "Asset", "id": int(currentItem)}]},
                                      headers={
                                          "x-csrf-token": currentAccount['xcsrf_token'], 'Accept': "application/json"},
                                      cookies={".ROBLOSECURITY": currentAccount["cookie"]}, verify=True)
                    response.raise_for_status()
                    json_response = json.loads(response.text)['data'][0]
                    if json_response.get("priceStatus") != "Off Sale" and 0 if json_response.get('unitsAvailableForConsumption') is None else json_response.get('unitsAvailableForConsumption') > 0:
                        productid_response = r.post("https://apis.roblox.com/marketplace-items/v1/items/details",
                                                    json={"itemIds": [
                                                        json_response["collectibleItemId"]]},
                                                    headers={
                                                        "x-csrf-token": currentAccount["xcsrf_token"], 'Accept': "application/json"},
                                                    cookies={".ROBLOSECURITY": currentAccount["cookie"]}, verify=True)
                        productid_response.raise_for_status()
                        productid_data = json.loads(productid_response.text)[0]

                        for i in self.accounts:
                            await self.buyItem(item_id=json_response["collectibleItemId"], price=json_response['price'], user_id=self.accounts[i]["id"], creator_id=json_response['creatorTargetId'], product_id=productid_data['collectibleProductId'], cookie=self.accounts[i]["cookie"], x_token=self.accounts[i]["xcsrf_token"])

                    t1 = time.monotonic()
                    self.last_time = round(t1 - t0, 3)

            except r.exceptions.RequestException as e:
                print(f'Connection error: {e} with item: {currentItem}')
                self.errors += 1
            except aiohttp.ContentTypeError as e:
                print(f'Content type error: {e}')
                self.errors += 1
            except aiohttp.ClientResponseError as e:
                print(f'Response error: {e}')
                self.errors += 1
            except aiohttp.client_exceptions.ClientResponseError as e:
                print(f"Response Error: {e}")
            finally:
                self.checks += 1
                await asyncio.sleep(1)

    async def start(self):
        coroutines = []
        coroutines.append(self.snipeID())
        coroutines.append(self.getLimiteds())
        coroutines.append(self.Update())
        # coroutines.append(self.proxyStart())
        await asyncio.gather(*coroutines)

    async def Update(self):
        firstExec = True
        while True:
            if not await self._checkXCSRF():
                raise Exception("Could not generate X_CSRF_TOKEN")
            os.system(self.clear)

            self._UI()
            if firstExec:
                delay = 1
                firstExec = False
            else:
                delay = 10
            await asyncio.sleep(delay)


os.system("cls" if os.name == "nt" else "clear")


class Menu():
    def showMenu(self, getOption):
        print('Select an option:')
        for key in sorted(getOption):
            print(f' {key}) {getOption[key][0]}')

    def readOption(self, getOption):
        while (a := input('Option: ')) not in getOption:
            print('Incorrect option, try again.')
        return a

    def execOption(self, opt, getOption):
        getOption[opt][1]()

    def genMenu(self, getOption, exitOpt):
        opt = None
        while opt != exitOpt:
            self.showMenu(getOption)
            opt = self.readOption(getOption)
            self.execOption(opt, getOption)
            print()

    def mainMenu(self):
        getOption = {
            '1': ('Start the bot', self.runBot),
            '2': ('Exit', self.quitProgram)
        }
        self.genMenu(getOption, '2')

    def runBot(self):
        UGCatcher()

    def quitProgram(self):
        print('Exiting...')


class LoadingBar():
    def bar(self):
        self.colors = ['\033[31m', '\033[33m', '\033[32m',
                       '\033[36m', '\033[34m', '\033[35m']
        self.loadBar = 50
        self.animSpeed = 0.05

        for i in range(self.loadBar + 1):
            if i == self.loadBar:
                getColor = len(self.colors) - 1
                self.percent = 100

                print('\r' + 'Loading UGCatcher ' + self.colors[getColor] + '| ' + '█' * i + ' ' * (
                    self.loadBar - i) + f' | {self.percent}%\033[0m', end='')
                print("\nUGCatcher loaded successfully!\n\n")

                time.sleep(2)

                menu = Menu()
                menu.mainMenu()
            else:
                getColor = int(i / (self.loadBar / len(self.colors)))
                self.percent = int(i / self.loadBar * 100)

                print('\r' + 'Loading UGCatcher ' + self.colors[getColor] + '| ' + '█' * i + ' ' * (
                    self.loadBar - i) + f' | {self.percent}%\033[0m', end='')
                time.sleep(self.animSpeed)


if __name__ == '__main__':
    load = LoadingBar()
    load.bar()
