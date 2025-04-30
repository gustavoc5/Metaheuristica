import json

def salvar_dicionario_em_data(cco_dict, sin_dict, historicos_list, semana_dict, horarios_dict, path='data.py'):
    with open(path, 'w', encoding='utf-8') as f:
        f.write("historicos = " + json.dumps(historicos_list, indent=4, ensure_ascii=False) + "\n\n")
        f.write("semana = " + json.dumps(semana_dict, indent=4, ensure_ascii=False) + "\n\n")
        f.write("horarios = " + json.dumps(horarios_dict, indent=4, ensure_ascii=False) + "\n\n")
        f.write("cco = " + json.dumps(cco_dict, indent=4, ensure_ascii=False) + "\n\n")
        f.write("sin = " + json.dumps(sin_dict, indent=4, ensure_ascii=False) + "\n")
    print("[✓] Arquivo data.py atualizado com os novos dados.")
