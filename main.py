import csv
import os
from pathlib import Path
import pydicom as py


def get_data(dcm_file: str):
    """function returns a generator object with all dicom files in the given
    folder"""
    if Path(dcm_file).exists():
        for dcm_file in Path(dcm_file).iterdir():
            if dcm_file.is_file():
                yield dcm_file
    else:
        print('FileNotFoundError')


def new_file_path(data_set: py.FileDataset):
    """function creates a new file path for the given dataset"""
    output_folder = (processed_set / data_set['StudyInstanceUID'].value
                     / data_set['SeriesInstanceUID'].value)
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    file_name = data_set['SOPInstanceUID'].value + '.dcm'
    return output_folder / file_name


def save_mapping(data: dict[str, str]):
    """function saves mapping"""

    with open(csv_file, 'w', newline='', encoding='utf-8') as file_dict:
        writer = csv.DictWriter(file_dict, fieldnames=['src', 'out'])
        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'src': key, 'out': value})


if __name__ == '__main__':
    original_set = str(Path('src'))
    processed_set = Path('result')
    csv_file = 'file_map.csv'
    mapping = dict()
    for file in get_data(original_set):
        dataset = py.dcmread(file)
        dataset.PatientName = None
        with open(new_file_path(dataset), 'wb') as outfile:
            dataset.save_as(outfile)
            mapping.update({file: outfile.name})
    save_mapping(mapping)
