@echo off
chcp 65001

set path=%1
set name=%2

cd %path%
mkdir %name%
cd %name%

mkdir .pypad

