# coding:utf -8
# 163邮箱需要开启smtp服务， 拿到授权密码
# 代码在自己电脑运行出现问题，UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd0 in position 2:
#                          invalid continuation byte
# 在服务器上没有报错

import smtplib
from email.mime.text import MIMEText


def send_email(from_user_name, from_address, password, to_address_list, subject, content, smtp_host):
    """
    :param from_user_name: str> 发送邮箱的用户名
    :param from_address: str> 发送邮箱地址
    :param password: str> 发送邮箱密码
    :param to_address_list: list> 接收邮箱地址
    :param subject: str> 邮件主题
    :param content: str> 邮件内容
    :param smtp_host: str> smtp服务器地址
    :return send_result: bool > 邮件是否发送成功
    """
    smtp = smtplib.SMTP_SSL(smtp_host, 465)
    smtp.ehlo(smtp_host)
    smtp.login(from_address, password)
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['From'] = '%s<%s>' % (from_user_name, from_address)
    msg['To'] = ",".join(to_address_list)
    msg['Subject'] = subject

    send_result = False
    try:
        smtp.sendmail(from_address, to_address_list, msg.as_string())
        send_result = True
        print("send seccussfully")
    except smtplib.SMTPException as e:
        print(str(e))
        send_result = False
    finally:
        smtp.quit()
        return send_result


if __name__ == '__main__':
    send_email(
        from_user_name='东东',
        from_address='**@163.com',
        password='***',
        to_address_list=['**@qq.com'], #可以写多个
        subject='邮件主题',
        content='hello,this is an email sended by python',
        smtp_host='smtp.163.com'
    )