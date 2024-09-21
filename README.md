# Project Setup Instructions

## Requirements
- **Python Version**: Python >= 3.9

## Setting up Python Virtual Environment

### MacOS / Linux
1. Open terminal.
2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
3. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
4. Upgrade `pip`:
    ```bash
    python -m pip install --upgrade pip
    ```

### Windows
1. Open command prompt (cmd) or PowerShell.
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```
4. Upgrade `pip`:
    ```bash
    python -m pip install --upgrade pip
    ```

## Installing PaddlePaddle and PaddleOCR

### For MacOS / Linux / Windows (Without GPU):
To install PaddlePaddle, run the following command:
```bash
python -m pip install paddlepaddle
```

### For MacOS/ Linux/ Windows (With GPU):
```bash
pip install paddlepaddle-gpu
```

Next, install PaddleOCR:
```bash
pip install "paddleocr>=2.0.1"
```
#### For windows users: 
If you getting this error OSError: [WinError 126] The specified module could not be found when you install shapely on windows. Please try to download Shapely whl file. You can refer to here: https://stackoverflow.com/questions/44398265/install-shapely-oserror-winerror-126-the-specified-module-could-not-be-found

### Run OCR
```bash
python predict.py
```