import matplotlib.pyplot as plt
import json

def open_file(file_json):
    try:
        with open(file_json, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Le fichier {file_json} est introuvable.")
        return {"features": []}


for i in range(0,22):
    input_file = open_file(f'input_lines_{i}.json')
    output_file = open_file(f'output_lines_{i}.json')

    plt.figure(figsize=(10, 6))

    if 'features' in input_file and input_file['features']:
        for line in input_file['features']:
            points = line['geometry']['coordinates']
            x, y = zip(*points)  
            plt.plot(x, y, label=line['id'])  

    if 'features' in output_file and output_file['features']:
        for line in output_file['features']:
            points = line['geometry']['coordinates']
            x, y = zip(*points)
            plt.plot(x, y, color='black', linewidth=2, label=f"{line['id']} (Output)")

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Visualisation des lignes avec ligne de sortie')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'graph_{i}')
    plt.close()
