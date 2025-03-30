import numpy as np

materias_curso_CCO={
    "XDES01":{
        "id":"1",
        "nome": "Fundamentos da Programação",
        "ch": "64",
        "anual":0,
        "requisito":0,
        "equivalentes":
    },
    "CRSC03":{
        "id":"2",
        "nome":"Arquitetura de Computadores 1", 
        "ch": "64",
        "anual": ,
        "requisito":0,
        "equivalentes":

        
    },
    "MAT00A":{
        "id":"3",
        "nome":"Cálculo A", 
        "ch": "64",
        "anual": 0,
        "requisito":0,
        "equivalentes":
    },
    "XMAC01":{
        "id":"4",
        "nome":"Matemática Discreta", 
        "ch": "64",
        "anual": ,
        "requisito":0,
        "equivalentes":
    },
    "CAHC04":{
        "id":"5",
        "nome":"Projeto Integrado", 
        "ch": "32",
        "anual": ,
        "requisito":0,
        "equivalentes":
    },
    "CTCO01":{
        "id":"6",
        "nome":"Algoritmo e Estrutura de Dados 1", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES01"],
        "equivalentes":
    },
    "CRSC04":{
        "id":"7",
        "nome":"Arquitetura de Computadores 2", 
        "ch": "64",
        "anual": ,
        "requisito":["CRSC03"],
        "equivalentes":  
    },
    "MAT00B":{
        "id":"8",
        "nome":"Cálculo B", 
        "ch": "64",
        "anual": 0,
        "requisito":["MAT00B"],
        "equivalentes":
    },
    "CMAC04":{
        "id":"9",
        "nome":"Modelagem Computacional", 
        "ch": "64",
        "anual":1,
        "requisito":["MAT00A"],
        "equivalentes":
    },
    "CTCO02":{
        "id":"10",
        "nome":"Algoritmo e Estrutura de Dados 2", 
        "ch": "64",
        "anual": ,
        "requisito":["CTCO01"],
        "equivalentes":
    },
    "XDES02":{
        "id":"11",
        "nome":"Programação Orientada a Objetos", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES01"],
        "equivalentes":
    },
    "XDES04":{
        "id":"12",
        "nome":"Engenharia de Software 1", 
        "ch": "64",
        "anual": ,
        "requisito":,
        "equivalentes":
    },
    "CRSC02":{
        "id":"13",
        "nome":"Sistemas Operacionais", 
        "ch": "64",
        "anual": ,
        "requisito":["CTCO01","CRSC04"],
        "equivalentes":
    },
    "CMAC03":{
        "id":"14
        "nome":"Algoritmos em Grafos", 
        "ch": "64",
        "anual":0 ,
        "requisito":["CTCO01"],
        "equivalentes":
    },
    "XMAC02":{
        "id":"14",
        "nome":"Métodos Matemáticos para Análise de Dados", 
        "ch": "64",
        "anual": ,
        "requisito":["MAT00A","XMAC01","CTCO01"],
        "equivalentes":
    },
    "CTCO04":{
        "id":"15",
        "nome":"Projeto e Análise de Algoritmos", 
        "ch": "64",
        "anual": ["CTCO02"],
        "requisito":,
        "equivalentes":
    },
    "XDES03":{
        "id":"16",
        "nome":"Programação Web", 
        "ch": "64",
        "anual": 0,
        "requisito":["XDES02"],
        "equivalentes":
    },
    "CDES05":{
        "id":"17",
        "nome":"Programação Lógica e Funcional", 
        "ch": "64",
        "anual": ,
        "requisito":["XMAC01"],
        "equivalentes":
    },
    "XRSC01":{
        "id":"18",
        "nome":"Redes de Computadores", 
        "ch": "64",
        "anual": 0,
        "requisito":["CRSC02"],
        "equivalentes":
    },
    "CRSC05":{
        "id":"19",
        "nome":"Sistemas Embarcados", 
        "ch": "64",
        "anual": ,
        "requisito":["CRSC02"],
        "equivalentes":
    },
    "CMAC05":{
        "id":"20",
        "nome":"Cálculo Numérico para Computação", 
        "ch": "64",
        "anual": ,
        "requisito":["MAT00B"],
        "equivalentes":
    },
    "CTCO03":{
        "id":"21",
        "nome":"Análise e Projeto Orientados a Objeto", 
        "ch": "64",
        "anual":0 ,
        "requisito":["XDES02"],
        "equivalentes":
    },
    "CTCO05":{
        "id":"22",
        "nome":"Teoria da Computação", 
        "ch": "64",
        "anual": 0,
        "requisito":["CTCO04","CDES05"],
        "equivalentes":
    },
    "XPAD01":{
        "id":"23",
        "nome":"Banco de Dados 1", 
        "ch": "64",
        "anual": ,
        "requisito":["STCO02"],
        "equivalentes":
    },
    "XMCO01":{
        "id":"24",
        "nome":"Inteligência Artificial", 
        "ch": "64",
        "anual": ,
        "requisito":["XMAC02"],
        "equivalentes":
    },
    "CMCO05":{
        "id":"25",
        "nome":"Introdução a Computação Visual", 
        "ch": "64",
        "anual": ,
        "requisito":["XMAC02","XDES02"],
        "equivalentes":
    },
    "CTCO06":{
        "id":"26",
        "nome":"Compiladores", 
        "ch": "64",
        "anual": ,
        "requisito":[],
        "equivalentes":
    },
    "XAHC02":{
        "id":"27",
        "nome":"Interação Humano-Computador", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES03","XDES04"],
        "equivalentes":
    },
    "XAHC03":{
        "id":"28",
        "nome":"Metodologia Científica", 
        "ch": "64",
        "anual": ,
        "requisito":["TCC1"],
        "equivalentes":
    },
    "XAHC01":{
        "id":"28",
        "nome":"Computação e Sociedade", 
        "ch": "64",
        "anual": ,
        "requisito":[],
        "equivalentes":
    },
    
    
}

materias_curso_SIN={
    "XDES01":{
        "id":"1",
        "nome": "Fundamentos da Programação",
        "ch": "64",
        "anual":0,
        "requisito":0,
        "equivalentes":
    },
    "CAHC04":{
        "id":"2",
        "nome":"Projeto Integrado", 
        "ch": "64",
        "anual": ,
        "requisito":0,
        "equivalentes":
    },
    "SAHC05":{
        "id":"3",
        "nome":"Fundamentos de Sistemas de Informação", 
        "ch": "32",
        "anual": ,
        "requisito":0,
        "equivalentes":
    },
    
    "MAT00A":{
        "id":"4",
        "nome":"Cálculo A", 
        "ch": "64",
        "anual": 0,
        "requisito":0,
        "equivalentes":
    },
    "IEPG01":{
        "id":"5",
        "nome":"Empreendedorismo e Inovação", 
        "ch": "48",
        "anual": 0,
        "requisito":0,
        "equivalentes":
    },
    "IEPG22":{
        "id":"6",
        "nome":"Administração Aplicada", 
        "ch": "32",
        "anual": 0,
        "requisito":0,
        "equivalentes":
    },
    "XDES02":{
        "id":"7",
        "nome":"Programação Orientada a Objetos", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES01"],
        "equivalentes":
    },
    "XDES04":{
        "id":"8",
        "nome":"Engenharia de Software 1", 
        "ch": "64",
        "anual": ,
        "requisito":,
        "equivalentes":
    },
    "STCO01":{
        "id":"9",
        "nome":"Algoritmo e Programação 1", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES01"],
        "equivalentes":
    },
    "XMAC01":{
        "id":"10",
        "nome":"Matemática Discreta", 
        "ch": "64",
        "anual": ,
        "requisito":0,
        "equivalentes":
    },
    "IEPG04":{
        "id":"11",
        "nome":"Mapeamento de Processos", 
        "ch": "32",
        "anual": ,
        "requisito":0,
        "equivalentes":
    },
    "XDES03":{
        "id":"12",
        "nome":"Programação Web", 
        "ch": "64",
        "anual": 0,
        "requisito":["XDES02"],
        "equivalentes":
    },

     "SDES05":{
        "id":"13",
        "nome":"Engenharia de Software 2", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES04"],
        "equivalentes":
    },
    "STCO02":{
        "id":"14",
        "nome":"Algoritmo e Programação 2", 
        "ch": "64",
        "anual": ,
        "requisito":["STCO01"],
        "equivalentes":
    },
    "SRSC03":{
        "id":"15",
        "nome":"Organização e Arquitetura de Computadores", 
        "ch": "64",
        "anual": ,
        "requisito":[""],
        "equivalentes":
    },
    "ECNO01":{
        "id":"16",
        "nome":"Economia", 
        "ch": "48",
        "anual": ,
        "requisito":[""],
        "equivalentes":
    },
    "XPAD01":{
        "id":"17",
        "nome":"Banco de Dados 1", 
        "ch": "64",
        "anual": ,
        "requisito":["STCO02"],
        "equivalentes":
    },
    "XMAC02":{
        "id":"18",
        "nome":"Métodos Matemáticos para Análise de Dados", 
        "ch": "64",
        "anual": ,
        "requisito":["MAT00A","XMAC01","STCO01"],
        "equivalentes":
    },
    "SMAC03":{
        "id":"19
        "nome":"Grafos", 
        "ch": "64",
        "anual":0 ,
        "requisito":["STCO01"],
        "equivalentes":
    },
    "SRSC02":{
        "id":"20",
        "nome":"Sistemas Operacionais", 
        "ch": "64",
        "anual": ,
        "requisito":["STCO01","SRSC03"],
        "equivalentes":
    },
    "IEPG14":{
        "id":"21",
        "nome":"Comportamento Organizacional 1", 
        "ch": "32",
        "anual": ,
        "requisito":[""],
        "equivalentes":
    },
    "SPAD02":{
        "id":"22",
        "nome":"Banco de Dados 2", 
        "ch": "64",
        "anual": ,
        "requisito":["XPAD01"],
        "equivalentes":
    },
    "SPAD03":{
        "id":"23",
        "nome":"Introdução à Análise de Dados", 
        "ch": "64",
        "anual": ,
        "requisito":["XPAD01","XMAC02"],
        "equivalentes":
    },
    "XRSC01":{
        "id":"24",
        "nome":"Redes de Computadores", 
        "ch": "64",
        "anual": 0,
        "requisito":["SRSC02"],
        "equivalentes":
    },
    "ADM515":{
        "id":"25",
        "nome":"Gestão de Conhecimentos", 
        "ch": "48",
        "anual": 0,
        "requisito":[""],
        "equivalentes":
    },
    "SDES06":{
        "id":"26",
        "nome":"Gerência de Projetos de Software", 
        "ch": "64",
        "anual": 0,
        "requisito":["XDES04"],
        "equivalentes":
    },
    "XMCO01":{
        "id":"27",
        "nome":"Inteligência Artificial", 
        "ch": "64",
        "anual": ,
        "requisito":["XMAC02"],
        "equivalentes":
    },
    "IEPG10":{
        "id":"28",
        "nome":"Engenharia Econômica", 
        "ch": "48",
        "anual": ,
        "requisito":[""],
        "equivalentes":
    },
    "SDES07":{
        "id":"29",
        "nome":"Desenvolvimento de Sistemas Web", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES03","XDES04","XPAD01"],
        "equivalentes":
    },
    "XAHC02":{
        "id":"30",
        "nome":"Interação Humano-Computador", 
        "ch": "64",
        "anual": ,
        "requisito":["XDES03"],
        "equivalentes":
    },
    "XAHC01":{
        "id":"31",
        "nome":"Computação e Sociedade", 
        "ch": "64",
        "anual": ,
        "requisito":[],
        "equivalentes":
    },
    "XAHC03":{
        "id":"32",
        "nome":"Metodologia Científica", 
        "ch": "64",
        "anual": ,
        "requisito":["TCC1"],
        "equivalentes":
    },
    "ADM03E":{
        "id":"33",
        "nome":"Empreendedorismo Tecnológico", 
        "ch": "48",
        "anual": ,
        "requisito":["IEPG01"],
        "equivalentes":
    },
    "XAHC03":{
        "id":"34",
        "nome":"Gestão e Governança de TI", 
        "ch": "64",
        "anual": ,
        "requisito":["IEPG22"],
        "equivalentes":
    },
     
    
    
    
    
    
}