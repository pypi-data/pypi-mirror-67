import pandas as pd
from aitech.utils import csv_list_multi, excel_pathing, chart_set_titles_axis, initilize_chart


class IR:

    def __init__(self, path, root, wavelengths, gradient=10, startingtemp=30, rms=False):
        self.root = root
        self.path = path
        self.st = startingtemp
        self.wl = wavelengths
        self.rms = rms
        self.gradient = gradient
        self.gradient_frames = self.load_dataframe().get('gradient')
        self.isotherm_frames = self.load_dataframe().get('isotherm')

    def load_dataframe(self):
        gradient = self.path.get('gradient')
        isotherm = self.path.get('isotherm')
        gradient_files = csv_list_multi(gradient)
        isotherm_files = csv_list_multi(isotherm)

        def _helper(csv_dictionary):
            standard_dictionary = {}
            rms_dictionary = {}
            i = 1
            csv_standard = csv_dictionary.get('standard')
            csv_rms = csv_dictionary.get('rms')

            for file in csv_standard:
                df = pd.read_csv(file, engine='python',
                                 header=3).dropna().transpose()
                header = df.iloc[0]
                header = header.astype(float).astype(int)
                ir_frame = df[1:]
                ir_frame.columns = header
                local_name = file.split('_')[-1][:-4]
                if standard_dictionary.get(local_name):
                    local_name = local_name + f"_{i}"
                    i = +1
                standard_dictionary[local_name] = ir_frame
            i = 1
            for file in csv_rms:
                ir_frame = pd.read_csv(file, engine='python',
                                       header=2).dropna()

                name = file.split('_')[-1][:-9]
                if rms_dictionary.get(name):
                    name = name + f"_{i}"
                    i = +1
                rms_dictionary[name] = ir_frame
            return {'standard': standard_dictionary, 'rms': rms_dictionary}

        gradient_dictionary = _helper(gradient_files)
        isotherm_dictionary = _helper(isotherm_files)
        return {'gradient': gradient_dictionary, 'isotherm': isotherm_dictionary}


    def wl_ext(self):
        wavelength = self.wl
        if not wavelength:
            return {'gradient': {}, 'isotherm': {}}

        gradient_frames = self.gradient_frames.get('standard')
        isotherm_frames = self.isotherm_frames.get('standard')

        def _helper(frames):
            frame_dictionary = {}
            for name, frame in frames.items():
                wave_list = []
                for wl in wavelength:
                    try:
                        wave_list.append(frame[wl])
                    except KeyError:
                        def jitter(jitter_frame, n):
                            return n if n in jitter_frame.columns else jitter(
                                jitter_frame, n + 1)

                        wave_list.append(frame[jitter(frame, wl + 1)])
                temp = pd.DataFrame(wave_list).transpose()
                frame_dictionary[name] = temp
            return frame_dictionary

        gradient_dictionary = _helper(gradient_frames)
        isotherm_dictionary = _helper(isotherm_frames)

        return {
            'gradient': gradient_dictionary,
            'isotherm': isotherm_dictionary
        }

    def rms_ext(self):
        if not self.rms:
            return {'gradient': {}, 'isotherm': {}}
        gradient_frames = self.gradient_frames.get('rms')
        isotherm_frames = self.isotherm_frames.get('rms')
        return {
            'gradient': gradient_frames,
            'isotherm': isotherm_frames
        }

    def ch(self, frame, legend, **kwargs):
        name = kwargs.get('name')
        writer = kwargs.get('writer')
        workbook = kwargs.get('workbook')
        x = kwargs.get('x')
        y = kwargs.get('y')
        title = kwargs.get('title')

        from itertools import product
        frame.to_excel(writer, sheet_name=name)

        samples = list(frame.columns.unique(0))

        # Product returns a tuple for whatever reason
        sample_names = pd.DataFrame(list(map(lambda _: f"{_[0]} - {str(_[1])}", list(
            product(samples, self.wl))))).transpose()

        sample_names.to_excel(writer, sheet_name=f"{name}_names")
        legend_names = f"{name}_names"

        chartsheet = workbook.add_chartsheet(f'{name}_chart')
        chartsheet.set_tab_color('#FF9900')

        chart = workbook.add_chart({
            'type': 'scatter',
            'subtype': 'smooth'})

        name_field = 1
        time_field = 1
        wave_index = 1
        max_row = frame.index.size + 3
        for i, sample_name in enumerate(samples):
            waves = len(list(frame[sample_name].columns)) - 1
            for wave in range(waves):
                cat_field = time_field + (wave + 1)
                chart.add_series({
                    'name': [legend_names, 1, wave_index],
                    'categories': [name, 3, time_field, max_row, time_field],
                    'values': [name, 3, cat_field, max_row, cat_field], })
                wave_index += 1

            name_field = name_field + (waves + 1)
            time_field = time_field + (waves + 1)
        chart_set_titles_axis(chart, x, y, title, legend)

        chartsheet.set_chart(chart)

    def ch_rms(self, frame, legend=True, **kwargs):
        name = kwargs.get('name')+'_RMS'
        writer = kwargs.get('writer')
        workbook = kwargs.get('workbook')
        x = kwargs.get('x')
        y = kwargs.get('y')
        title = kwargs.get('title')

        chart, chartsheet, max_row, sample, sample_names = initilize_chart(frame,
                                                                           name,
                                                                           workbook,
                                                                           writer)

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

    def run(self):
        def _helper(frames, isograd):
            ir_dict = {}
            for name, frame in frames.items():
                temp = frame.reset_index()
                temp['index'] = temp['index'].str.replace("(\.\d+)$", "")
                if isograd == 'isotherm':
                    temp["index"] = temp['index'].astype(float).map(
                        lambda x: x / 60).round(3)
                    temp.rename(columns={
                        'index': 'Time'}, inplace=True)
                if isograd == 'gradient':
                    temp["index"] = temp['index'].astype(float).apply(
                        lambda x: 30 + ((x / 60) * self.gradient))
                    temp.rename(columns={
                        'index': 'Temperature'}, inplace=True)
                ir_dict[name] = temp
            frame = pd.concat(ir_dict.values(), axis=1, keys=list(ir_dict.keys()))
            return frame

        def _kwargs(isograd):
            name = f"IR_{isograd}"
            excel_path = excel_pathing(self.root, name)
            writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
            workbook = writer.book
            if isograd == 'isotherm':
                mx = "Time (min)"
                my = "Absorbance"
            else:
                mx = "Sample Temperature (°C)"
                my = "Absorbance"
            title = "IR"
            return {
                "name": name,
                "excel_path": excel_path,
                "writer": writer,
                "workbook": workbook,
                "x": mx,
                "y": my,
                "title": title}

        def _rms_helper(frames, isograd):
            ir_dict = {}
            for name, frame in frames.items():
                if isograd == 'gradient':
                    frame["Time (secs)"] = frame['Time (secs)'].astype(float).apply(
                        lambda x: 30 + ((x / 60) * self.gradient))
                    frame.rename(columns={
                        'Time (secs)': 'Temperature'}, inplace=True)
                if isograd == 'isotherm':
                    frame["Time (secs)"] = frame['Time (secs)'].astype(float).map(
                        lambda x: x / 60).round(3)
                ir_dict[name] = frame
            h_frame = pd.concat(ir_dict.values(), axis=1, keys=list(ir_dict.keys()))
            return h_frame

        if self.wl:
            for k, v in self.wl_ext().items():
                if v:
                    params = _kwargs(k)
                    ir_frame = _helper(v, k)
                    self.ch(frame=ir_frame, legend=True, **params)
                    params.get('writer').save()
        if self.rms:
            for k, v in self.rms_ext().items():
                if v:
                    params = _kwargs(k)
                    ir_frame = _rms_helper(v, k)
                    self.ch_rms(frame=ir_frame, legend=True, **params)
                    params.get('writer').save()


        # gradient_params = _gradient()  # gradient_ir_frame = _helper(gradient, False)  # self.ch_wl(frame=gradient_ir_frame, legend=False, **gradient_params)  # gradient_params.get('writer').save()
