from getLogin import user
import requests

loginName = None
password = None
roleType = None
rememberMe = 2

loginInformation = user.getLoginInformation()


def getLoginCookies(self):
    if 'msg' in loginInformation and loginInformation['msg'] == "登录成功":
        data = loginInformation.get('data', {})
        token = data.get('token')
        return {'Cookie': f'{token}'}
    else:
        return None


def getGradeList(self):
    url = "https://hfs-be.yunxiao.com/v3/exam/list?start=0&limit=10"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.0.0 Safari/537.36',
        'Origin': 'https://www.haofenshu.com',
        'Referer': 'https://www.haofenshu.com/'
    }
    gradeList = requests.post(url, headers=headers, data=getLoginCookies()).json()
