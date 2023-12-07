import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "omonnuloraimkulov@gmail.com"
# sender_password ni ozingiz emailingiz parolini yozmatsiz @rmkvlly shu telegramga yosez chuntirvoraman
sender_password = ""
receiver_email = "mominovsharif12@gmail.com"

subject = "Python orqali yozilgan xabar"
message = "Salom, bu Python orqali yozilgan xabar."


smtp_server = "smtp.domen.com"
smtp_port = 587  # Agar port 587 ishlayotgan bo'lsa

try:
    # SMTP serverga ulanish
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Xabar tuzilishi
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Xabar yuborish
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # SMTP serverni yopish
    server.quit()
    print("Xabar yuborildi!")

except Exception as e:
    print(f"Xatolik yuz berdi: {str(e)}")
