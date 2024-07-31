import requests
import os
import pandas as pd 

def echo(yaho):
    return yaho

def apply_type2df(load_dt="20120101",path="~/tmp/test_parquet"):
    df=pd.read_parquet(f'{path}/load_dt={load_dt}')
    df['rnum']=pd.to_numeric(df['rnum'])
    df['rank']=pd.to_numeric(df['rank'])
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']
    for c in num_cols:
        df[c]=pd.to_numeric(df[c])

    #df[num_cols] = df[num_cols].apply(pd.to_numeric)    
    return df

def save2df(load_dt='20120101', url_param={}):
    # airflow 호출지점
    df = list2df(load_dt,url_param)
    # df에 load_dt 컬럼 추가 (조회 일자 YYYYMMDD 형식 으로)
    df['load_dt'] = f'{load_dt}' 
    print(df.head())
    # 아래 파일 저장시 load_dt 기준으로 파티셔닝 
    df.to_parquet('~/tmp/test_parquet/',partition_cols=['load_dt'])
    return df


def list2df(load_dt='20120101',url_param={}):
    l = req2list(load_dt,url_param)
    df =  pd.DataFrame(l)
    return df

def req2list(load_dt='20120101',url_param={})->list:
    _, data = req(load_dt,url_param)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l 

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(load_dt="20120101",url_param={}):
    # url = gen_url('20240720')
    url = gen_url(load_dt, url_param)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    # print(data)
    return code, data

def gen_url(dt="20120101", url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    for k, v in url_param.items():
        url = url + f'&{k}={v}'
    print(url)
    return url
