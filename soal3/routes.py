from fastapi import APIRouter, Depends, HTTPException,status
import sqlalchemy
from sqlalchemy import Table
from db import conn, meta
from model import  tbl_cmb_bak
# import sys

# sys.setrecursionlimit(100000)

biak = APIRouter()


@biak.get("/get-data/")
async def get_data():
    query = conn.execute(tbl_cmb_bak.select()).fetchall()
    qry = sqlalchemy.select([tbl_cmb_bak.c.bayar_daftar,sqlalchemy.func.count(tbl_cmb_bak.c.bayar_daftar)]).group_by(tbl_cmb_bak.c.bayar_daftar)
    

    qry1 = conn.execute(qry).fetchall()
    if query == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Server Internal Error!')
    return {"status" : "success",
            "message" : "Data Berhasil Diperoleh",
            "data" : {
             "Jumlah Bayar" :qry1,
            "result data" : query} 
            }