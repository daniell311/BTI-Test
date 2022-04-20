from pydantic import BaseModel

class Biak(BaseModel):
    kode: str
    bukaSmb: str
    nomor: str
    nama_lengkap: str
    jalur_seleksi: str
    bayar_daftar: str
    daftar_ulang: str
    nim: str
    nama_sekolah: str
