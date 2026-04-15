# 🔍 Análisis de Tráfico de Red y Auditoría Forense - LMTM

**Autora:** Luz María Talavera Martínez  
**Fecha:** 15 de abril de 2026  
**Objetivo:** Verificación de integridad de red y auditoría de protocolos en infraestructura endurecida.

---

## 🛠️ Arsenal de Inspección
Este proyecto documenta el uso de herramientas de grado industrial para la vigilancia de activos:
*   **Nmap:** Escaneo de superficie para la detección de puertos abiertos y servicios activos.
*   **Tshark/Wireshark:** Captura y disección de paquetes en tiempo real para validación de cifrado.

## 📊 Metodología de Validación
Se realizaron pruebas de interceptación de tráfico (Sniffing) sobre un nodo con Hardening Index de 82/100, obteniendo los siguientes resultados:
1.  **Aislamiento de Puertos:** Se confirmó mediante Nmap que el 99% de los puertos TCP permanecen en estado `closed (reset)`, mitigando vectores de ataque externos.
2.  **Verificación de Cifrado:** El análisis forense con Tshark confirmó que el 100% de la comunicación administrativa utiliza el protocolo **SSHv2**, con paquetes marcados como `Encrypted packet`.

## 📂 Archivos de Evidencia
*   `mi_captura.pcap`: Captura de tráfico real analizada (60KB de datos forenses).
---
**Mentoría IA:** Proyecto desarrollado bajo consultoría avanzada de arquitectura de seguridad.
