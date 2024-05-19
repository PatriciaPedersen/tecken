import os
from utils.img_process import process_img

def make_csv():
    """
    Extraherar referenspunkter från bilder i datasetet och sparar dem i en CSV-fil.
    """
    mypath = 'dataset'
    output_csv = 'dataset.csv'
    
    # Öppna CSV-filen i lägg-till-läge
    with open(output_csv, 'a') as file_name:
        # Iterera genom varje mapp i datasetmappen
        for each_folder in os.listdir(mypath):
            if each_folder.startswith('._'):
                continue
            
            # Iterera genom varje bild i mappen
            for each_image in os.listdir(os.path.join(mypath, each_folder)):
                if each_image.startswith('._'):
                    continue
                
                label = each_folder  # Mappnamnet används som etikett
                file_loc = os.path.join(mypath, each_folder, each_image)
                
                try:
                    # Extrahera referenspunkter
                    data = process_img(file_loc)
                    
                    # Skriv referenspunkterna till CSV-filen
                    for id, value in enumerate(data):
                        file_name.write(f"{value},")
                    
                    # Skriv etiketten till CSV-filen
                    file_name.write(f"{label}\n")
                
                except Exception as e:
                    # Hantera eventuella fel som uppstår vid bearbetning
                    print(f"Fel vid bearbetning av fil {file_loc}: {e}")
                    file_name.write('0,None\n')
    
    print('CSV skapad')

if __name__ == "__main__":
    make_csv()
