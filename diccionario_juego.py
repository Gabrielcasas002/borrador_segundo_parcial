diccionario_prueba = [ {"letras" : ["A","C","R","R","O","S"], "palabras" : ["CARROS", "CARRO", "CARO", "ROCA", "ORCA", "ARO", "RARO","ARCO"]},
                {"letras": ["E","L","S","O","P","A"], "palabras": ["PALO","PASO","PESO", "SOL", "POSE", "EL","SOPA","OLA","PELOS"]},
                {"letras": ["I","R","C","O","T","A"], "palabras": ["RICOTA","CORTA","RICO","TOCAR","ACTOR","RIO","OCA","TIRO"]},
                {"letras": ["O","T","J","S","A","O"], "palabras": ["OJOTAS","SOJA","JOTA","TOS","AJO","AJOS"]},
                {"letras": ["F","L","A","R","T","O"], "palabras": ["FLOTAR","FLORA","ORAL","RATO","ALTO","FARO"]},
                {"letras": ["M","R","I","U","C","A"], "palabras": ["CURA","RIMA","MIRA","CIMA","MAR","IRA"]},
                {"letras": ["D","O","S","I","A","L"], "palabras": ["SALDO","DIOS","SAL","LADO","DIOSA","LISO","DOS"]},
                {"letras": ["T", "O", "G", "I", "A", "T"], "palabras": ["GATITO","GATO","GOTA","TITO","IA","TIO","TIA"]},
                {"letras": ["G", "T", "O", "A", "M", "I"], "palabras": ["GOMITA","GOMA","MITO","GOTA","MIGA","TOMA","AMO","TIMO"]},
                {"letras": ["A", "R", "U", "N", "I", "T"], "palabras": ["RUTINA","RUTA","TINA","RITA","UNIR","URNA","TUNA"]},
                {"letras": ["I", "A", "N", "O", "C", "M"], "palabras": ["CAMINO","MINA","MONA","CIMA","COMA","MANO","MIO"]},
                {"letras": ["P", "O", "R", "D", "I", "A"], "palabras": ["RAPIDO","RAP","IDA","PIDA","PIDO","PRADO","PODAR","PARO"]},
                {"letras": ["R", "O", "S", "E", "P", "R"], "palabras": ["PERROS","PERO","PERRO","PESO","RESO","PRESO"]},
                {"letras": ["B", "C", "S", "R", "O", "A"], "palabras": ["BARCOS","COSA","ROSA","COBRA","OBRA","CASO","CABO","BOCA"]},
                {"letras": ["O", "D", "R", "A", "O", "D"], "palabras": ["RODADO","DADO","DORADO","DODO","ORO","DARDO","ORDA"]},
                ]


# Modificar algunas listas del diccionario_prueba para que contengan mas palabras

diccionario_juego = [
    {
        "nivel": 1,
        "estado_comodines": [False,False,False],
        "partidas": [
            {"letras": ["A","C","R","R","O","S"],
             "palabras": ["CARROS", "CARRO", "CARO", "ROCA", "ORCA", "ARO", "RARO","ARCO"]},

            {"letras": ["E","L","S","O","P","A"],
             "palabras": ["PALO","PASO","PESO", "SOL", "POSE", "EL","SOPA","OLA","PELOS"]},

            {"letras": ["I","R","C","O","T","A"],
             "palabras": ["RICOTA","CORTA","RICO","TOCAR","ACTOR","RIO","OCA","TIRO"]}
        ]
    },

    {
        "nivel": 2,
        "estado_comodines": [False,False,False],
        "partidas": [
            {"letras": ["O","T","J","S","A","O"],
             "palabras": ["OJOTAS","SOJA","JOTA","TOS","AJO","AJOS"]},

            {"letras": ["F","L","A","R","T","O"],
             "palabras": ["FLOTAR","FLORA","ORAL","RATO","ALTO","FARO"]},

            {"letras": ["M","R","I","U","C","A"],
             "palabras": ["CURA","RIMA","MIRA","CIMA","MAR","IRA"]}
        ]
    },

    {
        "nivel": 3,
        "estado_comodines": [False,False,False],
        "partidas": [
            {"letras": ["D","O","S","I","A","L"],
             "palabras": ["SALDO","DIOS","SAL","LADO","DIOSA","LISO","DOS"]},

            {"letras": ["T", "O", "G", "I", "A", "T"],
             "palabras": ["GATITO","GATO","GOTA","TITO","IA","TIO","TIA"]},

            {"letras": ["G", "T", "O", "A", "M", "I"],
             "palabras": ["GOMITA","GOMA","MITO","GOTA","MIGA","TOMA","AMO","TIMO"]}
        ]
    },

    {
        "nivel": 4,
        "estado_comodines": [False,False,False],
        "partidas": [
            {"letras": ["A", "R", "U", "N", "I", "T"],
             "palabras": ["RUTINA","RUTA","TINA","RITA","UNIR","URNA","TUNA"]},

            {"letras": ["I", "A", "N", "O", "C", "M"],
             "palabras": ["CAMINO","MINA","MONA","CIMA","COMA","MANO","MIO"]},

            {"letras": ["P", "O", "R", "D", "I", "A"],
             "palabras": ["RAPIDO","RAP","IDA","PIDA","PIDO","PRADO","PODAR","PARO"]}
        ]
    },

    {
        "nivel": 5,
        "estado_comodines": [False,False,False],
        "partidas": [
            {"letras": ["R", "O", "S", "E", "P", "R"],
             "palabras": ["PERROS","PERO","PERRO","PESO","RESO","PRESO"]},

            {"letras": ["B", "C", "S", "R", "O", "A"],
             "palabras": ["BARCOS","COSA","ROSA","COBRA","OBRA","CASO","CABO","BOCA"]},

            {"letras": ["O", "D", "R", "A", "O", "D"],
             "palabras": ["RODADO","DADO","DORADO","DODO","ORO","DARDO","ORDA"]}
        ]
    }
]

diccionario_estadisticas = {
    "Puntuacion Total" : 0,
    "Ingresos incorrectos" : 0,
    "Cantidad de rondas jugadas": 0,
    "Tiempo restante total en segundos" : 0,
    "Tiempo entre niveles" : 0,
    "Tiempo promedio entre niveles" : 0
}
