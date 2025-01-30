from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


msg = MIMEMultipart()
texto = "EMAIL Hackeado com SUCESS"

#parâmetros
senha = "S@nts163"
msg['From'] = "otaviosatago@gmail.com"
msg['To'] = "robblox7@gmail.com"
msg['Subject'] = "HACKEADOO"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))


#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')