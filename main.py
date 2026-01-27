meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "algo raro o embarazoso",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"}



word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict:
    print(meme_dict[word])
else:
        print("Esta palabra no esta disponible o es incorrecta")
