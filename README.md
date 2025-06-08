# 🐾 FindMyPet - API de Localização de Animais 

API desenvolvida para consulta de localização de animais perdidos, integrada com a plataforma ThingSpeak (IoT).

## 👨‍💻 Participantes
- Davi Alves de Lima - RM 556008
- Pedro Henrique Mendonça de Novais – RM 555276
- Rodrigo Alcides Bohac Ríos – RM 554826

## ⚙️ Funcionamento
A API utiliza dados provenientes do ThingSpeak (canais de IoT) onde:
- `field1`: Latitude
- `field2`: Longitude
- `field3`: Status (0: perdido, 1: encontrado)
- `field4`: ID do animal

O endpoint `/find` busca os dados mais recentes do animal pelo seu ID.

## 🔧 Pré-requisitos
- Python 3.8+
- Bibliotecas: `Flask` e `requests`

## 🚀 Instalação
```bash
# Clone o repositório (se aplicável)
git clone https://github.com/seu-usuario/findmypet-api-iot.git
cd findmypet-api-iot
```

# Instale as dependências
```bash
pip install -r requirements.txt
```

##🏃 Executando a API
```bash
python main.py
```

##🔍 Endpoints
#1. Página Inicial
URL: /

Método: GET

Exemplo:
```bash
curl http://localhost:5000/
```

Resposta:
```bash
Bem-vindo a api de consulta de buscas FindMyPet!
```

#2. Busca animal por id
URL: /find

Método: GET

Exemplo:
```bash
curl "http://localhost:5000/find?id=4347"
```

Resposta de sucesso:
```bash
{
  "entry_id": 16,
  "created_at": "2025-06-08T15:34:10Z",
  "latitude": "-23.54720",
  "longitude": "-46.62360",
  "status": "0",
  "animal_id": "4347"
}
```

Resposta de erro:
```bash
{"error": "Animal com ID 9999 não encontrado"}
```

