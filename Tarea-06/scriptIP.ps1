function funcIP {
    #  IP local
    Get-NetIPAddress -AddressFamily IPv4


    #  IP publica
    Invoke-WebRequest ifconfig.me | Select-Object -Expand Content


    #  Segmento de red privado
    nmap 192.168.0.16/24


    #  Escaneo a una IP con un script
    nmap -p 23 --script telnet-ntlm-info 192.168.0.1   # CAMBIAR


    #  Escaneo a una IP publica
    nmap github.com
}

funcIP > reporte.txt

$archivo = Get-Content .\reporte.txt
$encode = [System.Text.Encoding]::UTF8.GetBytes($archivo)
[System.Convert]::ToBase64String($encode) > .\reporte_encode.txt