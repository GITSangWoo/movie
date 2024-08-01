from mov.api.call import gen_url, req, get_key,req2list,list2df,save2df,echo,apply_type2df
import pandas as pd 


def test_apply_type2df():
    df= apply_type2df()
    assert isinstance(df,pd.DataFrame)
    assert str(df['rnum'].dtype) in ['int64'] 
    assert str(df['rank'].dtype) in ['int64'] 
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']
    for i in num_cols:
        # assert df[i].dtype in ['int64','float64']
        df[num_cols] = df[num_cols].apply(pd.to_numeric)


def test_echo():
    df=echo("사람 살려요")
    # print(df)
    assert True



def test_savd2df():
    d = {"repNationCd" : "K"}
    df=save2df(url_param = d)
    print(df)
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
    # url = gen_url()
    #assert "http" in url
    # assert "kobis" in url
    # d = {"multiMovieYn" : "N"}
    # d = {"multiMovieYn" : "Y"}
    s = {"repNationCd" : "K"}
    url = gen_url(url_param=s)

def test_req():
    code, data = req()
    assert code == 200
    
    code,data = req('20230101')
    assert code == 200
