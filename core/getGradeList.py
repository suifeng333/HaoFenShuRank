from getLogin import getLogin
import requests


class GradeList:
    def __init__(self, loginName, password, roleType, rememberMe):
        self.login = getLogin(loginName, password, roleType, rememberMe)
        self.loginInformation = self.login.getLoginInformation()

    def getLoginCookies(self):
        if 'msg' in self.loginInformation and self.loginInformation['msg'] == "登录成功":
            data = self.loginInformation.get('data', {})
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
        checkCookies = self.getLoginCookies()
        if checkCookies:
            headers.update(checkCookies)
            response = requests.post(url, headers=headers)
            response.raise_for_status()
            gradeList = response.json()
            exam = gradeList.get('data', {}).get('list', [])
            examsInfo = []
            for i in exam:
                examClassName = i.get('className')
                examName = i.get('name')
                examScore = i.get('scoreS')
                examClassRankLevel = i.get('classRankPart')
                examClassRank = i.get('classRank')
                examClassDefeatRatio = i.get('classDefeatRatio')
                examGradeRankLevel = i.get('gradeRankPart')
                examGradeRank = i.get('gradeRank')
                examGradeDefeatRatio = i.get('gradeDefeatRatio')
                examInfo = {
                    'examClassName': examClassName,
                    'examName': examName,
                    'examScore': examScore,
                    'examClassRankLevel': examClassRankLevel,
                    'examClassRank': examClassRank,
                    'examClassDefeatRatio': examClassDefeatRatio,
                    'examGradeRankLevel': examGradeRankLevel,
                    'examGradeRank': examGradeRank,
                    'examGradeDefeatRatio': examGradeDefeatRatio
                }
                examsInfo.append(examInfo)
            return examsInfo
        else:
            return None
