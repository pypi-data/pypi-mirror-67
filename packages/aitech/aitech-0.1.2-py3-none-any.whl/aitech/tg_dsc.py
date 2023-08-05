import os
import re
import pandas as pd
import glob
from aitech.utils import (excel_pathing, csv_list_multi, chart_set_titles_axis,
                          initilize_chart)
from numpy import inf, nan


def derivative(df):
    df = df.iloc[40:]
    delta = df[['Time', 'Unsubtracted Weight']].diff().dropna()
    delta['Unsubtracted Weight'] = delta['Unsubtracted Weight'].ewm(span=50).mean(

        ).div(delta['Time'])

    delta = pd.concat([delta, df['Sample Temperature']], axis=1).dropna()

    return delta


class TgDsc:

    def __init__(self, path, root, tg_columns=None, dsc_columns=None,
                 calibration=False, topic=None, isotherms=None, gradients=None):

        if isotherms is None:
            isotherms = [190, 220]
        if gradients is None:
            gradients = [10]
        self.calibration = calibration
        self.root = root
        self.path = path
        self.topic = topic
        self.isotherms = isotherms
        self.gradients = gradients

        if tg_columns is None:
            self.tg_cols = ["Time", "Unsubtracted Weight", 'Sample Temperature']
        else:
            self.tg_cols = tg_columns

        if dsc_columns is None:
            self.dsc_cols = ["Time", "Unsubtracted Heat Flow", 'Sample Temperature']
        else:
            self.dsc_cols = dsc_columns

        self.use_cols = self.tg_cols + self.dsc_cols

        # Procedural classes ...

    def ch(self, name, frame, writer, workbook, x, y, title, y2=None, legend=True):
        def color_list(n):
            color_list = ["black", "blue", "red", "green", "navy", "purple", "cyan",
                          "gray", "brown", "lime", "#4f2f2f", "#666699", "#7f00ff",
                          "#8e2323", "#93db70", "#99ccff"]
            return color_list[n % len(color_list)]
        chart, chartsheet, max_row, sample, sample_names = initilize_chart(frame,
                                                                           name,
                                                                           workbook,
                                                                           writer)

        for i, sample_name in enumerate(sample):
            color = color_list(i)
            if y2:
                weight = (i * 3) + 2
                temp = (i * 3) + 3
                time = (i * 3) + 1
                chart.add_series({
                    'name': [sample_names, 1, i + 1],
                    'categories': [name, 3, time, max_row, time],
                    'values': [name, 3, weight, max_row, weight],
                    'line': {
                        "color": color}})
                chart.add_series({
                    'name': [sample_names, 1, i + 1],
                    'categories': [name, 3, time, max_row, time],
                    'values': [name, 3, temp, max_row, temp],
                    'y2_axis': 1,
                    'line': {
                        "color": color,
                        'dash_type': 'long_dash'}})
            if not y2:
                weight = (i * 3) + 2
                temp = (i * 3) + 3
                chart.add_series({
                    'name': [sample_names, 1, i + 1],
                    'categories': [name, 3, temp, max_row, temp],
                    'values': [name, 3, weight, max_row, weight],
                    'line': {
                        "color": color}})

        chart_set_titles_axis(chart, x, y, title, legend, y2)
        chart.set_style(4)
        chartsheet.set_chart(chart)

    def run(self):

        def frame_generator(frames, isograd):
            tg_dict = {}
            tg_frame_corrected_dict = {}
            dsc_dict = {}
            tg_derivative_dict = {}
            calibration = {}

            if isograd == 'isotherm':
                pattern = r'(?<=isotherm )(\d{0,3})'
                iso = self.isotherms
                isothermal_calibrations = [' '.join([str(x), f'{isograd} Baseline'])
                                           for x in iso]
                for cal in isothermal_calibrations:
                    if cal in frames.keys():
                        calibration[cal] = frames.pop(cal)
            else:
                pattern = r'gradient'
                grad = self.gradients
                gradient_calibrations = [' '.join([str(x), f'{isograd} Baseline'])
                                         for x in grad]
                for cal in gradient_calibrations:
                    if cal in frames.keys():
                        calibration[cal] = frames.pop(cal)

            for name, frame in frames.items():
                temp_tg = frame.filter(self.tg_cols)

                # mass TG
                tg_dict[name] = temp_tg

                # Percent TG
                temp_tg_corrected = temp_tg.copy(deep=True)
                temp_tg_corrected['Unsubtracted Weight'] = temp_tg_corrected[
                    'Unsubtracted Weight'].div(
                    temp_tg_corrected['Unsubtracted Weight'].max())
                temp_tg_corrected['Unsubtracted Weight'] = temp_tg_corrected[
                    'Unsubtracted Weight'].multiply(100)

                tg_frame_corrected_dict[name] = temp_tg_corrected

                # mass TG Derivative
                if isograd == 'gradient':
                    temp_tg_derivative = derivative(temp_tg)
                    tg_derivative_dict[name] = temp_tg_derivative.replace(
                        [inf, -inf], nan).dropna()

                # DSC
                temp_dsc = frame.filter(self.dsc_cols)

                if isograd == 'isotherm':
                    extract_temp = re.findall(pattern, name)
                    if extract_temp:
                        keys = calibration.keys()
                        f = list(filter(lambda x: extract_temp[0] in x, keys))
                        if f:
                            f = f[0]
                            c = calibration[f]
                            column = 'Unsubtracted Heat Flow'
                            temp_dsc[column] = temp_dsc[column] - c[column]
                if isograd == 'gradient':
                    c = calibration.get('10 Gradient Baseline')
                    if c:
                        column = 'Unsubtracted Heat Flow'
                        temp_dsc[column] = temp_dsc[column] - c[column]

                dsc_dict[name] = temp_dsc

            def f(item):
                ff = []
                if item:
                    ff = pd.concat(item.values(), axis=1, keys=list(item.keys()))
                return ff

            tg_frame = f(tg_dict)
            dsc_frame = f(dsc_dict)
            tg_derivative = f(tg_derivative_dict)
            tg_frame_corrected = f(tg_frame_corrected_dict)

            return {
                'tg_frame': tg_frame,
                'tg_frame_corrected': tg_frame_corrected,
                'dsc_frame': dsc_frame,
                'tg_derivative': tg_derivative}

        def frame_finisher(isograd, **complete):
            tg_frame = complete.get('tg_frame')
            tg_frame_corrected = complete.get("tg_frame_corrected")
            dsc_frame = complete.get("dsc_frame")
            tg_derivative = complete.get('tg_derivative')
            writer = complete.get('writer')
            workbook = complete.get('workbook')
            tx = complete.get('tx')
            ty = complete.get('ty')
            ttitle = complete.get('ttitle')
            tyd = complete.get('tyd')
            ty2 = complete.get('ty2')
            dxtitle = complete.get('dxtitle')
            tyc = complete.get("tyc")
            dy2 = complete.get("dy2")
            dtitle = complete.get("dtitle")
            dx = complete.get("dx")
            dy = complete.get("dy")

            self.ch("tg", tg_frame, writer, workbook, x=tx, y=ty, title=ttitle,
                    y2=ty2, legend=True)

            if isograd == 'gradient':
                if "tg_derivative" in complete.keys():
                    self.ch("tg_derivative", tg_derivative, writer, workbook, x=tx,
                            y=tyd, title=dxtitle, y2=ty2, legend=True)

            self.ch("tg_percent", tg_frame_corrected, writer, workbook, x=tx, y=tyc,
                    title=ttitle, y2=ty2, legend=True)
            self.ch("DSC", dsc_frame, writer, workbook, x=dx, y=dy, title=dtitle,
                    y2=dy2, legend=True)

            tg_frame.to_excel(writer, sheet_name="raw tg")
            dsc_frame.to_excel(writer, sheet_name='raw dsc')

            writer.save()

        def _kwargs(isograd):
            name = f"TG_{isograd}"
            excel_path = excel_pathing(self.root, name)
            writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
            workbook = writer.book

            ty = "Weight loss (mg)"
            tyc = 'Percent mass (%)'
            ttitle = "TGA"
            dx = "Time (min)"
            dy = "Heat Flow Endo Up (mW)"
            dy2 = "Sample Temperature (°C)"
            dtitle = "DSC"
            ty2 = None
            ttitle = None
            dtitle = None
            tyd = None
            dxtitle = None
            tx = None

            if isograd == 'isotherm':
                tx = "Time (min)"
                ty2 = "Sample Temperature (°C)"
            if isograd == 'gradient':
                tx = "Sample Temperature (°C)"
                tyd = "d/dx"
                dxtitle = "TGA Derivative"

            return {
                "name": name,
                "excel_path": excel_path,
                "writer": writer,
                "workbook": workbook,
                "tx": tx,
                "ty": ty,
                "tyc": tyc,
                "ty2": ty2,
                "tyd": tyd,
                "dxtitle": dxtitle,
                "ttitle": ttitle,
                "dx": dx,
                "dy": dy,
                "dy2": dy2,
                "dtitle": dtitle}

        for k, v in self.load_dsc().items():
            if v:
                params = _kwargs(k)
                sta_frame = frame_generator(v, k)
                sta_frame.update(params)
                frame_finisher(k, **sta_frame)

    def load_dsc(self):
        gradient = self.path.get('gradient')
        isotherm = self.path.get('isotherm')
        gradient_files = csv_list_multi(gradient).get('standard')
        isotherm_files = csv_list_multi(isotherm).get('standard')

        def _helper(csv, isotherm_data):
            i = 0
            frame_dictionary = {}
            calibration_file = self.calibration_check(isotherm_data)
            if calibration_file:
                for calibration, calibration_data in calibration_file.items():
                    if self.use_cols:
                        df = pd.read_csv(calibration_data, engine='python',
                                         usecols=self.use_cols)
                    else:
                        df = pd.read_csv(calibration_data, engine='python')
                    frame_dictionary[calibration] = df

            for file in csv:
                if self.use_cols:
                    df = pd.read_csv(file, engine='python', usecols=self.use_cols)
                else:
                    df = pd.read_csv(file, engine='python')

                local_name = file.split('_')[-1][:-4]
                thermal_frame = df

                if local_name in frame_dictionary.keys():
                    local_name += f"_{i}"
                    i = +1
                frame_dictionary[local_name] = thermal_frame
            return frame_dictionary

        gradient_dictionary = _helper(gradient_files, False)
        isotherm_dictionary = _helper(isotherm_files, True)
        return {
            'gradient': gradient_dictionary,
            'isotherm': isotherm_dictionary}

    def calibration_check(self, isotherm):
        calibration_paths = glob.glob(self.root + '\\Parameter\\*')

        if isotherm:
            p = 'Isotherm Baseline'
        else:
            p = 'Gradient Baseline'

        calibration_dict = {}
        for path in calibration_paths:
            for r, d, f in os.walk(path):
                if re.search(p, r):
                    if list(filter(lambda x: os.path.splitext(x)[-1] == '.csv', f)):
                        baseline = list(
                            filter(lambda x: os.path.splitext(x)[-1] == '.csv', f))
                        base_name = [os.path.splitext(x)[0] for x in baseline]
                        file_list = list(map(lambda x: os.path.join(r, x), baseline))
                        for k, v in zip(base_name, file_list):
                            calibration_dict[k] = v
        return calibration_dict
