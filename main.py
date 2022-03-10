from serpapi import GoogleSearch
from dotenv import dotenv_values
import os, json

import webbrowser as wb

config = dotenv_values(".env")

def save_to_file(data):
    with open("data.html", "w", encoding="utf8") as file:
        file.write("<html><head><title>Naver Results</title></head><body>")
        file.write("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3' crossorigin='anonymous'>")
        file.write("<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p' crossorigin='anonymous'></script>")

        file.write("<div class='col-md4 col-lg-4 order-md-last'>")
        file.write("<h4 class='d-flex justify-content-between align-items-center mb-3'>")
        file.write("<span class='text-primary'>Google search results</span>")
        file.write("</h4>")
        file.write("<ul class='list-group mb-3'>")
        
        for tag in data:

            file.write("<li class='list-group-item d-flex justify-content-between 1h-sm>")               
            file.write("<div>")
            file.write("<span class='my-0'>{}</span>".format(tag["position"]))
            file.write("<h6 class='my-1'>{}</h6>".format(tag["title"]))
            file.write("<small class='text-muted'>{}</small>".format(tag["link"]))
            #file.write("<p>{}</p>".format(tag["snippet"]))
           
            file.write("</div>")
            file.write("</li>")
        file.write("</ul>")
        file.write("</div>")
        file.write("</body></html>")
        file.close()
    
    with open("data.json", "w", encoding="utf8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.close()

def serpapi_get_naver_organic_results_google():
    params = {
        "api_key": config.get("API_KEY"),
        "engine":"google",
        "q":"zamaca",
        "location_requested":"Community of Madrid, Spain",
        "location_used":"Community of Madrid,Spain",
        "google_domain":"google.es",
        "hl":"es",
        "gl":"es",
        "device":"desktop",
        "num":50
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    data = []

    for result in results["organic_results"]:
        data.append({
            "position": result["position"],
            "title": result["title"],
            "link": result["link"],
            "displayed_link": result["displayed_link"],
            "snippet": result["snippet"]
        })

    save_to_file(data)

def serpapi_get_naver_organic_results_bing():
    params = {
        "api_key": config.get("API_KEY"),
        "engine":"bing",
        "q":"zamaca",
        "location_requested":"Community of Madrid, Spain",
        "location_used":"Community of Madrid,Spain",
        "google_domain":"google.es",
        "hl":"es",
        "gl":"es",
        "device":"desktop",
        "num":50
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    data = []

    for result in results["organic_results"]:
        data.append({
            "position": result["position"],
            "title": result["title"],
            "link": result["link"],
            "displayed_link": result["displayed_link"],
            "snippet": result["snippet"]
        })

    save_to_file(data)

def serpapi_get_naver_organic_results_youtube():
    params = {
    "engine": "youtube",
    "search_query": "zamaca",
    "api_key": config.get("API_KEY"),
    "location_requested":"Community of Madrid, Spain",
    "location_used":"Community of Madrid,Spain",
    "google_domain":"google.es",
    "hl":"es",
    "gl":"es",
    "device":"desktop",
    "num":50
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    movie_results = results['movie_results']

def serpapi_get_naver_organic_results_twitter():
    params = {
    "q": "Naval twitter",
    "location": "Austin,Texas,United States",
    "hl": "en",
    "gl": "us",
    "api_key": config.get("API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    twitter_results = results['twitter_results']

serpapi_get_naver_organic_results_bing()

wb.open_new_tab('file://' + os.path.realpath("data.html"))