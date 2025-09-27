from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

def crawl_comments(url):
    all_comments = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True nếu không cần thấy trình duyệt
        page = browser.new_page()
        page.goto(url, timeout=60000)

        # Đợi trang load lần đầu
        page.wait_for_selector( 
        ".my-4.text-left.text-textOnWhitePrimary.b2-semibold.mb\\:hidden.pc\\:h6-semibold", 
        timeout=30000)
        while True:

            try:
                popup_close = page.locator("button:has-text('Để sau')")
                if popup_close.is_visible():
                    popup_close.click()
                    time.sleep(1)
            except:
                pass

            # Lấy toàn bộ HTML sau khi render
            html = page.content()
            soup = BeautifulSoup(html, "html5lib")

            # Tìm các comment
            comments = soup.find_all('span', class_='false break-all')
            # print(comments)
            for c in comments:
                text = c.get_text(strip=True)
                if text:
                    all_comments.append(text)

            # Thử tìm nút next còn khả dụng
            next_button = page.locator(
            "li.Pagination_pagerItemNext__N2sCi:not(.Pagination_pagerItemNextDisabled__EV0cb)")
            if next_button.count() > 0:
                next_button.click()
                time.sleep(2)
            else:
                break


        # browser.close()

    return all_comments

def save_comments(comments, filename="comment.csv"):
    # Tạo DataFrame từ danh sách comment
    df = pd.DataFrame([{"Label": "", "Content": c} for c in comments])

    # Nếu file chưa tồn tại thì ghi kèm header
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False, encoding="utf-8-sig")
    else:
        # Nếu đã tồn tại thì append, không ghi header
        df.to_csv(filename, mode="a", index=False, header=False, encoding="utf-8-sig")

products = [
    {'name':'tivi','items':['lg-smart-tivi-4k-55-inch-55nano81tsa',
    'samsung-smart-tv-crystal-uhd-43-inch-4k-ua43du7000', 
    'tivi-xiaomi-a-32-inch',
    'lg-smart-tivi-4k-43-inch-43uq7050psa',
    'xiaomi-google-tivi-4k-a-43-inch-f-2025-l43ma-afsea',
    'casper-smart-tv-43-inch-full-hd-43fgk610',
    'smart-tivi-samsung-crystal-uhd-4k-43-inch-ua43au7002',
    'xiaomi-google-tivi-qled-4k-55-inch-a-pro-55-2025-l55ma-ssea',
    'samsung-4k-55-inch-ua55du7700',
    'casper-android-tv-32-inch-hd-32hg5200',
    'vsp-android-tv-32-inch-hd-vua32auh01',
    'casper-smart-tv-32-inch-hd-32hgk610']},
    {'name':'dien-thoai','items':['iphone-13','iphone-14','iphone-15','iphone-16','iphone-17']},
    {'name':'may-tinh-xach-tay','items':['macbook-air-13-m4-2025-10cpu-8gpu-16gb-256gb',
                          'macbook-air-m2-13-2024-8cpu-8gpu-16gb-256gb',
                          'asus-vivobook-go-15-e1504ga-bq1141w-i3-n305',
                          'hp-14s-em0086au-r5-7520u',
                          'lenovo-gaming-loq-e-15iax9e-i5-12450hx-83lk0079vn',
                          'lenovo-ideapad-slim-3-14irh10-83k00008vn',
                          'asus-vivobook-go-15-e1504ga-bq1141w-i3-n305',
                          'macbook-air-m2-2023-15-inch',
                          'macbook-pro-14-2023-m3-pro-12-cpu-18-gpu-18gb-1tb',
                          'macbook-air-m2-13-inch-2022-8cpu-10gpu-16gb-256gb',
                          'hp-15-fd0083tu-i7-1355u',
                          'msi-creator-m16-b13ve-830vn-i7-13700h?sku=00881433',
                          'acer-swift-14-ai-sf14-51-75vp-ultra-7-258v',
                          'lenovo-gaming-legion-slim-5-16ahp9-r7-8845hs',
                          'lenovo-gaming-loq-15arp9-r5-7235hs-83jc00hyvn']},

]

for product in products:
    for i in product['items']:
        url = f'https://fptshop.com.vn/{product['name']}/{i}'
        comments = crawl_comments(url)
        save_comments(comments)
# print(f"✅ Tổng số comment lấy được: {len(comments)}")
# for c in comments[:10]:  # in thử 10 comment đầu
#     print("-", c)

# pd.DataFrame(comments).to_csv('500comment')