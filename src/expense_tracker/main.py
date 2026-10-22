from expense_tracker.config import CAMINHO_DESPESAS
from expense_tracker.repositories.despesa_repository import DespesaRepository
from expense_tracker.services.despesa_service import DespesaService

def main():
    repositorio = DespesaRepository(CAMINHO_DESPESAS)
    servico = DespesaService(repositorio)
    print(servico.listar())

if __name__ == "__main__":
    main()