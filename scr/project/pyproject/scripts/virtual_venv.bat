@echo off
chcp 65001

@REM path to project
set project_path=%1
set python_path=%2

cd %project_path%

call %python_path% -m venv .venv

