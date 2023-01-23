@echo off
net start TobiiGeneric || net stop TobiiGeneric
net start TobiiIS5LARGEPCEYE5 || net stop TobiiIS5LARGEPCEYE5
net start "Tobii Service" || net stop "Tobii Service"

pause