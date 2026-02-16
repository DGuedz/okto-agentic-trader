#!/bin/bash

# Configuração do ambiente para otimização de assets (Okto)

VENV_DIR="venv"
REQUIREMENTS="Pillow"

echo "🐙 Okto Asset Optimizer Setup"
echo "----------------------------"

# 1. Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale o Python 3."
    exit 1
fi

# 2. Criar Virtual Environment se não existir
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Criando ambiente virtual ($VENV_DIR)..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "❌ Falha ao criar venv."
        exit 1
    fi
else
    echo "✅ Ambiente virtual encontrado."
fi

# 3. Ativar e Instalar Dependências
source "$VENV_DIR/bin/activate"
echo "⬇️  Instalando dependências ($REQUIREMENTS)..."
pip install $REQUIREMENTS > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Dependências instaladas."
else
    echo "❌ Falha ao instalar dependências."
    exit 1
fi

# 4. Executar Otimizador (se argumento for passado)
if [ ! -z "$1" ]; then
    echo "🚀 Otimizando: $1"
    python3 ops/optimize_image.py "$1"
else
    echo "ℹ️  Uso: ./optimize_assets.sh <caminho_da_imagem>"
    echo "    Exemplo: ./optimize_assets.sh okto-huge.png"
fi

echo "----------------------------"
