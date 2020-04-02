import json
import smtplib


def initialize(login, pss):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    conn.login(login,pss)
    
def send_email(conn, f, t, m):
    date = str(datetime.datetime.today())
    conn.sendmail(f,t,m)
    conn.quit()