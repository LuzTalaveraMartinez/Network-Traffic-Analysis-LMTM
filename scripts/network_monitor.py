import subprocess
import os

def run_command(command, description):
    print(f"\n[+] {description}...")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error en la ejecución: {e}"

def main():
    print("================================================")
    print("   LMTM NETWORK MONITOR - Auditoría Proactiva   ")
    print("   Desarrollado por: Luz María Talavera Martínez.      ")
    print("================================================\n")

    # 1. Escaneo de Nmap
    nmap_cmd = ["sudo", "nmap", "-F", "127.0.0.1"]
    output = run_command(nmap_cmd, "Escaneando superficie de ataque (Nmap)")
    print(output)

    # 2. Captura con Tshark
    tshark_cmd = [
        "sudo", "tshark", "-i", "enp0s3", 
        "-a", "duration:5", 
        "-w", "/tmp/python_capture.pcap"
    ]
    run_command(tshark_cmd, "Capturando ráfaga de tráfico (5 segundos)")

    # 3. Mover y limpiar permisos
    output_file = os.path.expanduser("~/Network-Traffic-Analysis-LMTM/python_evidence.pcap")
    os.system(f"sudo mv /tmp/python_capture.pcap {output_file}")
    os.system(f"sudo chown $USER:$USER {output_file}")
    
    print(f"\n✅ Proceso Finalizado. Captura guardada en: {output_file}")

if __name__ == "__main__":
    main()
