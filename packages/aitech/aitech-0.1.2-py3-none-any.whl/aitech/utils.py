import datetime
import os
import re
from collections import defaultdict

import pandas as pd

def write_yaml():
    tests = os.path.join(os.getcwd(), 'tests')
    return {'PROJECT DIRECTORY': tests, 'WAVE LENGTHS': [None, None, None, None], 'GRADIENT': 30, 'RMS': False}


def csv_list(file_path):
    root_dir = file_path
    files = []
    for dir_, _, files in os.walk(root_dir):
        files = [os.path.relpath(os.path.join(root_dir, dirpath, file), root_dir) for
                 (dirpath, dirnames, filenames) in os.walk(root_dir) for file in
                 filenames if re.match("^.*.csv$", file, flags=re.IGNORECASE)]

    compiled_pattern = r'.*compiled.*'
    if files:
        compiled_file = list(filter(lambda x: re.search(compiled_pattern, x), files))
        if compiled_file:
            files.remove(compiled_file[0])
    return files


def csv_list_multi(file_path: list, mode='csv'):
    from glob import glob
    files = []
    rms_files = []
    for file in file_path:
        files.append(glob(file + f"\\*.{mode}"))
    files = [f for y in files for f in y if f]
    rms_pattern = r'(RMS Intensity Profile)'
    compiled_pattern = r'(.*compiled.*)'
    if files:
        compiled_file = list(filter(lambda x: re.search(compiled_pattern, x), files))
        rms = list(filter(lambda x: re.search(rms_pattern, x), files))
        files = list(set(files) - set(compiled_file))
        rms_files.extend(rms)
    return {'standard': files, 'rms': rms_files}


def name(file):
    pattern = r"[_]([2]\d{6}.*)"
    lims_pattern = r'[_](\d{7})[_]'
    search_string = r'[a-zA-Z].+'
    free_text = re.search(search_string, file[:-4]).group(0)
    lims = re.search(lims_pattern, file).group(1)
    name = '_'.join([str(lims), free_text])
    return name


def excel_pathing(path, isograd):
    excel_path = os.path.join(path, f"{isograd}"
                                    f"_{datetime.date.today()}.xlsx")
    return excel_path


def find_nearest_non_null(f):
    for col in f.columns:
        df = f[col]
        if df.isnull().any():
            df[df.isnull().idxmax()] = df[df.isnull().idxmin()]


def topic_directories(path) -> (list, list):
    topics = [topic for topic in os.listdir(path) if re.search(r'^Topic', topic)]

    directories = [os.path.join(path, topic) for topic in topics if
                   os.path.isdir(os.path.join(path, topic))]

    return topics, directories


def method_directories(topic_paths, topics, isotherms=None):
    full = defaultdict(list)
    temp = defaultdict()
    md = _construct_methods_listing(isotherms)
    for topic_directory, topic in zip(topic_paths, topics):
        for key in md.keys():
            for item in md[key]:
                full[key].append(os.path.join(topic_directory, item))
        temp[topic] = full.copy()
        full.clear()
    return temp


def _construct_methods_listing(isotherms):
    methods = ['IR', 'MS', 'STA', 'TGA', 'GC']
    root = ['Data']
    type = ['Gradient', 'Isotherm']
    if not isotherms:
        isotherms = ['190', '220', '350']
    method_dict = defaultdict(list)
    for m in methods:
        for t in type:
            if t == 'Isotherm':
                for i in isotherms:
                    for r in root:
                        method_dict['isotherm'].append(f"{r}\\{t}\\{i}\\{m}")

            else:
                for r in root:
                    method_dict['gradient'].append(f"{r}\\{t}\\{m}")

    return method_dict


def chart_set_titles_axis(chart, x, y, title, legend, y2=None):
    font = "Palatino Linotype"
    color = "#333333"
    chart.set_x_axis({
        'name': x,
        'name_font': {
            'name': font,
            'color': color}})
    chart.set_y_axis({
        'name': y,
        'name_font': {
            'name': font,
            'color': color}})
    if y2:
        chart.set_y2_axis({
            'name': y2,
            'name_font': {
                'name': font,
                'color': color}})
    chart.set_legend({
        'none': legend})
    chart.set_title({
        'name': title,
        'name_font': {
            'name': font,
            'color': color}})
    chart.set_plotarea({
        'fill': {
            'color': '#FFFFCC',
            'transparency': 85}})


def normalize(df, feature: list = None):
    if feature:
        features = feature
    else:
        features = df.columns
    for feature_name in features:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        df[feature_name] = (
                ((df[feature_name] - min_value) / (max_value - min_value)) * 100)
    return df


def initilize_chart(frame, sheet_name, workbook, writer):
    frame.to_excel(writer, sheet_name=sheet_name)
    sample = list(frame.columns.unique(0))
    sample_frame = pd.DataFrame([sample])
    sample_frame.to_excel(writer, sheet_name=f"{sheet_name}_names")
    sample_names = f"{sheet_name}_names"
    chartsheet = workbook.add_chartsheet(f'{sheet_name}_chart')
    chartsheet.set_tab_color('#FF9900')
    chart = workbook.add_chart({
        'type': 'scatter',
        'subtype': 'smooth'})
    max_row = frame.last_valid_index() + 3
    return chart, chartsheet, max_row, sample, sample_names
