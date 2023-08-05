import os
import re

import numpy as np
import pandas as pd
from aitech.utils import (excel_pathing, csv_list_multi, chart_set_titles_axis,
                          initilize_chart)
import xlsxwriter

class MassSpec:
    def __init__(self, path, root, gc, gradient=10):
        self.root = root
        self.path = path
        self.gradient_temp = gradient
        self.gc = gc

    @staticmethod
    def massspec_temperature_convert(frame, min_temp=0, max_temp=None, t_start=30,
                                     t_gradient=10):

        result = frame.copy()
        result.index = np.round(((result.index * t_gradient) + t_start), 2)
        return result[min_temp:max_temp] if max_temp else result[min_temp:]

    def load_dataframe(self):
        gradient = self.path.get('gradient')
        isotherm = self.path.get('isotherm')
        gradient_files = csv_list_multi(gradient, 'txt').get('standard')
        isotherm_files = csv_list_multi(isotherm, 'txt').get('standard')
        p = 'Topic'

        def _helper(file_list, iso=False):
            frame_dictionary = {}
            i = 1

            for file in file_list:
                # This is finnicky -- Depends on if the original txt file has a "header"
                frame = pd.read_table(file, sep="\s+", header=None,
                                      names=['Time', 'Absorbance'])
                topic = list(filter(lambda x: re.search(p, x), file.split('\\')))

                if iso:
                    isotherm_temp = re.search(r'[\\](\d{3})[\\]', file).groups()[0]
                    ion = file.split('\\')[-1]
                    local_name = ' '.join({topic[0][5:].strip(), isotherm_temp, ion[:-4].strip()})
                else:
                    ion = file.split('\\')[-1]
                    local_name = ' '.join({topic[0][5:].strip(), ion[:-4].strip()})
                    print(local_name)
                frame['Absorbance'] = frame['Absorbance'].ewm(span=5).mean()
                ms_frame = frame
                # Duplicates anly seperated by date delt with here

                if local_name in frame_dictionary.keys():
                    local_name += f"_{i}"
                    i = +1
                frame_dictionary[local_name] = ms_frame
            return frame_dictionary

        if self.gc:
            gradient_gc = [tic_file for tic_file in gradient_files if 'tic' in tic_file.lower()]
            isotherm_gc = [tic_file for tic_file in isotherm_files if 'tic' in tic_file.lower()]
            gradient_dictionary = _helper(gradient_gc)
            isotherm_dictionary = _helper(isotherm_gc, True)
        else:
            gradient_dictionary = _helper(gradient_files)
            isotherm_dictionary = _helper(isotherm_files, True)
        return gradient_dictionary, isotherm_dictionary

    def ch(self, name, frame, writer, workbook, x, y, title, legend=True):

        chart, chartsheet, max_row, sample, sample_names = initilize_chart(frame,
                                                                           name, workbook, writer)

        chart = workbook.add_chart({
            'type': 'scatter',
            'subtype': 'smooth'})

        for i, sample_name in enumerate(sample):
            time_field = 1 + (i * 2)
            absorbance = 2 + (i * 2)
            chart.add_series({
                'name': [sample_names, 1, i + 1],
                'categories': [name, 3, time_field, max_row, time_field],
                'values': [name, 3, absorbance, max_row, absorbance], })
        chart_set_titles_axis(chart, x, y, title, legend)

        chartsheet.set_chart(chart)

    def run_excel(self):
        gradient, isotherm = self.load_dataframe()

        def f(item):
            ff = []
            if item:
                ff = pd.concat(item.values(), axis=1, keys=list(item.keys()))
            return ff

        if isotherm:
            name = f"MS_Isotherm"
            excel_path = excel_pathing(self.root, name)
            writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
            workbook = writer.book
            isotherm_frame = f(isotherm)
            mx = "Time"
            my = "Abundance"
            title = "MS"
            self.ch(name="MS", frame=isotherm_frame, writer=writer,
                    workbook=workbook, x=mx, y=my, title=title, legend=False)
            writer.save()

        if gradient:
            name = f"MS_Gradient"
            excel_path = excel_pathing(self.root, name)
            if not self.gc:
                for key in gradient:
                    gradient[key].rename(columns={
                        'Time': 'Temperature'}, inplace=True)
                    gradient[key]['Temperature'] = gradient[key]['Temperature'].apply(
                        lambda x: 30 + x * self.gradient_temp)
            writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
            workbook = writer.book
            mx = "Temperature (°C)"
            my = "Abundance"
            title = "MS"
            gradient_frame = f(gradient)
            self.ch(name="MS", frame=gradient_frame, writer=writer,
                    workbook=workbook, x=mx, y=my, title=title, legend=False)
            writer.save()

    def write_mass_csv(self):
        gradient, isotherm = self.load_dataframe()
        path = self.path

        def _writer(frames):
            for frame in frames:
                name = frame.columns
                frame.to_csv(os.path.join(path, "{}.csv".format(name)), sep=';')

        _writer(gradient)
        _writer(isotherm)
