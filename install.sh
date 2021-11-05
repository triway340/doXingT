#!bin/bash

echo $YELLOW"[$RED!$YELLOW] Vamos a instalar los requerimientos para usar este script, escriba 's' si continua, de lo contrario escriba 'n' (sin las comillas)[s/n]"
read inp
if [ "$inp" = "s" ]; then
   	pkg install python -y
   	pip install -r requirements.txt
    echo $GREEN"¡INSTALADO!"
fi
if [ "$inp" = "n" ]; then
    echo $RED"Bien ya puedes continuar, escribe: python3 do.py"
    exit
fi
