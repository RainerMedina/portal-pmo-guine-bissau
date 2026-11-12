import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA (LARGURA TOTAL)
# ==========================================
st.set_page_config(
    page_title="Gabinete do Primeiro-Ministro | República da Guiné-Bissau",
    page_icon="🇬🇼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CSS FULL-BLEED (100% DA TELA DE PONTA A PONTA)
# ==========================================
st.markdown("""
<style>
    /* Remove margens e limites do Streamlit para preencher 100% do ecrã */
    #MainMenu, header, footer {visibility: hidden;}
    .stApp {
        background-color: #ffffff;
    }
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    [data-testid="stVerticalBlock"] {
        gap: 0rem !important;
    }

    /* 1. Barra Superior Oficial .gov.gw */
    .gov-masthead {
        width: 100%;
        background-color: #f3f4f6;
        border-bottom: 1px solid #e5e7eb;
        padding: 6px 5%;
        font-size: 13px;
        color: #374151;
    }

    /* 2. Barra de Alerta Institucional (Estilo Singapura) */
    .gov-alert-bar {
        width: 100%;
        background-color: #eef2ff;
        border-bottom: 1px solid #c7d2fe;
        padding: 12px 5%;
        font-size: 13.5px;
        color: #1e3a8a;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Faixa Tricolor Guiné-Bissau */
    .tricolor-bar {
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #CE1126 0%, #CE1126 33.3%, #FCD116 33.3%, #FCD116 66.6%, #009E49 66.6%, #009E49 100%);
    }

    /* 3. Cabeçalho Branco Full-Width */
    .pmo-navbar {
        width: 100%;
        background-color: #ffffff;
        padding: 16px 5%;
        border-bottom: 1px solid #e5e7eb;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .pmo-brand {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .pmo-emblem {
        width: 48px;
        height: 48px;
        background-color: #CE1126;
        color: #000000;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        border: 3px solid #FCD116;
        flex-shrink: 0;
    }
    .pmo-title-sub {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #6b7280;
        font-weight: 700;
        margin: 0;
    }
    .pmo-title-main {
        font-size: 22px;
        font-weight: 800;
        color: #111827;
        margin: 0;
        line-height: 1.1;
    }

    /* 4. Hero Split-Screen (Vermelho à Esquerda + Imagem à Direita) */
    .hero-split {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        min-height: 430px;
        background-color: #b91c1c;
    }
    .hero-left {
        flex: 1 1 50%;
        background-color: #b91c1c; /* Vermelho Institucional */
        color: #ffffff;
        padding: 60px 5% 60px 8%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .hero-left h1 {
        font-size: 42px;
        font-weight: 800;
        margin: 0 0 16px 0;
        line-height: 1.15;
        color: #ffffff;
    }
    .hero-left p {
        font-size: 18px;
        line-height: 1.5;
        color: #fee2e2;
        margin: 0 0 28px 0;
        max-width: 540px;
    }
    .hero-right {
        flex: 1 1 50%;
        min-height: 360px;
        background-image: linear-gradient(to right, rgba(185, 28, 28, 0.25), rgba(17, 24, 39, 0.45)),
                          url('https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=1200&q=80');
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: flex-end;
        padding: 28px;
    }
    .hero-caption-box {
        background: rgba(17, 24, 39, 0.85);
        border-left: 4px solid #FCD116;
        color: #ffffff;
        padding: 12px 18px;
        font-size: 13px;
        border-radius: 2px;
    }

    /* Container interno com respiro lateral elegante para o conteúdo abaixo do Hero */
    .content-wrapper {
        padding: 36px 5% 50px 5%;
        background-color: #ffffff;
    }

    /* Cards da Sala de Imprensa */
    .news-card {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-top: 4px solid #009E49;
        border-radius: 4px;
        padding: 22px;
        margin-bottom: 14px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .news-meta {
        font-size: 12px;
        color: #009E49;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .news-title {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 10px;
        line-height: 1.35;
    }
    .news-excerpt {
        font-size: 14px;
        color: #4b5563;
        line-height: 1.55;
    }

    /* Estilização da barra de abas para parecer menu horizontal */
    .stTabs [data-baseweb="tab-list"] {
        padding: 0 5%;
        background-color: #f9fafb;
        border-bottom: 1px solid #e5e7eb;
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        font-weight: 600;
        font-size: 15px;
    }

    /* Rodapé Full-Width */
    .pmo-footer {
        width: 100%;
        background-color: #111827;
        color: #9ca3af;
        padding: 44px 5%;
        font-size: 13.5px;
        margin-top: 40px;
    }
    .pmo-footer h4 {
        color: #ffffff;
        font-size: 16px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BASE DE DADOS (COMUNICADOS E DISCURSOS)
# ==========================================
COMUNICADOS = [
    {
        "id": 1,
        "categoria": "Comunicados de Imprensa",
        "data": "12 de Novembro de 2026",
        "titulo": "Conselho de Ministros aprova Plano Nacional de Modernização Digital e Infraestruturas",
        "resumo": "O Executivo reuniu-se em Bissau para aprovar o pacote de investimentos destinado à digitalização dos serviços públicos e reabilitação das vias estruturantes.",
        "conteudo": """
        **BISSAU, 12 de Novembro de 2026** — Reunido hoje em sessão ordinária no Palácio do Governo, o Conselho de Ministros, presidido por Sua Excelência o Primeiro-Ministro da República da Guiné-Bissau, aprovou o Plano Nacional de Modernização Digital e Infraestruturas (2026–2030).

        **Principais medidas aprovadas:**
        - Criação do Portal Único do Cidadão (`.gov.gw`) para emissão digital de documentos essenciais;
        - Reabilitação prioritária dos eixos rodoviários de escoamento da produção agrícola nas regiões de Bafatá, Gabú e Oio;
        - Reforço da transparência orçamental e auditoria trimestral às empresas públicas.
        """
    },
    {
        "id": 2,
        "categoria": "Discursos",
        "data": "04 de Novembro de 2026",
        "titulo": "Discurso de Sua Excelência o Primeiro-Ministro na Cimeira Económica da CEDEAO",
        "resumo": "Intervenção centrada na integração comercial regional, segurança alimentar e transição energética na África Ocidental.",
        "conteudo": """
        **Excelências, Chefes de Estado e de Governo,**

        A Guiné-Bissau apresenta-se hoje perante a nossa comunidade regional com uma mensagem clara de compromisso com a paz, a boa governação e a integração económica efetiva.

        O nosso país detém um potencial agrícola e marítimo extraordinário. Estamos a trabalhar para transformar a cadeia de valor do caju, modernizar o Porto de Bissau e garantir que a juventude guineense tenha acesso à formação técnica e ao empreendedorismo digital.
        """
    },
    {
        "id": 3,
        "categoria": "Relações Internacionais",
        "data": "28 de Outubro de 2026",
        "titulo": "Audiência com a Delegação da União Europeia e Parceiros de Desenvolvimento",
        "resumo": "Avaliação dos programas de cooperação nas áreas da educação, saúde materno-infantil e energias renováveis.",
        "conteudo": """
        **BISSAU, 28 de Outubro de 2026** — Sua Excelência o Primeiro-Ministro recebeu hoje, no Palácio do Governo, uma delegação de alto nível composta por representantes da União Europeia e agências das Nações Unidas para avaliar os projetos de eletrificação rural e equipamento hospitalar.
        """
    }
]

@st.dialog("Documento Oficial — Gabinete do Primeiro-Ministro", width="large")
def abrir_documento(item):
    st.caption(f"{item['categoria'].upper()}  |  {item['data']}")
    st.subheader(item["titulo"])
    st.divider()
    st.markdown(item["conteudo"])
    st.divider()
    st.caption("Gabinete de Comunicação e Informação • Palácio do Governo, Bissau, República da Guiné-Bissau")

# ==========================================
# TOPO INSTITUCIONAL (.GOV.GW + AVISO)
# ==========================================
st.markdown("""
<div class="gov-masthead">
    🇬🇼 <strong>Portal Oficial do Governo da República da Guiné-Bissau</strong>  |  Domínio institucional verificado (<code>.gov.gw</code>)
</div>
<div class="gov-alert-bar">
    <span>ℹ️</span>
    <span><strong>Aviso Oficial:</strong> Os membros do Governo nunca solicitam transferências financeiras nem dados bancários por telefone. Verifique sempre o endereço oficial <code>.gov.gw</code>.</span>
</div>
<div class="tricolor-bar"></div>
<div class="pmo-navbar">
    <div class="pmo-brand">
        <div class="pmo-emblem">★</div>
        <div>
            <p class="pmo-title-sub">República da Guiné-Bissau</p>
            <h1 class="pmo-title-main">Gabinete do Primeiro-Ministro</h1>
        </div>
    </div>
    <div style="font-size: 13px; color: #4b5563; font-weight: 600;">
        PT  |  KRI  |  FR
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# NAVEGAÇÃO HORIZONTAL FULL-WIDTH
# ==========================================
tab_inicio, tab_pm, tab_governo, tab_imprensa, tab_contacto = st.tabs([
    "Início",
    "O Primeiro-Ministro",
    "Conselho de Ministros",
    "Sala de Imprensa",
    "Contactos"
])

# ==========================================
# ABA 1: INÍCIO (COM HERO SPLIT FULL-SCREEN)
# ==========================================
with tab_inicio:
    # Banner Hero de ponta a ponta (Vermelho à esquerda + Foto à direita)
    st.markdown("""
    <div class="hero-split">
        <div class="hero-left">
            <h1>Gabinete do Primeiro-Ministro</h1>
            <p>Destaque: Intervenção de Sua Excelência o Primeiro-Ministro sobre a Reforma Administrativa, Estabilidade e Desenvolvimento Económico da Guiné-Bissau.</p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                <span style="background: #ffffff; color: #b91c1c; padding: 10px 22px; font-weight: 700; border-radius: 3px; font-size: 14px;">Ler comunicado</span>
                <span style="border: 1.5px solid #ffffff; color: #ffffff; padding: 10px 22px; font-weight: 700; border-radius: 3px; font-size: 14px;">Sala de Imprensa</span>
            </div>
        </div>
        <div class="hero-right">
            <div class="hero-caption-box">
                <strong>DISCURSO DE ABERTURA</strong><br>
                Presidência do Conselho de Ministros • Palácio do Governo, Bissau
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Conteúdo abaixo do banner com espaçamento lateral limpo
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    
    col_t, col_s = st.columns([2, 1])
    with col_t:
        st.subheader("Últimas Notícias e Comunicados")
    with col_s:
        busca = st.text_input("Pesquisar", placeholder="🔍 Pesquisar no portal...", label_visibility="collapsed")

    st.write("")
    resultados = [
        c for c in COMUNICADOS
        if busca.lower() in c["titulo"].lower() or busca.lower() in c["resumo"].lower()
    ]

    cols = st.columns(3)
    for idx, item in enumerate(resultados):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="news-card">
                <div class="news-meta">{item['categoria']} • {item['data']}</div>
                <div class="news-title">{item['titulo']}</div>
                <div class="news-excerpt">{item['resumo']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Ler artigo completo →", key=f"home_art_{item['id']}"):
                abrir_documento(item)

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ABA 2: O PRIMEIRO-MINISTRO
# ==========================================
with tab_pm:
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.subheader("Chefia do Governo da República da Guiné-Bissau")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.info("🏛️ **Palácio do Governo**\n\nPraça dos Heróis Nacionais\n\nBissau, Guiné-Bissau")
    with c2:
        st.markdown("""
        Nos termos da Constituição da República da Guiné-Bissau, o Primeiro-Ministro é o Chefe do Governo, competindo-lhe dirigir e coordenar a ação governativa e assegurar o funcionamento harmonioso das instituições da administração pública.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ABA 3: CONSELHO DE MINISTROS
# ==========================================
with tab_governo:
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.subheader("Estrutura do Executivo e Ministérios")
    ministerios = [
        ("Ministério dos Negócios Estrangeiros, Cooperação Internacional e das Comunidades", "Política externa, diplomacia e apoio à diáspora guineense."),
        ("Ministério das Finanças", "Orçamento Geral do Estado, política fiscal, tesouro e aduanas."),
        ("Ministério da Administração Interna e Ordem Pública", "Segurança interna, proteção civil e administração territorial."),
        ("Ministério da Justiça e dos Direitos Humanos", "Modernização judicial, registos, notariado e promoção dos direitos humanos."),
        ("Ministério da Economia, Plano e Integração Regional", "Planeamento estratégico, promoção do investimento e integração na CEDEAO/UEMOA."),
        ("Ministério da Educação Nacional, Ensino Superior e Investigação Científica", "Ensino básico, secundário, universidades e capacitação docente."),
        ("Ministério da Saúde Pública", "Rede hospitalar nacional, saúde preventiva e programas materno-infantis."),
        ("Ministério da Agricultura e Desenvolvimento Rural", "Segurança alimentar, apoio aos produtores e fileira do caju.")
    ]
    for nome, desc in ministerios:
        with st.expander(f"🏛️ {nome}"):
            st.write(desc)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ABA 4: SALA DE IMPRENSA
# ==========================================
with tab_imprensa:
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.subheader("Sala de Imprensa e Arquivo Oficial")
    for item in COMUNICADOS:
        with st.container(border=True):
            st.caption(f"**{item['categoria'].upper()}** | {item['data']}")
            st.markdown(f"#### {item['titulo']}")
            st.write(item["resumo"])
            if st.button("Ler documento", key=f"news_btn_{item['id']}"):
                abrir_documento(item)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ABA 5: CONTACTOS
# ==========================================
with tab_contacto:
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.subheader("Atendimento Institucional")
    st.write("**Sede:** Palácio do Governo, Caixa Postal 37, Bissau — República da Guiné-Bissau")
    st.write("**E-mail Institucional:** `imprensa@pmo.gov.gw`")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# RODAPÉ FULL-WIDTH
# ==========================================
st.markdown("""
<div class="pmo-footer">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div>
            <h4>Gabinete do Primeiro-Ministro</h4>
            <p>República da Guiné-Bissau • Unidade, Luta, Progresso</p>
        </div>
        <div>
            <h4>Ligações Institucionais</h4>
            <p>Presidência da República • Assembleia Nacional Popular • Boletim Oficial</p>
        </div>
    </div>
    <hr style="border-color: #374151; margin: 20px 0;">
    <p style="margin: 0; font-size: 12px;">© 2026 Governo da República da Guiné-Bissau. Todos os direitos reservados.</p>
</div>
""", unsafe_allow_html=True)
