def read_formulas_from_text():
    formulas = []
    print("Paste the formulas (one per line), and press 'Enter' on an empty line when finished:")
    while True:
        line = input()
        if line == '':
            break
        formulas.append(line.strip())
    return formulas

def read_formulas_from_txt_file(filepath):
    with open(filepath, 'r') as file:
        formulas = [line.strip() for line in file.readlines()]
    return formulas

def read_formulas_from_excel(filepath):
    df = pd.read_excel(filepath, header=None)
    return df[0].tolist()