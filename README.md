
# AffinityAnswers Internship Questions

This repository contains solutions to questions asked for the AffinityAnswers internship.

---

## Q1. OLX Car Cover Search

**Task:**  
Search for "Car Cover" on OLX using [www.olx.in/items/q-car-cover](https://www.olx.in/items/q-car-cover) and write a Python program to save the search results to a file.

**[View Code](https://github.com/c0dem0de/AffinityAnswers/blob/main/olx-ads.py)**

### Usage

1. **Set up a virtual environment:**
    ```sh
    python -m venv venv
    ```

2. **Install dependencies:**
    ```sh
    pip install httpx selectolax
    ```

3. **Run the script:**
    ```sh
    python olx-ads.py
    ```

---

## Q2. Extract Scheme Name and Asset Value from AMFI

**Task:**  
Write a shell script to extract 'Scheme Name' and 'Asset Value' from [NAVAll.txt](https://www.amfiindia.com/spages/NAVAll.txt) and save the results as a TSV file.

**[View Code](https://github.com/c0dem0de/AffinityAnswers/blob/main/scheme-NAV.sh)**


### Should this data be in JSON instead?

> CSV and TSV formats are best suited for simple, tabular visualisation and needs to be opened in softwares like Excel.  
> If the data were more complex, with nested structures or relationships between different tables, using a JSON format would be more appropriate apporach, as it can represent hierarchical data more effectively.

---
