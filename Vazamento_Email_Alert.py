import pandas as pd
import numpy  as np

#LISTA COM TODOS OS CONDOMINIOS E EMAILS
df=pd.read_csv('Vazamentos.csv',sep=',')
df=df.set_index('NAME_SYSTEM')
df=df[df.ENVIA_EMAIL==1]

# LISTA DE CLIENTES SEM VAZAMENTO
dt_sem_vaz=df[df.VAZAMENTO!=1]
dt_sem_vaz = dt_sem_vaz[['ENVIA_EMAIL','EMAIL','EMAIL_RESPONSAVEL']].copy() 

# LISTA DE CLIENTES COM VAZAMENTO
dt_vaz = df[df.VAZAMENTO==1]
dt_vaz=dt_vaz.drop(columns=['VAZAMENTO']).drop_duplicates()

df2= dt_vaz.drop(columns=['DATA','CONSUMO_MADRUGADA']).drop_duplicates()
for data in dt_vaz.DATA.unique():   
    aux=dt_vaz[dt_vaz.DATA==data]['CONSUMO_MADRUGADA']
    data='Consumo Madrugada em '+data
    df2.insert(loc=len(df2.columns), value=aux.values,column=data)
dt_vaz=df2

from datetime import datetime, timedelta
dt_ini=datetime.today().strftime('%d/%m/%Y')
dt_fim= datetime.today() - timedelta(days=7)
dt_fim= dt_fim.strftime('%d/%m/%Y')

def Envia_Email(de,para,assunto,html):

    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = assunto
    msg['From'] = de
    msg['To'] = ", ".join(para)
    msg['Cc'] = ', '.join(cc)

    # Create the body of the message (a plain-text and an HTML version).

    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('my_email_server@gmail.com', 25)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(de, (para+cc), msg.as_string())
    s.quit()

de ="my_email@gmail"
cc = ["some_email@gmail.com.br"]

# ENVIO DE EMAIL SEM VAZAMENTO
for name in dt_sem_vaz.index.unique():
    para=dt_sem_vaz[dt_sem_vaz.index==name]['EMAIL'].to_list()
    resp=dt_sem_vaz[dt_sem_vaz.index==name]['EMAIL_RESPONSAVEL'].drop_duplicates().to_list()
    para=para+resp
    html='''Prezado, <br> Durante a semana do dia {} a {}, o condomínio {} <br> não apresentou nenhuma
    suspeita de vazamento em suas unidades consumidoras. <br><br>
    Atenciosamente,<br> My Team <br><br>'''.format(dt_fim,dt_ini,name)
    
    assunto = "Subject - Condomino {} - Suspeita de vazamento".format(name)
    Envia_Email(de,para,assunto,html)
    
# ENVIO DE EMAIL COM VAZAMENTO

for name in dt_vaz.index.unique():
    print("For Externo: "+name)
    para=dt_vaz[dt_vaz.index==name]['EMAIL'].to_list()
    resp=dt_vaz[dt_vaz.index==name]['EMAIL_RESPONSAVEL'].drop_duplicates().to_list()
    para=para+resp
    dt=dt_vaz.drop(columns=['EMAIL','ENVIA_EMAIL','EMAIL_RESPONSAVEL']).drop_duplicates()
    mensagem ='''
    Prezado, <br> Durante a semana do dia {} a {}, foi constatado que o condomínio {} <br> possui suspeita
    de vazamento em suas unidades consumidoras conforme tabela abaixo. <br><br>
    '''.format(dt_fim,dt_ini,name)
    html=mensagem+dt[dt.index== name].to_html(index=False)+"<br>Atenciosamente,<br> My Team<br>" 
    
    assunto = "Subject - Condomino {} - Suspeita de vazamento".format(name)
    
    Envia_Email(de,para,assunto,html)
