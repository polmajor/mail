import json
import smtplib
import datetime

def initialize(login, pss):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(login,pss)
    
    return server
    
def send_email(conn, f, t, m):
    date = str(datetime.datetime.today())
    r = conn.sendmail(f,t,m)
    conn.quit()
    
    return r    