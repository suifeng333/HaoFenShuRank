import requests
from requests import RequestException


class getLogin():
    def __init__(self, loginName, password, roleType, rememberMe):
        self.loginName = loginName
        self.password = password
        self.roleType = roleType
        self.rememberMe = rememberMe

    def checkRoleType(self):
        if self.roleType == "1":
            return "学生登录"
        elif self.roleType == "2":
            return "家长登录"
        else:
            return "未知"

    def getLoginInformation(self):
        url = "https://hfs-be.yunxiao.com/v2/users/sessions"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/101.0.0.0 Safari/537.36',
            'Origin': 'https://www.haofenshu.com',
            'Referer': 'https://www.haofenshu.com/'
        }
        data = {
            "loginName": self.loginName,
            "password": self.password,
            "roleType": self.roleType,
            "rememberMe": self.rememberMe
        }
        try:
            login = requests.post(url, headers=headers, data=data)
            loginJson = login.json()
            login.raise_for_status()
            if 'msg' in loginJson and loginJson['msg'] == '登录成功':
                return loginJson
            elif 'msg' in loginJson and loginJson['msg'] == '密码错误':
                return print("密码错误")
        except RequestException as e:
            print(f"在获取登录信息时发生错误：{e}")
            return None
