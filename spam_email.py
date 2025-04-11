import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_email(sender_email, sender_password, recipient_list, subject, body, smtp_server, smtp_port):
    try:
        # Настройка сообщения
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(recipient_list)
        msg['Subject'] = Header(subject, 'utf-8')
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Подключение к SMTP-серверу
        server = smtplib.SMTP(smtp_server, smtp_port)

        server.starttls()  # Соединение
        server.login(sender_email, sender_password) # Подключение
        
        # Отправка письма
        for recipient in recipient_list:
            server.sendmail(sender_email, recipient, msg.as_string())
        
        server.quit()
        print("Сообщение отправлено")
    except Exception as e:
        print(f"Error: {e}")

# Пример использования
if __name__ == "__main__":
    sender_email = "vados020676@gmail.com"
    sender_password = "omjk vegn djyl usri"
    recipient_list = ['aleksejabdeev11@gmail.com']
    subject = "Привет это рассылка"
    body = "сообщение"
    smtp_server = "smtp.gmail.com"  # Например, для Gmail
    smtp_port = 587
    
    send_email(sender_email, sender_password, recipient_list, subject, body, smtp_server, smtp_port)