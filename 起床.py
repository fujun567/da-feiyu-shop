# -*- coding: utf-8 -*-
"""
起床提醒邮件 —— 单次发送脚本
配合 Windows 任务计划程序：每天 07:50 触发一次本脚本
所有敏感信息（服务器、账号、授权码）均从环境变量读取，不硬编码。
"""
import os
import ssl
import smtplib
from email.message import EmailMessage
from email.utils import formatdate


def env(name, default=None, required=False):
    v = os.environ.get(name, default)
    if required and not v:
        raise SystemExit(f"[配置错误] 缺少环境变量：{name}")
    return v


def main():
    host = env("SMTP_HOST", required=True)          # 例：smtp.qq.com
    port = int(env("SMTP_PORT", "465"))             # SSL 常用 465
    user = env("SMTP_USER", required=True)          # 你的邮箱
    password = env("SMTP_PASS", required=True)      # 授权码（不是登录密码！）
    to_addr = env("MAIL_TO", user)                  # 收件人，默认发给自己
    use_ssl = env("SMTP_SSL", "1") == "1"           # 1=SSL，0=STARTTLS

    subject = "起床啦！☀️ 新的一天开始咯"
    body = (
        "早上好，符均！\n\n"
        "闹钟响啦，该起床啦 🛏️\n"
        "记得洗漱、吃早饭，元气满满地开始新的一天。\n\n"
        "—— 来自你的自动提醒助手"
    )

    msg = EmailMessage()
    msg["From"] = user
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg.set_content(body)

    try:
        if use_ssl:
            ctx = ssl.create_default_context()
            with smtplib.SMTP_SSL(host, port, context=ctx, timeout=30) as s:
                s.login(user, password)
                s.send_message(msg)
        else:
            with smtplib.SMTP(host, port, timeout=30) as s:
                s.ehlo()
                s.starttls(context=ssl.create_default_context())
                s.ehlo()
                s.login(user, password)
                s.send_message(msg)
        print(f"[OK] 邮件已发送 -> {to_addr}")
    except Exception as e:
        print(f"[FAIL] 发送失败：{e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()