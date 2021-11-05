#!bin/bash

echo $YELLOW"[$RED!$YELLOW] Eu vou instalar as dependências essenciais pro bot funcinar você só concorda com os programas que vou instalar blz? [s/n]"
read inp
if [ "$inp" = "s" ]; then
   	apt update python3 && pkg install python3
   	pip install -r requirements.txt
    echo $GREEN"¡INSTALADO!"
fi
if [ "$inp" = "n" ]; then
    echo $RED"Bien ya puedes continuar, escribe: python3 do.py"
    exit
fi