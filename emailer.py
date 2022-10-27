import datetime as dt
import smtplib    

MY_EMAIL = "corndogg821@yahoo.com"
MY_PASSWORD = "vaderT!m3vaderT!m"
x = "hELLO"
y = "Test"

def email(x, y):    
    now = dt.datetime.now()
    weekday = now.weekday()
    if weekday == 0 or weekday == 2:
        print(f"emailing {y} data")
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="emanfred821@gmail.com",
                msg=f"Subject:{y} Stats\n\n{x}"
            )
            connection.quit

email(x, y)