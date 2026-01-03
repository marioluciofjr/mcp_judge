from mcp.server.fastmcp import FastMCP
from typing import Annotated
from pydantic import Field

# Inicializa o servidor FastMCP com o nome 'mcp-judge'
mcp = FastMCP("mcp-judge")

@mcp.tool(name="calcular_veredito")
def calcular_veredito(
    precisao: int,
    clareza: int,
    completude: int,
    alucinacao: int
) -> str:
    """
    Calcula o veredito final baseado nos scores parciais (1-5), aplicando pesos e penalidades lógicas.
    Pesos: Alucinação (40%), Precisão (30%), Completude (15%), Clareza (15%).
    Penalidades Críticas:
    - Se Alucinação <= 2 (Muita Alucinação): Score Final travado em 2.0 (Reprovado).
    - Se Precisão <= 2 (Incorreto): Score Final travado em 2.5 (Reprovado).
    """
    try:
        # Pesos
        w_aluc = 0.40
        w_prec = 0.30
        w_comp = 0.15
        w_clar = 0.15

        # Cálculo Ponderado
        score_base = (alucinacao * w_aluc) + (precisao * w_prec) + (completude * w_comp) + (clareza * w_clar)
        
        # Lógica de Penalidade (Computational Reasoning)
        penalidade_aplicada = None
        score_final = score_base

        if alucinacao <= 2:
            score_final = min(score_base, 2.0)
            penalidade_aplicada = "PENALIDADE CRÍTICA: Alto nível de alucinação detectado. Nota travada."
        elif precisao <= 2:
            score_final = min(score_base, 2.5)
            penalidade_aplicada = "PENALIDADE CRÍTICA: Baixa precisão factual. Nota travada."

        veredito_texto = "APROVADO" if score_final >= 4.0 else ("REQUER REVISÃO" if score_final >= 3.0 else "REPROVADO")

        return f"""
### Resultado do Cálculo Computacional
- **Score Base Calculado**: {score_base:.2f}
- **Penalidade Ativa**: {penalidade_aplicada if penalidade_aplicada else "Nenhuma"}
- **Score Final Oficial**: {score_final:.2f}
- **Veredito Matemático**: {veredito_texto}
"""
    except Exception as e:
        return f"Erro no cálculo: {str(e)}"

@mcp.prompt()
def prompt_juiz(
    input_usuario: Annotated[str, Field(description="O prompt ou pergunta original feita pelo usuário.")],
    output_modelo: Annotated[str, Field(description="A resposta gerada pelo modelo que deve ser avaliada.")]
) -> str:
    """
    Carrega o prompt com a persona 'LLM as a Judge' Crítico.
    Instrui o modelo a avaliar critérios e usar a tool 'calcular_veredito' para a nota oficial.
    """
    try:
        prompt = f"""
        ## persona
        Você é um Juiz de LLMs extremamente crítico (Computational Judge).
        Sua tarefa é avaliar a resposta, atribuir notas mentais para os critérios e, OBRIGATORIAMENTE, invocar a tool `calcular_veredito` para obter o resultado oficial.

        ## contexto
        ### Input Original
        ```text
        {input_usuario}
        ```

        ### Output do Modelo
        ```text
        {output_modelo}
        ```

        ## tarefa
        1. Analise criticamente o output.
        2. Defina mentalmente notas de 1 a 5 (inteiros) para:
           - Precisão (Fatos corretos?)
           - Clareza (Fácil de ler?)
           - Completude (Respondeu tudo?)
           - Alucinação (5 = Sem alucinação / Perfeito, 1 = Inventou tudo)
        3. CHAME a tool `calcular_veredito` passando essas notas.
        4. Use o retorno da tool para compor seu veredito final.

        ## formato
        
        ### Análise
        [Sua crítica detalhada, apontando erros específicos]

        ### Chamada de Tool
        [Aqui você deve ter invocado a tool e mostrar o resultado dela]

        ### Conclusão
        [Confirme o veredito dado pela tool]

        ## regras
        1. NÃO calcule a média manualmente. Use a tool.
        2. Se achar alucinação, dê nota baixa em alucinação (1 ou 2) para acionar a penalidade.
        3. Seja impiedoso.
        """
        return prompt
    except Exception as e:
         return f"Erro ao construir o prompt do juiz: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')

