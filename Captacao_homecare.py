pacientes = []

while True:

    print("\n--- Cadastro de Paciente Home Care ---")

    nome = input("Nome: ")
    idade = input("Idade: ")
    mae = input("Nome da mãe: ")
    nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    hd = input("Hipótese diagnóstica: ")
    dispositivos = input("Dispositivos utilizados: ")
    complexidade = input("Grau de complexidade: ")
    tempo = input("Tempo na condição: ")
    cuidados = input("Descreva os cuidados necessários: ")

    paciente = {
        "Nome": nome,
        "Idade": idade,
        "Mãe": mae,
        "Nascimento": nascimento,
        "CPF": cpf,
        "Endereço": endereco,
        "HD": hd,
        "Dispositivos": dispositivos,
        "Complexidade": complexidade,
        "Tempo": tempo,
        "Cuidados": cuidados
    }

    pacientes.append(paciente)

    print("\nPaciente cadastrado!")

    continuar = input("Cadastrar outro paciente? (s/n): ")

    if continuar.lower() != "s":
        break

print("\nPacientes cadastrados:")

for p in pacientes:
    print(p)
