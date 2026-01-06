# gft-viacep-case

## Visão Geral
Este projeto implementa um pipeline ETL em Python para leitura de uma lista de CEPs,
consulta ao serviço ViaCEP, tratamento de erros e geração de múltiplas saídas.

## Arquitetura
O projeto segue uma arquitetura ETL com separação de responsabilidades:
- Extract: leitura dos CEPs a partir de um CSV
- Transform: consulta ao endpoint do ViaCEP e normalização dos dados
- Load: persistência e geração de arquivos de saída
- Core: modelos e estruturas compartilhadas


## Qualidade
O projeto utiliza GitHub Actions para validação automática do código.
Atualmente, o pipeline executa lint com flake8.
