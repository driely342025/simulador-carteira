import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Simulador de Carteira", layout="wide")

st.title("📊 Simulador de Diversificação de Investimentos")

# Entrada do usuário
valor = st.number_input("Digite o valor que deseja investir (R$):", min_value=100.0, step=100.0)

# Definição das classes de ativos
alocacao = {
    "Ações": 0.4,
    "Fundos Imobiliários": 0.3,
    "Renda Fixa": 0.2,
    "Caixa": 0.1
}

if valor > 0:
    # Calcula os valores
    dados = {"Classe": [], "Percentual": [], "Valor (R$)": []}
    for ativo, percentual in alocacao.items():
        dados["Classe"].append(ativo)
        dados["Percentual"].append(f"{percentual*100:.0f}%")
        dados["Valor (R$)"].append(valor * percentual)

    df = pd.DataFrame(dados)

    # Mostra a tabela
    st.subheader("📌 Distribuição da Carteira")
    st.table(df)

    # Gráfico de pizza
    fig = px.pie(df, values="Valor (R$)", names="Classe", title="Diversificação da Carteira", hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

    # Resumo
    st.success(f"✅ Valor total investido: R$ {valor:,.2f}")
