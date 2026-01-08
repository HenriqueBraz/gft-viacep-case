# gft-viacep-case

## Visão Geral

Este projeto implementa um **pipeline ETL em Python**, responsável por:

- Ler uma lista de CEPs a partir de um arquivo CSV  
- Consultar dados de endereço via serviço **ViaCEP**  
- Tratar falhas e inconsistências  
- Persistir os resultados em diferentes formatos  

O objetivo do projeto é demonstrar **boas práticas de engenharia de dados**, incluindo
arquitetura em camadas, paralelismo, testes automatizados e integração contínua.

---

## Arquitetura

O pipeline segue uma arquitetura **ETL clássica**, com separação clara de responsabilidades:

- **Extract**
  - Leitura dos CEPs a partir de um arquivo CSV
  - Validação e separação entre CEPs válidos e inválidos

- **Transform**
  - Enriquecimento dos CEPs válidos via integração com o ViaCEP
  - Processamento paralelo utilizando `ThreadPoolExecutor`
  - Tratamento de falhas, timeouts e retentativas controladas
  - Exibição de progresso durante a execução

- **Load**
  - Persistência dos dados em banco **SQLite**
  - Gravação dos resultados em arquivos **JSON** e **XML**
  - Gravação dos CEPs inválidos ou com falha em **CSV**
  - Armazenamento do payload completo retornado pelo ViaCEP (modelo híbrido)

- **Core**
  - Estruturas e utilidades compartilhadas entre as camadas

---

## Execução do Pipeline

### Preparar o ambiente

```
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# ou
.venv\Scripts\Activate     # Windows
pip install -r requirements.txt
```

### Gerar dados de entrada (opcional)
Os CEPs podem ser gerados localmente por meio do script generate_ceps.py

```
python app/scripts/generate_ceps.py
```
O arquivo CSV gerado é utilizado apenas como entrada do ETL e não é versionado.

### Executar o pipeline

```
python app/main.py
```
Durante a execução, o progresso da etapa de transformação é exibido no terminal.

### Integração com ViaCEP e Modo Mock
Em alguns ambientes (ex.: redes corporativas ou institucionais), o acesso ao endpoint
do ViaCEP pode estar bloqueado por restrições de rede.

Para esses casos, o projeto oferece um modo mock, que simula a resposta do ViaCEP
sem alterar a arquitetura do pipeline.

Ativando o modo mock

 - PowerShell (Windows)

```
$env:USE_MOCK_VIACEP="true"
python app/main.py
```
 - Linux / macOS

```
export USE_MOCK_VIACEP=true
python app/main.py
```
O modo mock é utilizado apenas para execução local e não altera o comportamento
esperado em produção.

### Qualidade e Testes
O projeto adota práticas de qualidade de código, incluindo:

 - Testes unitários para as camadas Extract, Transform e Load

 - Mock de dependências externas (ViaCEP) nos testes

 - Lint automático com flake8

 - Integração contínua com GitHub Actions

Os testes podem ser executados localmente com:

```
pytest
```

### Dados de Saída
Os arquivos gerados pelo pipeline incluem:

 - addresses.json – endereços válidos em formato JSON

 - addresses.xml – endereços válidos em formato XML

 - errors.csv – CEPs inválidos ou que falharam no processamento

No repositório, são versionadas apenas amostras de saída para fins de demonstração.
Os dados completos gerados em execuções locais são ignorados via .gitignore.

### Observações Finais

Este projeto foi desenvolvido com foco em:

 - Clareza arquitetural

 - Robustez frente a falhas externas

 - Facilidade de manutenção

 - Boas práticas de engenharia de dados

O pipeline pode ser facilmente adaptado para execução em ambientes distribuídos,
processamento em batch ou integração com orquestradores como Airflow.



