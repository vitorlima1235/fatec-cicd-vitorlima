# FATEC CI/CD - Pipeline de Integração Contínua e Entrega Contínua

> Projeto de demonstração de um **pipeline CI/CD seguro** com análise de segurança (CodeQL), testes automatizados e deploy para ambiente de stage.

## 📋 Visão Geral

Este projeto implementa um pipeline CI/CD completo usando **GitHub Actions** que:

1. ✅ **Analisa segurança** com CodeQL (detecta vulnerabilidades como SQL Injection)
2. 🧪 **Executa testes automatizados** com pytest
3. 📊 **Verifica qualidade do código** com flake8
4. 🚀 **Faz deploy** para ambiente de stage

## 🏗️ Estrutura do Projeto

```
fatec-cicd-vitorlima/
├── .github/
│   ├── workflows/
│   │   ├── ci-cd-pipeline.yml      # Workflow principal com 3 jobs
│   │   └── codeql.yml              # Análise CodeQL
│   └── codeql-config.yml           # Configuração de análise
├── main.py                          # Código Python funcional
├── tests/
│   └── test_main.py                # Suite de testes
├── requirements.txt                # Dependências do projeto
├── .gitignore                      # Arquivos ignorados pelo Git
└── README.md                       # Este arquivo
```

## 🚀 Pipeline CI/CD

## 📊 Teste 1: Código Seguro → ✅ Todos os Jobs Verdes

### Resultado Esperado
- ✅ **Job 1 (CodeQL)** → PASSOU
- ✅ **Job 2 (Testes)** → PASSOU  
- ✅ **Job 3 (Deploy)** → PASSOU

### Evidência
<img width="1278" height="261" alt="image" src="https://github.com/user-attachments/assets/b7995e1c-ebd1-4c50-9141-91e6b7776fd3" />

## ❌ Teste 2: Código Vulnerável → Job 1 Falha

<img width="1192" height="268" alt="image" src="https://github.com/user-attachments/assets/88dcb479-542b-4fd3-841a-06cd1985224e" />

### Resultado Observado
- ❌ **Job 1 (CodeQL)** → **FALHOU** (detectou vulnerabilidade)
- ⬜ **Job 2 (Testes)** → NÃO EXECUTOU (bloqueado pela falha)
- ⬜ **Job 3 (Deploy)** → NÃO EXECUTOU (bloqueado pela falha)

## ✅ Teste 3: Correção Aplicada → Pipeline Verde Novamente

<img width="1093" height="282" alt="{E13AB6C6-E2A7-400D-B30E-D84CB20D7C90}" src="https://github.com/user-attachments/assets/659b4fb0-4230-4f19-86e5-937f509b3e07" />


### Resultado
- ✅ **Job 1 (CodeQL)** → PASSOU (nenhuma vulnerabilidade)
- ✅ **Job 2 (Testes)** → PASSOU (testes executados com sucesso)
- ✅ **Job 3 (Deploy)** → PASSOU (deployment concluído)

## 🔐 Configurações de Segurança

### GitHub Advanced Security
- ✅ CodeQL habilitado
- ✅ Code scanning alerts ativo
- ✅ Dependabot habilitado



## 🎯 Aprendizados Principais

1. **CodeQL como guardião de segurança** - Bloqueia código vulnerável antes do deploy
2. **Pipeline como barreira de qualidade** - Garante que apenas código testado entra em produção
3. **Automação reduz riscos** - Detecta vulnerabilidades sem intervenção manual
4. **Segurança desde o início** - Análise de segurança é o primeiro job, não o último

## 🔗 Links Úteis

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [CodeQL Documentation](https://codeql.github.com/)
- [OWASP SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)

---

**Status:** ✅ CI/CD Pipeline 100% Funcional e Seguro | Todos os testes passando 🟢
