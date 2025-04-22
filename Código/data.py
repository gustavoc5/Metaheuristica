historicos = [
    "historico_CCO-1.pdf",
    "historico_CCO-2.pdf",
    "historico_CCO-3.pdf",
    "historico_CCO-4.pdf",
    "historico_CCO-5.pdf",
    "historico_SIN-1.pdf",
    "historico_SIN-2.pdf",
    "historico_SIN-3.pdf",
    "historico_SIN-4.pdf",
    "historico_SIN-5.pdf"
]

cco = {
    "1": {
        "codigo": "XDES01",
        "nome": "Fundamentos da Programação",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [
            "COM110",
            "ECOP11A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "2": {
        "codigo": "MAT00A",
        "nome": "Cálculo A",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [
            "MAT001"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "3": {
        "codigo": "XMAC01",
        "nome": "Matemática Discreta",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": 0,
        "equivalentes": [
            "MAT015",
            "MAT057",
            "MAT017",
            "ECOM11A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "4": {
        "codigo": "CAHC04",
        "nome": "Projeto Integrado",
        "ch": "32",
        "horario": [],
        "anual": 1,
        "requisito": 0,
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "5": {
        "codigo": "CTCO01",
        "nome": "Algoritmo e Estrutura de Dados 1",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "1"
        ],
        "equivalentes": [
            "COM111",
            "STCO01",
            "ECOP02A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 2,
        "obrigatoria": 1
    },
    "53": {
        "codigo": "CRSC03",
        "nome": "Arquitetura de Computadores 1",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [],
        "equivalentes": [
            "CIC120",
            "ELTD11A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "6": {
        "codigo": "CRSC04",
        "nome": "Arquitetura de Computadores 2",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "53"
        ],
        "equivalentes": [
            "CIC121",
            "ECOX01"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 2,
        "obrigatoria": 1
    },
    "7": {
        "codigo": "MAT00B",
        "nome": "Cálculo B",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "2"
        ],
        "equivalentes": [
            "MAT002"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 2,
        "obrigatoria": 1
    },
    "8": {
        "codigo": "CMAC04",
        "nome": "Modelagem Computacional",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "2"
        ],
        "equivalentes": [
            "CIC510"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 2,
        "obrigatoria": 1
    },
    "9": {
        "codigo": "CTCO02",
        "nome": "Algoritmo e Estrutura de Dados 2",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "5"
        ],
        "equivalentes": [
            "COM112",
            "STCO02"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "10": {
        "codigo": "XDES02",
        "nome": "Programação Orientada a Objetos",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "1"
        ],
        "equivalentes": [
            "COM220",
            "ECOP13A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "11": {
        "codigo": "XDES04",
        "nome": "Engenharia de Software 1",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [
            "C0M210",
            "XDES04",
            "ECOP13A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "12": {
        "codigo": "CRSC02",
        "nome": "Sistemas Operacionais",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "5",
            "6"
        ],
        "equivalentes": [
            "COM120",
            "ECOS11A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "13": {
        "codigo": "CMAC03",
        "nome": "Algoritmos em Grafos",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "5"
        ],
        "equivalentes": [
            "SIN110",
            "SMAC03"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "14": {
        "codigo": "XMAC02",
        "nome": "Métodos Matemáticos para Análise de Dados",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "2",
            "3",
            "5"
        ],
        "equivalentes": [
            "MAT013"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "15": {
        "codigo": "CTCO04",
        "nome": "Projeto e Análise de Algoritmos",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "9"
        ],
        "equivalentes": [
            "CIC110"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "16": {
        "codigo": "XDES03",
        "nome": "Programação Web",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "10"
        ],
        "equivalentes": [
            "COM222",
            "ECOX05"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "17": {
        "codigo": "CDES05",
        "nome": "Programação Lógica e Funcional",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "3"
        ],
        "equivalentes": [
            "CIC131"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "18": {
        "codigo": "XRSC01",
        "nome": "Redes de Computadores",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "12"
        ],
        "equivalentes": [
            "COM240"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "19": {
        "codigo": "CRSC05",
        "nome": "Sistemas Embarcados",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "12"
        ],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "20": {
        "codigo": "CMAC05",
        "nome": "Cálculo Numérico para Computação",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "7"
        ],
        "equivalentes": [
            "CIC250"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "21": {
        "codigo": "CTCO03",
        "nome": "Análise e Projeto Orientados a Objeto",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "16"
        ],
        "equivalentes": [
            "COM221"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "22": {
        "codigo": "CTCO05",
        "nome": "Teoria da Computação",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "15",
            "17"
        ],
        "equivalentes": [
            "CIC132"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "23": {
        "codigo": "XPAD01",
        "nome": "Banco de Dados 1",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "9"
        ],
        "equivalentes": [
            "COM230",
            "ECOT13A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "24": {
        "codigo": "XMCO01",
        "nome": "Inteligência Artificial",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "14"
        ],
        "equivalentes": [
            "CIC260",
            "SIN260"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "25": {
        "codigo": "CMCO05",
        "nome": "Introdução a Computação Visual",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "14",
            "16"
        ],
        "equivalentes": [
            "CIC271"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "26": {
        "codigo": "CTCO06",
        "nome": "Compiladores",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "22"
        ],
        "equivalentes": [
            "CIC220"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 6,
        "obrigatoria": 1
    },
    "27": {
        "codigo": "XAHC02",
        "nome": "Interação Humano-Computador",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "16",
            "11"
        ],
        "equivalentes": [
            "COM213"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 7,
        "obrigatoria": 1
    },
    "28": {
        "codigo": "XAHC03",
        "nome": "Metodologia Científica",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "51"
        ],
        "equivalentes": [
            "COM310"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 7,
        "obrigatoria": 1
    },
    "29": {
        "codigo": "XAHC01",
        "nome": "Computação e Sociedade",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [],
        "equivalentes": [
            "COM312"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 7,
        "obrigatoria": 1
    },
    "51": {
        "codigo": "TCC1",
        "nome": "TCC1",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "28"
        ],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 7,
        "obrigatoria": 1
    },
    "52": {
        "codigo": "TCC2",
        "nome": "TCC2",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "28"
        ],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 8,
        "obrigatoria": 1
    }
}

sin = {
    "1": {
        "codigo": "XDES01",
        "nome": "Fundamentos da Programação",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [
            "COM110",
            "ECOP11A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "2": {
        "codigo": "MAT00A",
        "nome": "Cálculo A",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [
            "MAT001"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "3": {
        "codigo": "XMAC01",
        "nome": "Matemática Discreta",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": 0,
        "equivalentes": [
            "MAT015",
            "MAT057",
            "MAT017",
            "ECOM11A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 2,
        "obrigatoria": 1
    },
    "4": {
        "codigo": "CAHC04",
        "nome": "Projeto Integrado",
        "ch": "32",
        "horario": [],
        "anual": 1,
        "requisito": 0,
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "10": {
        "codigo": "XDES02",
        "nome": "Programação Orientada a Objetos",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "1"
        ],
        "equivalentes": [
            "COM220",
            "ECOP13A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "11": {
        "codigo": "XDES04",
        "nome": "Engenharia de Software 1",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [
            "C0M210",
            "XDES04",
            "ECOP13A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "16": {
        "codigo": "XDES03",
        "nome": "Programação Web",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "10"
        ],
        "equivalentes": [
            "COM222",
            "ECOX05"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "18": {
        "codigo": "XRSC01",
        "nome": "Redes de Computadores",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "12"
        ],
        "equivalentes": [
            "COM240"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "23": {
        "codigo": "XPAD01",
        "nome": "Banco de Dados 1",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "9"
        ],
        "equivalentes": [
            "COM230",
            "ECOT13A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "24": {
        "codigo": "XMCO01",
        "nome": "Inteligência Artificial",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "14"
        ],
        "equivalentes": [
            "CIC260",
            "SIN260"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "27": {
        "codigo": "XAHC02",
        "nome": "Interação Humano-Computador",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "16",
            "11"
        ],
        "equivalentes": [
            "COM213"
        ],
        "situacao": 0,
        "parametro": 0
    },
    "28": {
        "codigo": "XAHC03",
        "nome": "Metodologia Científica",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "TCC1"
        ],
        "equivalentes": [
            "COM310"
        ],
        "situacao": 0,
        "parametro": 0
    },
    "29": {
        "codigo": "XAHC01",
        "nome": "Computação e Sociedade",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [],
        "equivalentes": [
            "COM312"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 8,
        "obrigatoria": 1
    },
    "30": {
        "codigo": "SAHC05",
        "nome": "Fundamentos de Sistemas de Informação",
        "ch": "32",
        "horario": [],
        "anual": 1,
        "requisito": 0,
        "equivalentes": [
            "SIN410"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "31": {
        "codigo": "IEPG01",
        "nome": "Empreendedorismo e Inovação",
        "ch": "48",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "32": {
        "codigo": "IEPG22",
        "nome": "Administração Aplicada",
        "ch": "32",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [
            "SIN310"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "33": {
        "codigo": "STCO01",
        "nome": "Algoritmo e Programação 1",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "1"
        ],
        "equivalentes": [
            "COM111",
            "CTCO01",
            "ECOP02A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 2,
        "obrigatoria": 1
    },
    "34": {
        "codigo": "IEPG04",
        "nome": "Mapeamento de Processos",
        "ch": "32",
        "horario": [],
        "anual": 0,
        "requisito": 0,
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 2,
        "obrigatoria": 1
    },
    "35": {
        "codigo": "SDES05",
        "nome": "Engenharia de Software 2",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "11"
        ],
        "equivalentes": [
            "COM211"
        ],
        "situacao": 0,
        "parametro": 0,
        "obrigatoria": 1
    },
    "36": {
        "codigo": "STCO02",
        "nome": "Algoritmo e Programação 2",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "33"
        ],
        "equivalentes": [
            "COM112",
            "CTCO02"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "37": {
        "codigo": "SRSC03",
        "nome": "Organização e Arquitetura de Computadores",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [],
        "equivalentes": [
            "SIN120",
            "CRSC04",
            "ECOX01"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "38": {
        "codigo": "IEPG20",
        "nome": "Introdução a economia",
        "ch": "48",
        "horario": [],
        "anual": 0,
        "requisito": [],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 3,
        "obrigatoria": 1
    },
    "39": {
        "codigo": "XMAC02",
        "nome": "Métodos Matemáticos para Análise de Dados",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "2",
            "3",
            "33"
        ],
        "equivalentes": [
            "MAT013"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "40": {
        "codigo": "SMAC03",
        "nome": "Grafos",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "33"
        ],
        "equivalentes": [
            "SIN110"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "41": {
        "codigo": "SRSC02",
        "nome": "Sistemas Operacionais",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "33",
            "37"
        ],
        "equivalentes": [
            "COM120",
            "ECOS11A"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "42": {
        "codigo": "IEPG14",
        "nome": "Comportamento Organizacional 1",
        "ch": "32",
        "horario": [],
        "anual": 0,
        "requisito": [],
        "equivalentes": [
            "SIN411"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 4,
        "obrigatoria": 1
    },
    "43": {
        "codigo": "SPAD02",
        "nome": "Banco de Dados 2",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "23"
        ],
        "equivalentes": [
            "COM231"
        ],
        "situacao": 0,
        "parametro": 0,
        "obrigatoria": 1
    },
    "44": {
        "codigo": "SPAD03",
        "nome": "Introdução à Análise de Dados",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "23",
            "39"
        ],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 1,
        "obrigatoria": 1
    },
    "45": {
        "codigo": "ADM51E",
        "nome": "Gestão de Conhecimentos",
        "ch": "48",
        "horario": [],
        "anual": 0,
        "requisito": [],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 5,
        "obrigatoria": 1
    },
    "46": {
        "codigo": "SDES06",
        "nome": "Gerência de Projetos de Software",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "11"
        ],
        "equivalentes": [
            "COM212"
        ],
        "situacao": 0,
        "parametro": 0,
        "obrigatoria": 1
    },
    "47": {
        "codigo": "IEPG10",
        "nome": "Engenharia Econômica",
        "ch": "48",
        "horario": [],
        "anual": 0,
        "requisito": [],
        "equivalentes": [
            "COM311"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 6,
        "obrigatoria": 1
    },
    "48": {
        "codigo": "SDES07",
        "nome": "Desenvolvimento de Sistemas Web",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "16",
            "11",
            "23"
        ],
        "equivalentes": [
            "SIN412"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 7,
        "obrigatoria": 1
    },
    "49": {
        "codigo": "ADM03E",
        "nome": "Empreendedorismo Tecnológico",
        "ch": "48",
        "horario": [],
        "anual": 0,
        "requisito": [
            "31"
        ],
        "equivalentes": [
            "SIN312"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 8,
        "obrigatoria": 1
    },
    "50": {
        "codigo": "SADG01",
        "nome": "Gestão e Governança de TI",
        "ch": "64",
        "horario": [],
        "anual": 1,
        "requisito": [
            "32"
        ],
        "equivalentes": [
            "SIN210"
        ],
        "situacao": 0,
        "parametro": 0,
        "periodo": 9,
        "obrigatoria": 1
    },
    "51": {
        "codigo": "TCC1",
        "nome": "TCC1",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "28"
        ],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 8,
        "obrigatoria": 1
    },
    "52": {
        "codigo": "TCC2",
        "nome": "TCC2",
        "ch": "64",
        "horario": [],
        "anual": 0,
        "requisito": [
            "51"
        ],
        "equivalentes": [],
        "situacao": 0,
        "parametro": 0,
        "periodo": 9,
        "obrigatoria": 1
    }
}
