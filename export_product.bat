@echo off
REM Используем UTF-8
chcp 65001

REM Переходим в папку проекта
cd /d C:\jslesson\js_proect\myshop\

REM Активируем виртуальное окружение
call C:\jslesson\js_proect\myshop\venv\Scripts\activate.bat

REM Формируем имя лог-файла с датой и временем


REM Запускаем Django команду и добавляем вывод в лог
python manage.py export_products 

REM Выводим сообщение о завершении
echo ✔ Экспорт завершён, подробности в %LOG_FILE%

pause
