from collections import defaultdict
import yaml
import aitech
import os
import argparse

def main():
    def represent_none(self, _):
        return self.represent_scalar('tag:yaml.org,2002:null', '')

    yaml.add_representer(type(None), represent_none)

    parameters = os.path.join(os.getcwd(), "parameter.yaml")
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='root path')

    try:
        with open(parameters, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
            gradient, method_paths, rms, root, wavelenths = decomporess(data_loaded)
            try:
                _run(method_paths, root, gradient, wavelenths, rms)
            except TypeError:
                print("Please double-check your parameters.yaml document'")
                os.startfile(os.path.join(os.getcwd(), 'parameters.yaml'))
    except FileNotFoundError:
        data_loaded = aitech.utils.write_yaml()
        with open('parameter.yaml', 'w') as outfile:
            yaml.dump(data_loaded, outfile, default_flow_style=False)
        print("Please fill out the parameter.yaml document")
        os.startfile(os.path.join(os.getcwd(), 'parameters.yaml'))


def decomporess(data_loaded):
    root = data_loaded.get('PROJECT DIRECTORY')
    topics, topic_paths = aitech.topic_directories(root)
    method_paths = aitech.method_directories(topic_paths, topics)
    wavelenths = data_loaded.get('WAVE LENGTHS')
    gradient = data_loaded.get('GRADIENT')
    rms = data_loaded.get('RMS')
    return gradient, method_paths, rms, root, wavelenths


def _run(method_paths, path, gradient, wl, rms):
    ir_list = defaultdict(list)
    ms_list = defaultdict(list)
    sta_list = defaultdict(list)
    gc_list = defaultdict(list)

    print("Running")
    for topic in method_paths.keys():
        for isograd in method_paths[topic].keys():
            for method in method_paths[topic][isograd]:
                technique = method.split('\\')[-1]
                if technique == 'IR':
                    ir_list[isograd].append(method)
                if technique == 'STA':
                    sta_list[isograd].append(method)
                if technique == 'MS':
                    ms_list[isograd].append(method)
                if technique == 'GC':
                    gc_list[isograd].append(method)
    mIR = aitech.IR(path=ir_list, root=path, wavelengths=wl, rms=rms)
    mIR.run()
    print("IR Done")
    run_sta = aitech.STA(path=sta_list, root=path, gradients=gradient)
    run_sta.run()
    print("STA Done")
    run_ms = aitech.MS(path=ms_list, gc=False, root=path)
    run_ms.run_excel()
    run_gc = aitech.MS(path=gc_list, gc=True, root=path)
    run_gc.run_excel()
    print("MS Done")


if __name__ == "__main__":
    main()
