# BTI-Test

How to Run soal2

1. Change directory to ././soal2
2. activate virtualenv with the following command
  .\venv\Scripts\activate

3. create MySQL Database name "user" 

4. Install the requirement with the following command
  pip install -r requirements.txt

5. Run program using uvicorn server with this following command
uvicorn main:app --reload


How to Run Soal3

1. Change directory to ././soal3
2. activate virtualenv with the following command
  .\venv\Scripts\activate

3. create MySQL Database name "user" 
4. Import database "tbl_cmb_bak" to local MySQL

5. Install the requirement with the following command
  pip install -r requirements.txt

6. Run program using uvicorn server with this following command
uvicorn main:app --reload
