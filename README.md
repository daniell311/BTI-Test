# BTI-Test

How to Run soal2

1. Instal virtual environment using this following command
   "pip install virtualenv"
2. create Virtual Environment with name "venv" using this following command
    "virtualenv venv"
3. Change directory to ././soal2
4. activate virtualenv with the following command
  .\venv\Scripts\activate

5. create MySQL Database name "user" 

6. Install the requirement with the following command
  pip install -r requirements.txt

7. Run program using uvicorn server with this following command
uvicorn main:app --reload


How to Run Soal3

1. Instal virtual environment using this following command
   "pip install virtualenv"
2. create Virtual Environment with name "venv" using this following command
    "virtualenv venv"
3. Change directory to ././soal3
4. activate virtualenv with the following command
  .\venv\Scripts\activate

5. create MySQL Database name "user" 
6. Import database "tbl_cmb_bak" to local MySQL

7. Install the requirement with the following command
  pip install -r requirements.txt

6. Run program using uvicorn server with this following command
uvicorn main:app --reload
