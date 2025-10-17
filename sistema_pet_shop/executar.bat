@echo off
echo ================================
echo    SISTEMA PET SHOP - LAUNCHER
echo ================================
echo.
echo Escolha uma opcao:
echo 1. Executar Sistema Completo
echo 2. Executar Interface Grafica
echo 3. Executar Exemplo de Demonstracao
echo 4. Sair
echo.
set /p opcao="Digite sua opcao (1-4): "

if "%opcao%"=="1" (
    python PetShop_Vitor.py
) else if "%opcao%"=="2" (
    python interface_grafica.py
) else if "%opcao%"=="3" (
    python exemplo_teste.py
) else if "%opcao%"=="4" (
    echo Saindo...
    exit
) else (
    echo Opcao invalida!
    pause
)

pause