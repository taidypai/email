# send_email

Мой код осуществляет рассылку по почте, чтобы все работало исправно вам ножно получить пароль для удаленного доступа к почте отправителя. 

Пример пароля **** **** **** ****

# Получение пароля
Получить пароль вы можете в настройках аккаунта google. Вбиваете в адресную строку " Пароли приложений gmail " и переходите в первоисточник, следуете инструкции на странице, подключаете впн и входите в свой акаунт по ссылке на странице. 

После получения пароля добавляете его в переменную

    sender_password = ""

Также добавляем Ссписок получателей, и сзаполняем заголовок с текстом сообщения

    recipient_list = [] # Список получателей
    subject = "" # Заголовок
    body = "" # Текст
  
