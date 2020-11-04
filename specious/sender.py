import yagmail

# 链接邮箱服务器
yag = yagmail.SMTP(
    user="chaochao.wu@hand-china.com",
    host='smtphm.qiye.163.com',
    port=465,
    smtp_ssl=True)

html = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>这是一个测试邮件</h1>
    <img src="http://www.china-7.net/uploads/14770342827041.jpg" alt="">
</body>
</html>
"""

# 邮箱正文
contents = [html]

# 发送邮件
yag.send('chaochao.wu@hand-china.com', '测试', contents)
# 关闭
yag.close()
