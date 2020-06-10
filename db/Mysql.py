import mysql.connector

class Mysql:
    # função construtora
    def __init__(self):
        self.__mysql_connection = None

    # Função para iniciar conexao
    def conexao(self):
        self.__mysql_connection = mysql.connector.connect(host='mysql-dev.vrg.ftrack.me',
                                                          user='ftrk_site',
                                                          password='yh7GzoFT',
                                                          database='rastreador')

    # Função para gravar no banco
    def gravar(self,dado):
        cursor = self.__mysql_connection.cursor()

        sql = """  
            INSERT INTO ras_relatorio_evento
            (ras_rle_id_veiculo ,ras_rle_contador ,ras_rle_data ,ras_rle_data_coleta ,ras_rle_id_indice) 
            VALUES {}
            """
        cursor.execute(sql.format(dado))
        self.__mysql_connection.commit()
        cursor.close()

    # Verificar se ja passou o horario do prox agendamento caso passou executar programa
    def verificar_agendamento(self):
        cursor = self.__mysql_connection.cursor()

        sql = """SELECT sva_data_prox_exec as data_de_execucao
                    FROM servicos_agendados 
                    WHERE sva_id = 24
                    LIMIT 1
        """

        cursor.execute(sql)
        dados = cursor.fetchone()
        cursor.close()
        return dados



    # marcar proximo agendamento
    def proximo_agendamento(self,data_servidor,data_agendamento):
        cursor = self.__mysql_connection.cursor()
        sql = """
                UPDATE servicos_agendados
                SET sva_data_ult_exec = %s ,sva_data_prox_exec = %s
                WHERE sva_id = 24;
        """

        cursor.execute(sql, (data_servidor,data_agendamento))
        self.__mysql_connection.commit()
        cursor.close()

    # contar a quantidade de posicoes de cada veiculo
    def get_positions(self,comeco_dia,fim_dia):
        cursor = self.__mysql_connection.cursor()

        sql = """  SELECT ras_eal_id_veiculo,ras_eal_id_indice,COUNT(DISTINCT ras_eal_id) as quantidade_de_posiçoes
                    FROM ras_eventos_alertas3 
                    where ras_eal_data_alerta  BETWEEN %s and %s
                    GROUP BY ras_eal_id_veiculo,ras_eal_id_indice;                  
            """

        cursor.execute(sql,(comeco_dia, fim_dia))
        dados = cursor.fetchall()
        cursor.close()
        return dados

    #funcao para fechar a conexao
    def close(self):
        self.__mysql_connection.close()

