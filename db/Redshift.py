import psycopg2

class Redshift:
    def __init__(self):
        self.__redshift_connection = None

    def conexao(self):
        self.__redshift_connection = psycopg2.connect(user="",
                                                      password="",
                                                      host="",
                                                      port="",
                                                      database="")


    def get_positions(self, comeco_dia, fim_dia):
        redshift_cursor = self.__redshift_connection.cursor()

        query = """SELECT id_ativo,id_indice,COUNT(DISTINCT id) as quantidade_de_posiçoes 
                            FROM tbl_tracking 
                            WHERE (dt_gps BETWEEN %s AND %s)
                            GROUP BY id_ativo,id_indice """

        redshift_cursor.execute(query,(comeco_dia, fim_dia,))
        todas_linhas = redshift_cursor.fetchall()
        redshift_cursor.close()
        return todas_linhas

    def close(self):
        self.__redshift_connection.close()

"""
MAIN
    redshift = banco_redshift.Redshift()
    registros = redshift.get_positions(comeco_dia(1), fim_dia())
    ras_rle_data = comeco_dia(0)
    data_coleta = data_servidor()
    s = ""
    for row in registros:
        s += '({} ,{} ,"{}","{}" ,{}),'.format(row[0],row[2],ras_rle_data,data_coleta,row[1])
    s = s[0:-1]
    redshift.close()
    
"""