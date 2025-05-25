import httpx
from selectolax.parser import HTMLParser
import json

# GET WEBSITE HTML STRUCTURE
def GetHTMLStructure(url:str) -> str:
    # Mimic a real browser and avoid being blocked by the website
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

    # Get HTML structure for the website
    response = httpx.get(url, headers=headers)

    if response.status_code == 200:
        # Return website html
        return response.text
    else:
        # Print errors
        print(f"Error: Received status code {response.status_code} for URL: {url}")
        print(f"Response content: {response.text}")
        # Return Empty data
        return ""

# FETCH ADS/ITEMS DATA FROM THE HTML
def ParseStructure(structure:str) -> dict:
    # Create a json structure
    ads = {}

    # A check for empty response
    if structure == "":
        return ads

    # Attach parser
    parser = HTMLParser(structure)

    # Fetch all the li tags that hold the ads/item data
    elements = parser.css('li[data-aut-id^="itemBox"]')

    ads["results"] = len(elements)
    ads["data"] = []

    # Fetch the li data one by one
    count = 0
    for el in elements:
        title = el.css_first('[data-aut-id="itemTitle"]')
        price = el.css_first('[data-aut-id="itemPrice"]')
        location = el.css_first('[data-aut-id="item-location"]')
        details = el.css_first('[data-aut-id="itemDetails"]')

        price = price.text(strip=True) if price else None,
        details = details.text(strip=True) if details else None,
        title = title.text(strip=True) if title else None,
        location = location.text(strip=True) if location else None,

        ads["data"].append({"title":title[0], "price":price[0], "location":location[0], "description":details[0]})
        count+=1

    # Return structured data
    return ads

# COPY THE RESULTS TO A FILE
def ResultsFile(data:dict, filename:str) -> None:
    output_file = filename
    with open(output_file, "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Data Copied to {output_file}")


# PROGRAM ENTRY POINT
if __name__ == "__main__":
    url = "https://www.olx.in/items/q-car-cover"
    html_structure = GetHTMLStructure(url)
    ads_data = ParseStructure(html_structure)
    ResultsFile(ads_data, "results.json")