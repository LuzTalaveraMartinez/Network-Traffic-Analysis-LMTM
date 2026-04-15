# 🔍 Análisis de Tráfico de Red y Auditoría Forense - LMTM

**Autora:** Luz María Talavera Martínez  
**Fecha:** 15 de abril de 2026  
**Objetivo:** Verificación de integridad de red y auditoría de protocolos en infraestructura endurecida (Hardening 82/100).

---

## 🤖 Ingeniería de Seguridad Asistida por IA
Este proyecto documenta un proceso de **Vigilancia Proactiva** desarrollado bajo la guía de una Inteligencia Artificial que actuó como **Mentor y Arquitecto de Red**. El enfoque principal fue la transición de la ejecución manual a la **Automatización de Seguridad**, garantizando procesos repetibles y libres de error humano.

---

## 🛠️ Arsenal de Inspección y Automatización
Este proyecto utiliza herramientas de grado industrial y scripts personalizados para la vigilancia de activos:

*   **Nmap:** Escaneo de superficie para la detección de puertos abiertos y servicios activos.
*   **Tshark/Wireshark:** Captura y disección de paquetes en tiempo real para validación de cifrado.
*   **Scripts de Automatización (Ecosistema Dual):**
    *   `scripts/network_monitor.py`: Monitor avanzado en **Python** que orquesta escaneos y capturas forenses.
    *   `scripts/auto_network_audit.sh`: Script rápido en **Bash** para auditorías de red en caliente.

---

## 📊 Metodología de Validación
Se realizaron pruebas de interceptación de tráfico (Sniffing) sobre un nodo con Hardening Index de 82/100, obteniendo los siguientes resultados:

1.  **Aislamiento de puertos:** Se confirma mediante Nmap que el 99% de los puertos TCP permanecen en estado `closed (reset)`, mitigando vectores de ataque externos.
2.  **Verificación de Cifrado:** El análisis forense con Tshark confirmó que el 100% de la comunicación administrativa utiliza el protocolo **SSHv2**, con paquetes marcados como `Encrypted packet`.

---

## 📂 Archivos de Evidencia
A continuación se presentan las capturas de pantalla que demuestran el análisis realizado:

### 1. Escaneo de Red con Nmap
En esta fase se realizó un escaneo para identificar puertos abiertos en el host objetivo. Se detectó que únicamente el puerto **22 (SSH)** se encuentra activo, validando la reducción de la superficie de ataque.

![Escaneo de Nmap - Puerto 22](./img/nmap_attack_surface_scan.png)

### 2. Análisis de Tráfico con Tshark
Tras identificar el servicio SSH, se procedió a capturar y analizar el tráfico. En la imagen se observa el intercambio de paquetes cifrados entre el cliente y el servidor, garantizando la privacidad de la sesión.

![Análisis de Tráfico Tshark](./img/ssh_traffic_encryption_v2.3.png)

---

## 🚀 Guía de Despliegue Rápido
```bash
git clone https://github.com/LuzTalaveraMartinez/Network-Traffic-Analysis-LMTM
cd Network-Traffic-Analysis-LMTM
# Ejecutar monitor automático:
python3 scripts/network_monitor.py
