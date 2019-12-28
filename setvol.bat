@echo off
set /a volume=%1 * 655
nircmd setvolume 0 %volume% %volume%