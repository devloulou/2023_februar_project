"""
This module handle file related task such as:
write JSON files and get metadata from folders
"""
import os
import json

class FileHandler:
    # def __init__(self, folder_path):
    #     self.folder_path = folder_path
    #     self.movies = self.get_files_path_from_folder()
    root_folder = os.path.dirname(os.path.dirname(__file__))
    meta_data = os.path.join(root_folder, 'meta_data')
    posters = os.path.join(root_folder, 'posters')

    def __init__(self):
        self.create_folders()

    @staticmethod
    def get_files_path_from_folder(folder_path):
        temp = os.listdir(folder_path)
        movies = []

        for item in temp:
            if item[-4:] == '.mkv':
                movies.append(item.split('.')[0])

        return movies
    
    def write_json(self, json_path, data):
        # if not os.path.exists(os.path.dirname(json_path)):
        #     raise Exception('Nem létezik a megadott útvonal györkérkönyvtára')
        with open(json_path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def create_folders(self):
        if not os.path.exists(self.meta_data):
            os.mkdir(self.meta_data)
        
        if not os.path.exists(self.posters):
            os.mkdir(self.posters)

if __name__ == '__main__':
    f_path = r"C:\WORK\2023_februar_projekt\movies"
    test = FileHandler()

    movies= test.get_files_path_from_folder(f_path)

    print(movies)
    # print(test.movies)

    # get_files_path_from_folder() függvény return valueját majd vizsgálnom kell, hogy üres e

    #test.write_json('valami/test.json', {'kulcs': 'ertek'})