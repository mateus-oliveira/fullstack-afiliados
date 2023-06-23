# Fullstack Afiliados

Backend da aplicação.

### Como executar
 
- Antes de mais nada, tenha certeza de ter o Docker e o Python 3.10 instalados
- Clone este projeto e então navegue até a pasta do repositório
- Ative um novo ambiente virtual com os seguintes comandos:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Execute os seguintes comandos para construir as imagens e iniciar os contêineres:
```bash
sudo docker compose build
sudo docker compose up -d
```