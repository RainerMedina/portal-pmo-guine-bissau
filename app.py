import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Gabinete do Primeiro-Ministro | República da Guiné-Bissau",
    page_icon="🇬🇼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# ESTILIZAÇÃO INSTITUCIONAL (ESTILO PMO.GOV.SG)
# ==========================================
st.markdown("""
<style>
    /* Ocultar barra padrão do Streamlit para visual institucional limpo */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 2rem;
        max-width: 1180px;
    }

    /* Barra Superior Oficial .gov.gw */
    .gov-masthead {
        background-color: #f3f4f6;
        border-bottom: 1px solid #e5e7eb;
        padding: 6px 20px;
        font-size: 13px;
        color: #374151;
        margin-bottom: 0px;
        border-radius: 0 0 4px 4px;
    }

    /* Faixa Tricolor Guiné-Bissau */
    .tricolor-bar {
        height: 5px;
        background: linear-gradient(90deg, #CE1126 0%, #CE1126 33.3%, #FCD116 33.3%, #FCD116 66.6%, #009E49 66.6%, #009E49 100%);
        margin-bottom: 20px;
    }

    /* Cabeçalho Principal */
    .pmo-header {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 10px 0 20px 0;
        border-bottom: 1px solid #e5e7eb;
    }
    .pmo-emblem {
        width: 58px;
        height: 58px;
        background-color: #CE1126;
        color: #000000;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        font-weight: bold;
        border: 3px solid #FCD116;
        flex-shrink: 0;
    }
    .pmo-title-sub {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #6b7280;
        font-weight: 600;
        margin: 0;
    }
    .pmo-title-main {
        font-size: 26px;
        font-weight: 700;
        color: #111827;
        margin: 0;
        line-height: 1.2;
    }

    /* Banner Hero (Destaque Principal) */
    .hero-card {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        color: white;
        padding: 36px;
        border-radius: 6px;
        border-left: 6px solid #CE1126;
        margin: 20px 0 30px 0;
    }
    .hero-tag {
        background-color: #FCD116;
        color: #111827;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 3px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .hero-heading {
        font-size: 28px;
        font-weight: 700;
        margin-top: 14px;
        margin-bottom: 12px;
        line-height: 1.3;
    }
    .hero-desc {
        font-size: 15px;
        color: #d1d5db;
        line-height: 1.6;
        max-width: 820px;
    }

    /* Cards de Notícias / Sala de Imprensa */
    .news-card {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-top: 3px solid #009E49;
        border-radius: 4px;
        padding: 20px;
        height: 100%;
        margin-bottom: 12px;
    }
    .news-meta {
        font-size: 12px;
        color: #6b7280;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .news-title {
        font-size: 17px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
        line-height: 1.35;
    }
    .news-excerpt {
        font-size: 14px;
        color: #4b5563;
        line-height: 1.5;
    }

    /* Rodapé Oficial */
    .pmo-footer {
        background-color: #111827;
        color: #9ca3af;
        padding: 32px 24px;
        border-radius: 6px;
        margin-top: 40px;
        font-size: 13px;
    }
    .pmo-footer h4 {
        color: #ffffff;
        font-size: 15px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BASE DE DADOS (SALA DE IMPRENSA E ATOS)
# ==========================================
COMUNICADOS = [
    {
        "id": 1,
        "categoria": "Comunicados de Imprensa",
        "data": "10 de Novembro de 2026",
        "titulo": "Conselho de Ministros aprova Plano Nacional de Modernização Digital e Infraestruturas",
        "resumo": "O Executivo reuniu-se em Bissau para aprovar o pacote de investimentos destinado à digitalização dos serviços públicos e reabilitação das vias estruturantes.",
        "conteudo": """
        **BISSAU, 10 de Novembro de 2026** — Reunido hoje em sessão ordinária no Palácio do Governo, o Conselho de Ministros, presidido por Sua Excelência o Primeiro-Ministro da República da Guiné-Bissau, aprovou o Plano Nacional de Modernização Digital e Infraestruturas (2026–2030).

        **Principais medidas aprovadas:**
        - Criação do Portal Único do Cidadão (`.gov.gw`) para emissão digital de documentos essenciais;
        - Reabilitação prioritária dos eixos rodoviários de escoamento da produção agrícola nas regiões de Bafatá, Gabú e Oio;
        - Reforço da transparência orçamental e auditoria trimestral às empresas públicas.

        O Primeiro-Ministro sublinhou que a estabilidade institucional e a eficiência administrativa são pilares indispensáveis para atrair investimento direto e melhorar a qualidade de vida das famílias guineenses.
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
        **Distintos Delegados,**

        A Guiné-Bissau apresenta-se hoje perante a nossa comunidade regional com uma mensagem clara de compromisso com a paz, a boa governação e a integração económica efetiva.

        O nosso país detém um potencial agrícola e marítimo extraordinário. Estamos a trabalhar para transformar a cadeia de valor do caju, modernizar o Porto de Bissau e garantir que a juventude guineense tenha acesso à formação técnica e ao empreendedorismo digital.

        Reiteramos o nosso apelo à cooperação solidária entre os Estados-membros da CEDEAO para enfrentar os desafios climáticos e consolidar o desenvolvimento sustentável da nossa sub-região.
        """
    },
    {
        "id": 3,
        "categoria": "Relações Internacionais",
        "data": "28 de Outubro de 2026",
        "titulo": "Audiência com a Delegação da União Europeia e Parceiros de Desenvolvimento",
        "resumo": "Avaliação dos programas de cooperação nas áreas da educação, saúde materno-infantil e energias renováveis.",
        "conteudo": """
        **BISSAU, 28 de Outubro de 2026** — Sua Excelência o Primeiro-Ministro recebeu hoje, no Palácio do Governo, uma delegação de alto nível composta por representantes da União Europeia e agências das Nações Unidas.

        Durante o encontro, foram passados em revista os projetos em curso no domínio da eletrificação rural através de centrais solares e o reforço do equipamento hospitalar nas regiões do interior.

        Ambas as partes reafirmaram o compromisso com o alinhamento das ajudas externas às prioridades definidas no Programa do Governo.
        """
    },
    {
        "id": 4,
        "categoria": "Decretos e Leis",
        "data": "19 de Outubro de 2026",
        "titulo": "Decreto-Lei n.º 14/2026: Regime de Incentivos ao Investimento Agrícola e Agroindustrial",
        "resumo": "Estabelece isenções fiscais e aduaneiras para unidades de transformação local de castanha de caju, arroz e frutas tropicais.",
        "conteudo": """
        **PRESIDÊNCIA DO CONSELHO DE MINISTROS**
        **Decreto-Lei n.º 14/2026**

        Considerando a necessidade imperiosa de fomentar a transformação industrial interna dos produtos agrícolas nacionais e reduzir a dependência das exportações em bruto, o Governo decreta:

        - **Artigo 1.º (Objeto):** O presente diploma estabelece o regime especial de incentivos fiscais para projetos agroindustriais instalados em território nacional.
        - **Artigo 2.º (Isenções Aduaneiras):** Ficam isentos de direitos de importação os equipamentos industriais e maquinarias destinados exclusivamente à transformação de produtos agrícolas locais.
        - **Artigo 3.º (Entrada em vigor):** O presente Decreto-Lei entra imediatamente em vigor na data da sua publicação no Boletim Oficial.
        """
    }
]

# ==========================================
# FUNÇÃO MODAL PARA LEITURA COMPLETA
# ==========================================
@st.dialog("Documento Oficial — Gabinete do Primeiro-Ministro", width="large")
def abrir_documento(item):
    st.caption(f"{item['categoria'].upper()}  |  {item['data']}")
    st.subheader(item["titulo"])
    st.divider()
    st.markdown(item["conteudo"])
    st.divider()
    st.caption("Gabinete de Comunicação e Informação • Palácio do Governo, Bissau, República da Guiné-Bissau")

# ==========================================
# BARRA SUPERIOR OFICIAL (.GOV.GW) & IDIOMA
# ==========================================
st.markdown("""
<div class="gov-masthead">
    🇬🇼 <strong>Portal Oficial do Governo da República da Guiné-Bissau</strong>  |  Domínio institucional verificado (<code>.gov.gw</code>)
</div>
<div class="tricolor-bar"></div>
""", unsafe_allow_html=True)

col_logo, col_lang = st.columns([4, 1])

with col_logo:
    st.markdown("""
    <div class="pmo-header" style="border-bottom: none; padding-bottom: 0;">
        <div class="pmo-emblem">★</div>
        <div>
            <p class="pmo-title-sub">República da Guiné-Bissau</p>
            <h1 class="pmo-title-main">Gabinete do Primeiro-Ministro</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_lang:
    st.write("")
    idioma = st.selectbox(
        "Idioma",
        ["Português (Oficial)", "Krioulo", "Français"],
        label_visibility="collapsed"
    )

st.divider()

# ==========================================
# NAVEGAÇÃO PRINCIPAL (ABAS ESTILO PMO.GOV.SG)
# ==========================================
tab_inicio, tab_pm, tab_governo, tab_imprensa, tab_contacto = st.tabs([
    "Início",
    "O Primeiro-Ministro",
    "Conselho de Ministros",
    "Sala de Imprensa",
    "Contactos e Serviços"
])

# ==========================================
# ABA 1: INÍCIO
# ==========================================
with tab_inicio:
    # Hero Banner
    st.markdown("""
    <div class="hero-card">
        <span class="hero-tag">Prioridade Nacional</span>
        <div class="hero-heading">Unidade, Estabilidade e Desenvolvimento Sustentável para a Guiné-Bissau</div>
        <div class="hero-desc">
            Acompanhe as decisões do Conselho de Ministros, os discursos oficiais, as políticas públicas e as iniciativas de modernização do Estado promovidas pela Chefia do Governo.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Barra de Pesquisa Rápida
    busca = st.text_input(
        "Pesquisar no portal",
        placeholder="🔍 Pesquisar discursos, decretos, comunicados ou palavras-chave (ex: CEDEAO, Decreto, Infraestruturas)..."
    )

    st.subheader("Destaques da Sala de Imprensa")

    resultados = [
        c for c in COMUNICADOS
        if busca.lower() in c["titulo"].lower() or busca.lower() in c["resumo"].lower() or busca.lower() in c["categoria"].lower()
    ]

    if not resultados:
        st.info("Nenhum comunicado encontrado para o termo pesquisado.")
    else:
        cols = st.columns(2)
        for idx, item in enumerate(resultados):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="news-card">
                    <div class="news-meta">{item['categoria']} • {item['data']}</div>
                    <div class="news-title">{item['titulo']}</div>
                    <div class="news-excerpt">{item['resumo']}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Ler comunicado completo →", key=f"btn_home_{item['id']}"):
                    abrir_documento(item)

# ==========================================
# ABA 2: O PRIMEIRO-MINISTRO
# ==========================================
with tab_pm:
    st.subheader("Chefia do Governo da República da Guiné-Bissau")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.info("🏛️ **Palácio do Governo**\n\nPraça dos Heróis Nacionais\n\nBissau, Guiné-Bissau")
        st.markdown("""
        **Atribuições Constitucionais:**
        - Dirigir a política geral do Governo;
        - Coordenar e orientar a ação de todos os Ministros;
        - Representar o Governo perante a Assembleia Nacional Popular e instâncias internacionais.
        """)
    with c2:
        st.markdown("""
        ### Missão e Visão de Governação
        Nos termos da Constituição da República da Guiné-Bissau, o Primeiro-Ministro é o Chefe do Governo, competindo-lhe dirigir e coordenar a ação governativa e assegurar o funcionamento harmonioso das instituições da administração pública.

        **Eixos Estratégicos do Executivo:**
        1. **Boa Governação e Reforma da Administração Pública:** Digitalização dos serviços ao cidadão e rigor na gestão das finanças públicas.
        2. **Diversificação Económica:** Valorização da produção agrícola, pescas e incentivo à transformação industrial local.
        3. **Capital Humano:** Investimento contínuo na escola pública, no ensino técnico-profissional e no acesso universal aos cuidados de saúde.
        4. **Diplomacia e Cooperação:** Fortalecimento dos laços históricos no seio da CPLP, CEDEAO, União Africana e Nações Unidas.
        """)

# ==========================================
# ABA 3: CONSELHO DE MINISTROS
# ==========================================
with tab_governo:
    st.subheader("Estrutura do Executivo e Ministérios")
    st.write("Composição orgânica dos departamentos governamentais coordenados pelo Primeiro-Ministro:")

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

# ==========================================
# ABA 4: SALA DE IMPRENSA
# ==========================================
with tab_imprensa:
    st.subheader("Arquivo Oficial de Comunicados, Discursos e Legislação")
    filtro_cat = st.radio(
        "Filtrar por categoria:",
        ["Todas", "Comunicados de Imprensa", "Discursos", "Relações Internacionais", "Decretos e Leis"],
        horizontal=True
    )

    filtrados = COMUNICADOS if filtro_cat == "Todas" else [c for c in COMUNICADOS if c["categoria"] == filtro_cat]

    for item in filtrados:
        with st.container(border=True):
            col_txt, col_act = st.columns([4, 1])
            with col_txt:
                st.caption(f"**{item['categoria'].upper()}** | {item['data']}")
                st.markdown(f"#### {item['titulo']}")
                st.write(item["resumo"])
            with col_act:
                st.write("")
                st.write("")
                if st.button("Abrir", key=f"btn_news_{item['id']}", use_container_width=True):
                    abrir_documento(item)

# ==========================================
# ABA 5: CONTACTOS E SERVIÇOS
# ==========================================
with tab_contacto:
    st.subheader("Atendimento Institucional e Imprensa")
    col_info, col_form = st.columns(2)

    with col_info:
        st.markdown("""
        **Sede do Governo**
        Palácio do Governo, Avenida Combatentes da Liberdade da Pátria
        Caixa Postal 37, Bissau — República da Guiné-Bissau

        **Horário de Expediente**
        Segunda a Sexta-feira: 08h00 – 16h00 (GMT)

        **Canais Oficiais**
        - Gabinete de Imprensa: `imprensa@pmo.gov.gw`
        - Protocolo de Estado: `protocolo@pmo.gov.gw`
        """)

    with col_form:
        with st.form("form_contacto"):
            st.write("**Enviar Mensagem ou Pedido de Informação**")
            nome_c = st.text_input("Nome completo ou Entidade")
            email_c = st.text_input("Endereço de e-mail")
            assunto_c = st.selectbox("Assunto", ["Informação Geral", "Acreditação de Imprensa", "Pedido de Audiência", "Outro"])
            msg_c = st.text_area("Mensagem")
            enviado = st.form_submit_button("Submeter Mensagem")
            if enviado:
                if nome_c and email_c and msg_c:
                    st.success("Mensagem registada com sucesso. O Gabinete de Atendimento responderá brevemente.")
                else:
                    st.warning("Por favor, preencha os campos obrigatórios.")

# ==========================================
# RODAPÉ INSTITUCIONAL
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
    <hr style="border-color: #374151; margin: 16px 0;">
    <p style="margin: 0; font-size: 12px;">© 2026 Governo da República da Guiné-Bissau. Todos os direitos reservados.</p>
</div>
""", unsafe_allow_html=True)
