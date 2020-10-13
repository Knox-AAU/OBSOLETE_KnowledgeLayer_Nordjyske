import knox_util, os
import shutil

from environment.EnvironmentConstants import EnvironmentConstants as ec
from loader.JsonLoader import NewsStruct

def process_existing(path: str) -> None:
    """
    Input:
        path: str - The input directory path, that will be processed

    This method will look through the input directory, and determine whether a file has been processed previously
    When the file has been processed, it will be moved to the output directory.
    """
    print(f'Checking for existing files in \'{path}\'...')
    paths = [os.path.join(path, fn) for fn in next(os.walk(path))[2]]
    if len(paths) == 0:
        print('No files were created between sessions')
        return

    for path in paths:
        
        # Process files here
        split_path = os.path.split(path)

        try:
            news = NewsStruct(path)
            news.load_publications()

            shutil.move(src=path, dst=f'{ec().get_value(ec().OUTPUT_DIRECTORY)}{split_path[-1]}')
        except:
            shutil.move(src=path, dst=f'{ec().get_value(ec().ERROR_DIRECTORY)}{split_path[-1]}')


    # Simulated finished
    