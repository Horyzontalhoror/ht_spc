@echo off
REM Aktifkan virtual environment
call venv\Scripts\activate

REM Jalankan aplikasi Python
python ht.py

REM Tunggu agar jendela tidak langsung tertutup (opsional)
pause
