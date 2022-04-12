#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#
#                   @Project Name : Super Plot Machine
#
#                   @File Name    : SuperPlotMachine.py
#
#                   @Programmer   : Koshou
#
#                   @Start Date   : 2022/4/1 
#
#                   @Last Update  : 2022/4/1
#
#-------------------------------------------------------------------
'''

import os
import matplotlib.pyplot as plt

COLOR_MAP = ['#FFBE7D', '#4E79A7', '#F28E2B', '#A0CBE8', '#59A14F', '#8CD17D', '#B6992D', '#F1CE63', '#499894', '#86BCB6', '#E15759', '#FF9D9A', '#79706E', '#BAB0AC', '#D37295', '#FABFD2', '#B07AA1', '#D4A6C8', '#9D7660', '#D7B5A6']

class SuperPlotMahcine:
    def __init__(self, **kwargs):
        self.filename = kwargs["filename"]
        self.dataframe = kwargs["dataframe"]
        self.output_folder = kwargs["output_folder"]
        self.make_folder()
        pass
    
    def make_folder(self):
        '''
        make folder what each file one folder in "fig" folder
        '''
        
        folder_name = self.output_folder+'\\'+self.filename
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            
    def plot_singal(self):
        '''
        plot each columns one fig 
        '''
        
        for content in zip(self.dataframe.columns, COLOR_MAP):
            plt.figure(figsize=(6,4))
            plt.plot(self.dataframe.index, self.dataframe[content[0]], color = content[1], label = content[0])
            plt.xlabel("index_num")
            plt.ylabel(f"{content[0]}_value")
            plt.grid()
            plt.title(f"{self.filename}_{content[0]}")
            plt.legend(bbox_to_anchor=(1.2,1))
            plt.savefig(f"{self.output_folder}\\{self.filename}\\{self.filename}_{content[0]}.png", bbox_inches='tight')
            plt.clf()
            
    def plot_all_in_one(self):
        '''
        plot all columns of dataframe's data in one fig
        '''
        
        plt.figure(figsize=(6,4))
        for content in zip(self.dataframe.columns, COLOR_MAP):
            plt.plot(self.dataframe.index, self.dataframe[content[0]], color = content[1], label = content[0])
        plt.xlabel("index_num")
        plt.ylabel("value")
        plt.grid()
        plt.title(f"{self.filename}_all_data")
        plt.legend(bbox_to_anchor=(1.2,1))
        plt.savefig(f"{self.output_folder}\\{self.filename}\\{self.filename}_all_data.png", bbox_inches='tight')
        
        
    def plot_two_axis(self):
        '''
        this function can choose which columns, default: front of two columns
        if want to choose columns of left side and rhght side, change the parameter called :"left_data" and "right_data"
        '''

        count = 0
        cols_list = []
        for cols in self.dataframe.columns:
            count += 1
            cols_list.append(cols)
        if count < 2:
            print("The num of columns must more than two") 
            raise Exception ("The num of columns must more than two")

        left_data = cols_list[0]
        right_data = cols_list[1]
        
        fig, ax_left = plt.subplots()
        fig.set_size_inches(6, 4)
        ax_right = ax_left.twinx()
        ax_left.set_xlabel("index_num")
        ax_left.set_ylabel(left_data, color=COLOR_MAP[0], fontsize=12, rotation = 0)
        ax_left.plot(self.dataframe.index, self.dataframe[left_data], color=COLOR_MAP[0], alpha=0.75)
        ax_left.tick_params(axis='y', labelcolor=COLOR_MAP[0])
        ax_right.set_ylabel(right_data, color=COLOR_MAP[1], fontsize=12, rotation = 0)
        ax_right.plot(self.dataframe.index, self.dataframe[right_data], color=COLOR_MAP[1], alpha=1)
        ax_right.tick_params(axis='y', labelcolor=COLOR_MAP[1])
        fig.tight_layout()
        plt.grid()
        plt.title(f"{self.filename}_{left_data} and {right_data}")
        plt.savefig(f"{self.output_folder}\\{self.filename}\\{self.filename}_two_axis.png", bbox_inches='tight')
        