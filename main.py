import page

login_url = 'https://github.com/login'
login_session = 'https://github.com/session'
headInfo = {"Host": "github.com",
            "Connection": "keep-alive",
            "Origin": "https://github.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "https://github.com/",
            "Accept-Encoding": "gzip, deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
            }

if __name__ == '__main__':
    webPage = page.WebPage('github_cookie.txt')
    # con = webPage.getPage(login_url, headerInfo=headInfo)
    # obj = webPage.getHtml5(con)
    # form = obj.find('form')
    # inputs = form.find_all('input')
    # pdata = {
    #
    # }
    # for input in inputs:
    #     pdata[input.get('name')] = input.get('value')
    #     # print('---', input.get('name'), input.get('value'))
    #
    # pdata["login"] = "zswsdx@126.com"
    # pdata["password"] = "zswsdx12@"
    # print(pdata)
    # con = webPage.getPage(login_session, postData=pdata, headerInfo=headInfo)
    # obj = webPage.getHtml5(con)
    # r = obj.find('meta', content='zswsdx')
    # if r:
    #     webPage.saveCookie()
    # else:
    #     print('login error')
    #
    webPage.loadCookie()
    con = webPage.getPage(login_session)
    # print(con)
    con = webPage.getPage('https://github.com/zswsdx/demo')
    print(con)
