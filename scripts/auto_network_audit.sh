#!/bin/bash
# =================================================================
# Auditor de Red Automático LMTM v1.0
# Desarrollado por: Luz María Talavera Martínez
# =================================================================

echo "--- 🔍 Iniciando Auditoría de Red LMTM ---"

# 1. Escaneo de superficie (Nmap)
echo "[+] Verificando puertos abiertos en localhost..."
sudo nmap -F 127.0.0.1 | grep "open"

# 2. Captura de tráfico (Tshark)
echo "[+] Capturando 10 segundos de tráfico forense..."
sudo tshark -i enp0s3 -a duration:10 -w /tmp/scan_temp.pcap

# 3. Mover y limpiar (lo dejamos en la carpeta raíz del repo)
mv /tmp/scan_temp.pcap ../evidencia_red.pcap
sudo chown $USER:$USER ../evidencia_red.pcap
chmod 644 ../evidencia_red.pcap

echo "--- ✅ Auditoría completada ---"
echo "Evidencia guardada en la raíz del repo como: evidencia_red.pcap"
