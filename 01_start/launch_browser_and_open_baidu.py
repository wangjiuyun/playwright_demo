from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 启动chromium浏览器
    browser = p.chromium.launch(headless=False)
    # 打开一个标签页
    page = browser.new_page()
    # 打开百度地址
    page.goto("https://www.baidu.com")
    # 打印当前页面title
    print(page.title())
    #关闭浏览器对象
    browser.close()