:: -------------------------------------------------------------------------
::  Copyright 2026 Ratha SIV. All rights reserved.
::  Apache-2.0 license
:: -------------------------------------------------------------------------

@echo off
setlocal
cd /d %~dp0
python -W ignore indexation.py
pause
