# -*- coding: utf-8 -*-
"""Render the 1200x630 social share images (assets/ogp.png / ogp-en.png)."""
import asyncio, os
from playwright.async_api import async_playwright
from gen import ART

ROOT = os.path.dirname(os.path.abspath(__file__))

TPL = """<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#f6f3ec;
  font-family:"Noto Serif CJK JP","Noto Serif JP",serif;color:#2b2a26;
  display:flex;flex-direction:column;justify-content:center;
  padding:0 90px;position:relative;overflow:hidden}}
body::after{{content:"";position:absolute;inset:26px;border:1px solid #d9d2c2}}
.kick{{font-family:"Noto Sans CJK JP",sans-serif;font-size:15px;letter-spacing:.44em;
  color:#b0965a;margin-bottom:26px}}
h1{{font-size:{fs}px;letter-spacing:{ls};font-weight:500;line-height:1.35}}
.rule{{width:64px;height:1px;background:#b0965a;margin:30px 0 26px}}
p{{font-family:"Noto Sans CJK JP",sans-serif;font-size:19px;line-height:2;
  color:#5a564c;letter-spacing:.05em;max-width:620px}}
.art{{position:absolute;right:74px;bottom:54px;width:400px;opacity:.9}}
.art svg{{width:100%;height:auto}}
</style>
<p class="kick">{kick}</p>
<h1>{title}</h1>
<div class="rule"></div>
<p>{sub}</p>
<div class="art">{art}</div>
"""

PAGES = [
    ("assets/ogp.png", dict(
        kick="YUSANDO ANTIQUE GALLERY", fs=52, ls=".14em",
        title="悠三堂古美術ギャラリー",
        sub="ときめきやワクワクでお茶道具を選びたい。<br>初心者でも楽しみやすい、均一価格の中古お茶道具ポータルです。")),
    ("assets/ogp-en.png", dict(
        kick="FLAT-PRICE TEA UTENSILS", fs=54, ls=".05em",
        title="Yusando<br>Antique Gallery",
        sub="A flat-price portal for pre-loved Japanese tea utensils —<br>chosen for delight, easy for beginners.")),
]


async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        ctx = await b.new_context(viewport={"width": 1200, "height": 630},
                                  device_scale_factor=1)
        pg = await ctx.new_page()
        for out, kw in PAGES:
            await pg.set_content(TPL.format(art=ART["chawan"], **kw))
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(ROOT, out))
            print("wrote", out)
        await b.close()

asyncio.run(main())
