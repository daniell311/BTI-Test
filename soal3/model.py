from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db import meta

tbl_cmb_bak = Table(
    "tbl_cmb_bak",
    meta,
    Column("kode", String(255), primary_key=True),
    Column("bukaSmb", String(255)),
    Column("nomor", String(255)),
    Column("nama_lengkap", String(255)),
    Column("jalur_seleksi", String(255)),
    Column("bayar_daftar", String(255)),
    Column("daftar_ulang", String(255)),
    Column("nim", String(255)),
    Column("nama_sekolah", String(255)),
)
