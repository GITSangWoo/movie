from mov.api.call import gen_url, req, get_key,req2list,list2df,save2df
import pandas as pd 

def test_savd2df():
    df=save2df(load_dt='20241231')
    assert True
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns



def test_list2df():
    df = list2df()
    assert isinstance(df, pd.DataFrame) 
    assert 'rnum' in df.columns
    assert 'rankOldAndNew' in df.columns
    assert 'salesChange' in df.columns
    

def test_req2list():
    l = req2list()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert  v['rnum'] == '1'

def test_비밀키숨기기():
    key = get_key()
    assert key


def test_gen_url():
    url = gen_url()
    assert "http" in url
    assert "kobis" in url

    url = gen_url("20241231")
    assert "20241231" in url

def test_req():
    code, data = req()
    assert code == 200
    
    code,data = req('20230101')
    assert code == 200
