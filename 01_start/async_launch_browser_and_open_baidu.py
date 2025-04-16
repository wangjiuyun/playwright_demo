import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

# playwright支持同步和异步
async def open_page(playwright,url):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto(url)
    print(await page.title())
    await browser.close()

# 同时打开百度，必应，搜狗
async def main():
    async with async_playwright() as playwright:
        tasks = [
            open_page(playwright,"https://www.baidu.com"),
            open_page(playwright,"https://www.bing.com"),
            open_page(playwright,"https://www.sogou.com"),
        ]
        #关键，并发执行
        await asyncio.gather(*tasks)
asyncio.run(main())

print("开启简单的方式实现异步：")
# 也可以用with语句来实现
playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.baidu.com")

browser.close()
playwright.stop()