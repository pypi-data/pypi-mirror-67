# common_python_programs

This library helps you in data clean up solutions and provides some commoly used functions

To use (with caution), simply do:

```
>>> import common_python_programs
>>> common_python_programs.drop_empty_rows_columns()
```

### Functions included in this package:
***
__*common_python_programs.drop_empty_rows_columns(dataframe):*__

**input:** pandas.dataframe type

**descrption:** drops all empty rows and columns which may contains white spaces or null values.

**returns**: preprocessed dataframe by dropping empty rows and columns
***

__*common_python_programs.get_files_in_directory(directory):*__

**input:** directory path, string type

**returns**: list of file names in the given directory path.
***

__*common_python_programs.data_frame_to_json(dataframe):*__

**input:** pandas.DataFrame type

**returns**: json format of dataframe
***

__*common_python_programs.file_to_html(file_path):*__

**input:** files with csv, excel extension

**returns:** table with html attributes

**additional info:** we can use this method to display data in browser using flask api

***

__*common_python_programs.upload_file(file_path):*__

**input:** location to save file

**returns:**  saves the file in the given path

**additional info:** we can use this method to browse the file to upload using flask api.

***


