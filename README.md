# BTI-Test

How to Run soal2

1. Change directory to ././soal2
2. Instal virtual environment using this following command
   "pip install virtualenv"
3. create Virtual Environment with name "venv" using this following command
    "virtualenv venv" 
4. activate virtualenv with the following command using command prompt
  ".\venv\Scripts\activate"
5. create MySQL Database name "user" 
6. Install the requirement with the following command
  "pip install -r requirements.txt"
7. Run program using uvicorn server with this following command
"uvicorn main:app --reload"


How to Run Soal3

1. Change directory to "././soal3"
2. Instal virtual environment using this following command
   "pip install virtualenv"
3. create Virtual Environment with name "venv" using this following command
    "virtualenv venv"
4. activate virtualenv with the following command using command prompt
  ".\venv\Scripts\activate"
5. create MySQL Database name "user" 
6. Import database "tbl_cmb_bak" to database that has been created on step 5
7. Install the requirement with the following command
  "pip install -r requirements.txt"
8. Run program using uvicorn server with this following command
  "uvicorn main:app --reload"
