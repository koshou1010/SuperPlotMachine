''' main.py use for change parameters incuding : choose cols, load file'''
import os
import pandas as pd
import SuperPlotMachine as SPM



def load_file(file):
    '''
    load_file use for load csv file, and paring it, then return a cleand dataframe
    '''

    dataframe = pd.read_csv(file)
    
    
    return dataframe


def make_output_folder():
    '''
    use for make folder and save output file
    '''
    
    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)


if __name__ == '__main__':
    OUTPUT_FOLDER = 'fig'
    FILE_PATH = 'data'
    make_output_folder()
    for root, dirs, files in os.walk(FILE_PATH):
        for file in files:
            if file.endswith('csv'):
                print(root+'\\'+file)
                dataframe = load_file(root+'\\'+file)

                plot = SPM.SuperPlotMahcine(dataframe = dataframe, filename = file.split('.')[0], output_folder = OUTPUT_FOLDER)
                plot.plot_singal()
                plot.plot_all_in_one()
                plot.plot_two_axis()
