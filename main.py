import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def check_link(url):
    result = {
        "url": url,
        "is_alive": False,
        "status": None,
        "rel": "dofollow",
    }
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
            async with session.get(url, allow_redirects=True) as resp:
                result["status"] = resp.status
                result["is_alive"] = 200 <= resp.status < 400
                text = await resp.text(errors='ignore')
                soup = BeautifulSoup(text, "html.parser")
                a = soup.find("a", href=True)
                if a and a.has_attr("rel"):
                    rel_vals = [r.lower() for r in a["rel"].split()]
                    if "nofollow" in rel_vals:
                        result['rel'] = "nofollow"
    except Exception as e:
        result["error"] = str(e)
    return result

async def main():
    info = await check_link("https://www.google.com/")
    print(info)

if __name__ == "__main__":
    asyncio.run(main())
