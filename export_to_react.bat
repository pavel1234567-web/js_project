
@echo off

cd  c:\jslesson\js_proect\myshop\

call c:\jslesson\js_proect\venv\Scripts\activate

python manage.py export_products

 pause
