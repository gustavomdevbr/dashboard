import streamlit as st
import pandas as pd
from meus_graficos import (
    gerar_grafico_barras, gerar_grafico_histograma,
    gerar_grafico_pizza, gerar_grafico_boxplot, gerar_grafico_dispersao
)

class Interface:
    def __init__(self):
        st.set_page_config(page_title="Dashboard de Dados", layout="wide")
        self.mostrar_cabecalho()
        self.mostrar_conteudo()
        self.upload_arquivo()

    def mostrar_cabecalho(self):
        st.header("Seja Bem-Vindo ao Centro de Controle")
        subtitulo = "<p style='font-size:17px; color:#58a6ff;'>Visualize dados. Tome decisões. Comande!</p>"
        st.markdown(subtitulo, unsafe_allow_html=True)

    def mostrar_conteudo(self):
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

        body {
            background: linear-gradient(135deg, #1e2a38, #0e1117);
            font-family: 'Poppins', sans-serif;
            color: #ddd;
        }

        .card {
            background: linear-gradient(145deg, #121a26, #0e1117);
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }

        .card-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 10px;
            text-align: center;
            color: #58a6ff;
        }

        .card-content {
            font-size: 16px;
            text-align: justify;
            color: #ccc;
        }

        div.stButton > button {
            background-color: #2563eb;
            color: white;
            padding: 10px 25px;
            border-radius: 8px;
            font-weight: 700;
            border: none;
            cursor: pointer;
        }

        div.stButton > button:hover {
            background-color: #1e40af;
            transform: scale(1.05);
        }

        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0e1117;
        }
        ::-webkit-scrollbar-thumb {
            background: #2563eb;
            border-radius: 10px;
        }
        </style>

        <div class="card">
            <div class="card-title">📊 Sobre o Dashboard</div>
            <div class="card-content">
                Este dashboard foi desenvolvido com o objetivo de <strong>facilitar a visualização de dados</strong> de forma prática e interativa.<br><br>
                Com ele, você pode:<br>
                ✅ Enviar arquivos nos formatos <code>.csv</code> ou <code>.xlsx</code> (Excel)<br>
                ✅ Visualizar automaticamente o conteúdo dos dados em formato de tabela<br>
                ✅ Gerar gráficos a partir das colunas numéricas para entender tendências e padrões<br>
                ✅ Analisar estatísticas básicas como média, desvio padrão, valores máximos e mínimos<br><br>
                Basta selecionar o arquivo desejado no menu lateral e o sistema fará o restante por você.<br>
                Ideal para análises rápidas, apresentações e decisões baseadas em dados — sem necessidade de programação.
            </div>
        </div>

        <div class="card">
            <div class="card-title">👨‍💻 Biografia</div>
            <div class="card-content">
                Gustavo Manoel da Silva é um jovem estudante de 20 anos, natural de Pernambuco, Brasil. Atualmente, está iniciando sua jornada no aprendizado da linguagem Python, dedicando-se a expandir seus conhecimentos em programação e desenvolvimento de projetos tecnológicos.<br><br>
                Gustavo concluiu o ensino médio na <strong>EREM Dom Vieira</strong>, uma escola de referência reconhecida como uma das melhores da Mata Norte de Pernambuco.<br><br>
                Com entusiasmo e compromisso, ele vem desenvolvendo soluções práticas como este dashboard, focando em aplicar seus aprendizados para gerar impacto e facilitar a análise de dados.
            </div>
        </div>
        """, unsafe_allow_html=True)

    def upload_arquivo(self):
        st.markdown("---")
        st.subheader("📁 Enviar Arquivo de Dados")

        arquivo = st.file_uploader("Escolha um arquivo CSV ou Excel", type=["csv", "xlsx"])

        if arquivo:
            try:
                df = pd.read_csv(arquivo) if arquivo.name.endswith('.csv') else pd.read_excel(arquivo)

                st.success("✅ Arquivo carregado com sucesso!")
                st.write("📄 Visualização dos dados:")
                st.dataframe(df)

                colunas_num = df.select_dtypes(include='number').columns.tolist()
                colunas_cat = df.select_dtypes(include='object').columns.tolist()

                if not colunas_num and not colunas_cat:
                    st.warning("⚠️ Nenhuma coluna categórica ou numérica encontrada.")
                    return

                st.subheader("📊 Gráficos Gerados")

                # Gráficos para colunas categóricas
                for col in colunas_cat:
                    st.markdown(f"### 📘 Coluna categórica: `{col}`")
                    gerar_grafico_barras(df, col)
                    gerar_grafico_pizza(df, col)

                # Gráficos para colunas numéricas
                for col in colunas_num:
                    st.markdown(f"### 📗 Coluna numérica: `{col}`")
                    gerar_grafico_histograma(df, col)
                    gerar_grafico_boxplot(df, col)

                # Gráfico de dispersão entre duas primeiras numéricas
                if len(colunas_num) >= 2:
                    st.markdown("### 📐 Gráfico de Dispersão")
                    gerar_grafico_dispersao(df, colunas_num[0], colunas_num[1])

            except Exception as e:
                st.error(f"❌ Erro ao processar o arquivo: {e}")
        else:
            st.info("🔄 Aguardando o envio de um arquivo...")

# Executa a aplicação
Interface()
