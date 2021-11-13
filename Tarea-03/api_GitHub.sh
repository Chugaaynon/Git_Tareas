#!/usr/bin/env bash

usuario="keydet89"

echo -e "\n Esta es la informacion del usuario: $usuario\n"
curl "https://api.github.com/users/$usuario"
echo -n "Presiona enter para continuar: "
read


echo -e "\n Repos de: $usuario\n"
curl "https://api.github.com/users/$usuario/repos?tab=repositories"
#echo -n "Ingrese un repo a investigar issues:"  # RegRipper3.0
#read issues
echo -n "Presiona enter para continuar: "
read


issues="RegRipper3.0"
echo -e "\n Issues del repo: $issues\n"
curl "https://api.github.com/repos/$usuario/$issues/issues"
#echo -n "Ingrese un repo a investigar contribuidores:"  # RegRipper3.0
#read repo
echo -n "Presiona enter para continuar: "
read


repo="RegRipper3.0"
echo -e "\n Contribuidores del repo: $repo\n"
curl "https://api.github.com/repos/$usuario/$repo/contributors"
echo -n "Presiona enter para continuar: "
read


repo="Tools"
echo -e "\n Contribuidores del repo: $repo\n"
curl "https://api.github.com/repos/$usuario/$repo/contributors"
echo -n "Presiona enter para continuar: "
read