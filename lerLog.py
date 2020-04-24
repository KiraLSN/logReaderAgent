import pymysql
arquivo = open('log.txt', 'r')
#print(arquivo)




leitura = arquivo.readlines()
arquivo.close()
tamanho = len(leitura)
print(leitura)
print(tamanho)
i = 0
for x in leitura:
    vetor = x.split(',')
    imei = vetor[0]
    proxc = vetor[1]
    prox = vetor[2]
    datetime = vetor[3]
    imeiresult = imei.split('= ')
    proxcresult = proxc.split('=')
    proxresult = prox.split('=')
    datetimeresult = datetime.split('= ')

    if (proxcresult[1]=='F' or proxresult[1]=='F'):
        result = 'F'
    else:
        result = 'P'


    #LEITURA DAS FALHAS DO BANCO
    selectdb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="line-tests-db"
    )

    mycursor = selectdb.cursor()

    sql = "SELECT imei FROM  proximitySar WHERE result = 'F'"

    mycursor.execute(sql)

    resultado = mycursor.fetchall()

    # Mostra o resultado:
    print(len(resultado))
    if(len(resultado) > 0):

        for linha in resultado :
            print("IMEI")
            print(linha)
            if linha == imeiresult[1]:
                print("Update "+ linha)
            else:

                mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="line-tests-db"
                )

                mycursor = mydb.cursor()

                sql = "INSERT INTO proximitySar (imei, prox, proxc, result, datahora) VALUES ('"+ imeiresult[1] +"', '"+ proxresult[1] +"', '"+ proxcresult[1] +"', '"+ result +"', '"+ datetimeresult[1] +"')"
                #val = (imei, prox, proxc, datetime)
                mycursor.execute(sql)

                mydb.commit()

                #print(mycursor.rowcount, "record inserted.")
                mydb.close()
    else:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="line-tests-db"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO proximitySar (imei, prox, proxc, result, datahora) VALUES ('"+ imeiresult[1] +"', '"+ proxresult[1] +"', '"+ proxcresult[1] +"', '"+ result +"', '"+ datetimeresult[1] +"')"
        #val = (imei, prox, proxc, datetime)
        mycursor.execute(sql)

        mydb.commit()

        #print(mycursor.rowcount, "record inserted.")
        mydb.close()

    selectdb.commit()


    selectdb.close()

    #FIM DA LEITURA DAS FALHAS



