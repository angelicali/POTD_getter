@echo off
REM ^ is the little-known BAT file line continuation...

REM Build POTD-getter
pyinstaller --noconfirm ^
			--log-level=WARN ^
			--onefile ^
			--console ^
			--name "POTD_getter"^
			"chrome_webdriver.py"




echo.
echo ################################################
echo #               POTD Getter built              #
echo ################################################
echo.

REM Done!
echo ------------------------------------------------
echo ^|                                              ^|
echo ^| - - -  Finished building all programs  - - - ^|
echo ^|                                              ^|
echo ------------------------------------------------
echo.
pause