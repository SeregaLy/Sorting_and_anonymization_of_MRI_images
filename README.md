# Sorting_and_anonymization_of_MRI_images
sorting and anonymization of MRI images

## Входные данные 

Находятся в данном репозитории в директории `src`

## Задание  

Ссылка на документацию `pydicom` - https://pydicom.github.io/pydicom/stable  
Выполнить преобразования входных данных, используя модуль `pydicom`. Необходимо сделать следующее:
* удалить информацию хранящуюся в ключе `PatientName` (анонимизировать файлы)
* используя информацию в ключах `StudyInstanceUID`, `SeriesInstanceUID`, `SOPInstanceUID` преобразовать структуру хранения файлов к следующей:
  1. на первом уровне `StudyInstanceUID`
  2. на втором уровне `SeriesInstanceUID`
  3. именем файла будет значение `SOPInstanceUID` с расширением `.dcm`

    Таким образом, путь к каждому файлу будет выглядеть так: `$StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm`

* дополнительно, нужно создать файл, в котором путь к каждому файлу исходной структуры сопоставлен пути к файлу в конечной структуре.
