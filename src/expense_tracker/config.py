from pathlib import Path

DIRETORIO_BASE = Path(__file__).resolve().parents[2] # dois níveis abaixo da raiz
CAMINHO_DESPESAS = DIRETORIO_BASE / "data" / "despesas.json"