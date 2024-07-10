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
        return token
    else:
        return None
