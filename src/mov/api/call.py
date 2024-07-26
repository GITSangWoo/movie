def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "d84851257c3a3b62cddfe861c832f8f5"
    url = f"{base_url}?key={key}&targetDt={dt}"  
    print(url)

