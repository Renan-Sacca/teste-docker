import time
from db import Mysql
from data.config_horas import *
#from db.banco_redshift import
mysql = Mysql.Mysql()
while True:

    mysql.conexao()
    verificado = mysql.verificar_agendamento()

    if datetime.timestamp(data_servidor()) >= datetime.timestamp(verificado[0]):

        mysql.proximo_agendamento(data_servidor(), proxima_data_de_agendamento())
        print("Agendamento marcado")

        dados_coleta = mysql.get_positions(comeco_dia(1), fim_dia())
        ras_rle_data = comeco_dia(0)
        data_coleta = data_servidor()
        
        s = ""
        for (ras_eal_id_veiculo, ras_eal_id_indice, quantidade_de_posiçoes) in dados_coleta:
            s += '({} ,{} ,"{}","{}" ,{}),'.format(ras_eal_id_veiculo,quantidade_de_posiçoes,ras_rle_data,data_coleta,ras_eal_id_indice)
        s = s[0:-1]
        print(s)

        if s != "":
            mysql.gravar(s)
            print("Dados gravados")

    mysql.close()
    print("...")
    time.sleep(3600)




