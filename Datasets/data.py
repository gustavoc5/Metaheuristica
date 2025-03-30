import numpy as np

materias_curso={
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
        "requisito":["CTCO02"],
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