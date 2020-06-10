from datetime import datetime
from datetime import timedelta

#funcao para pegar a data atual
def data_servidor():
    dia_servidor = datetime.now()
    return dia_servidor


#funcao para pegar a data do proximo agendamento
def proxima_data_de_agendamento():
    data_atual = datetime.now()
    proxima_data = data_atual + timedelta(days=1, hours=-int(data_atual.strftime('%H')) + 3,
                                        minutes=-int(data_atual.strftime('%M')),
                                        seconds=-int(data_atual.strftime('%S')))

    return proxima_data

#funcao para pegar o dia que realiza o processo as 00:00 horas
def comeco_dia(n):
    dia = data_servidor()
    comeco_dia = dia - timedelta(days=1, hours=int(dia.strftime('%H')),
                                 minutes=int(dia.strftime('%M')),
                                 seconds=int(dia.strftime('%S')),
                                 microseconds=int(dia.strftime('%f')))
    if n==1:
        return comeco_dia
    else:
        return comeco_dia.strftime("%Y-%m-%d")

#funcao para pegar o fim do dia
def fim_dia():
    dia = comeco_dia(1)
    fim_dia = dia + timedelta(hours=23,
                                 minutes=59,
                                 seconds=59)
    return fim_dia



