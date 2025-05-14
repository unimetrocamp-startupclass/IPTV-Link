Documentação do Sistema 

<ATENÇÃO> 

 

<BAIXE ESTE DOCUMENTO PARA SUA MÁQUINA. INSIRA ESTE ARQUIVO NO GITHUB (DEIXE COMO RAW). COMPARTILHE O LINK COM O ORIENTADOR. profkesede64@gmail.com> 

 

<APAGUE TODAS AS INSTRUÇÕES EM VERMELHO DA SUA CÓPIA. AS INSTRUÇÕES PODERÃO SER CONSULTADAS A PARTIR DESTE ORIGINAL.> 

 

<PARA PREENCHIMENTO DA SUA CÓPIA, SIGA AS DATAS NO ARQUIVO “CALENDÁRIO DE PROJETOS.2025.1”> 

 

 

SUMÁRIO 

 

​​Dados do Cliente	2 

​Equipe de Desenvolvimento	3 

​1. Introdução	4 

​2. Objetivo	5 

​3. Escopo	6 

​4. Backlogs do Produto	7 

​5. Cronograma	8 

​6. Materiais e Métodos	9 

​7. Resultados	10 

​8. Conclusão	11 

​9. Homologação do MVP junto ao cliente	12 

​10. Divulgação	13 

​11. Carta de Apresentação	15 

​12. Carta de Autorização	16 

​13. Relato individual do processo	18​ 

 

 

 

 

 

 

 

Dados do Cliente 

Título do Projeto:  <Título do projeto: no título deve constar, resumidamente, qual problema o software está resolvendo. Ex.: Pneumático: um trocador automático de pneus>. Este título deve ser idêntico ao da planilha “Equipes Projetos” 

Cliente: <razão social/nome do cliente> 

CNPJ/CPF: <CNPJ/CPF do cliente> 

Contato: <nome do contato> 

Email do contato: <email do contato> 

 

 

Equipe de Desenvolvimento  

<Elencar, na tabela abaixo, os dados dos integrantes e do professor-orientador.> 

Nome completo 

Curso 

Disciplina 

Gabriel de Moura Botelho Campos 

Análise e Desenvolvimento de Sistema  

Programação Orientada a Objeto em Java 

Matheus Oliveira da Silva 

Análise e Desenvolvimento de Sistema 

Programação Orientada a Objeto em Java 

Pedro Adolfo custódio Maia 

Análise e Desenvolvimento de Sistema 

Programação Orientada a Objeto em Java 

Lucas Rodrigues Bueno 

Análise e Desenvolvimento de Sistema 

Programação Orientada a Objeto em Java 

<integrante 5> 

<nome do curso> 

<nome da disciplina> 

 

Professor Orientador 

Kesede Rodrigues Júlio. 

 

Introdução 

 

 

A comunicação eficiente entre empresas e seus clientes é um fator essencial para o sucesso de qualquer negócio, especialmente no setor de serviços, como a IPTV (Internet Protocol Television). No contexto atual, a automação de processos de comunicação tem se mostrado uma estratégia crucial para otimizar o atendimento, reduzir custos e melhorar a experiência do usuário. Este trabalho propõe uma solução inovadora que integra o banco de dados de um provedor de serviços IPTV com o WhatsApp, visando automatizar a comunicação entre clientes e fornecedores, oferecendo uma experiência mais ágil, eficiente e personalizada. 

A crescente demanda por soluções que conectem plataformas digitais a canais de comunicação populares, como o WhatsApp, torna-se uma necessidade estratégica para empresas que desejam melhorar o relacionamento com seus clientes, automatizar atendimentos e agilizar processos. A integração de sistemas, por sua vez, é um desafio que exige um planejamento técnico apurado e uma análise profunda dos processos de negócios envolvidos. 

 

 

 

Objetivo 

 

Problema: 
O cliente enfrenta dificuldades em automatizar a comunicação com seus clientes via WhatsApp. O atendimento é feito manualmente, resultando em atrasos, erros e um processo ineficiente. As informações, como status de pagamento e agendamentos, são inseridas manualmente, o que aumenta os custos e prejudica a experiência do cliente. 

Solução Proposta: 
Implementar um sistema computadorizado que integre o banco de dados da empresa com a WhatsApp Business API. A automação permitirá o envio de mensagens personalizadas, como lembretes de pagamento e atualizações de serviço, diretamente pelo WhatsApp, com base nas informações do cliente. Isso reduzirá o tempo de resposta, melhorará a personalização do atendimento e diminuirá a carga de trabalho manual, resultando em maior eficiência e satisfação do cliente. 

 

 

Escopo 

 

Escopo do Sistema 

Requisitos Principais: 

Integração com WhatsApp Business API: Conectar o banco de dados da empresa ao WhatsApp para enviar mensagens automáticas personalizadas. 

Automação de Mensagens: Enviar automaticamente mensagens como lembretes de pagamento e atualizações de serviço. 

Personalização das Mensagens: Adaptar as mensagens conforme o histórico e dados de cada cliente. 

Limites de Implementação: 

Interações Complexas: Atendimento personalizado e suporte técnico avançado não serão automatizados. 

Integração com Outras Plataformas: O sistema será focado apenas no WhatsApp, sem integração com outras plataformas de comunicação. 

Escalabilidade Inicial: O sistema não será projetado para suportar grandes volumes de dados ou interações simultâneas inicialmente. 

O que não será Implementado: 

Funcionalidades de e-commerce e processamento de pagamentos via WhatsApp. 

Suporte a canais de comunicação além do WhatsApp. 

 

Backlogs do Produto 

 

[14:27, 04/05/2025] +55 19 99875-9779: Objetivo do Sistema: Criar um sistema de gestão e distribuição de IPTV para clientes que desejam acessar canais pagos, filmes, séries e conteúdos sob demanda (VOD) através da internet, utilizando decodificadores, apps ou players compatíveis com listas IPTV 

[14:27, 04/05/2025] +55 19 99875-9779: Funcionalidades Principais do Sistema para Clientes: 

[14:27, 04/05/2025] +55 19 99875-9779: Funcionalidade	Descrição 

📺 Acesso a canais ao vivo	Transmissão de canais nacionais e internacionais, incluindo esportes, filmes, notícias etc. 

🎥 Conteúdo VOD (Vídeo sob demanda)	Catálogo com filmes, séries e programas para assistir a qualquer momento. 

⏯️ Reprodutor embutido ou integração com apps	suporte a players externos (ex: IPTV Smarters, VLC, Kodi). 

📱 Compatibilidade com dispositivos	Acesso via Smart TV, Android, iOS, computadores e TV Box. 

🧾 Gestão de assinaturas	Login/senha, tempo restante de assinatura, upgrade de plano. 

📶 Detecção de status do servidor	Verificação se o servidor está online, offline ou com lentidão. 

🆘 Suporte técnico ao cliente	Canal de contato direto com suporte (chat, WhatsApp, ticket). Funcionalidade	Descrição 

📺 Acesso a canais ao vivo	Transmissão de canais nacionais e internacionais, incluindo esportes, filmes, notícias etc. 

🎥 Conteúdo VOD (Vídeo sob demanda)	Catálogo com filmes, séries e programas para assistir a qualquer momento. 

⏯️ Reprodutor embutido ou integração com apps	suporte a players externos (ex: IPTV Smarters, VLC, Kodi). 

📱 Compatibilidade com dispositivos	Acesso via Smart TV, Android, iOS, computadores e TV Box. 

🧾 Gestão de assinaturas	Login/senha, tempo restante de assinatura, upgrade de plano. 

📶 Detecção de status do servidor	Verificação se o servidor está online, offline ou com lentidão. 

🆘 Suporte técnico ao cliente	Canal de contato direto com suporte (chat, WhatsApp, ticket). 

[14:29, 04/05/2025] +55 19 99875-9779: Requisitos Funcionais: Código	Requisito	Descrição 

RF01	Cadastro de usuários	Usuário pode criar conta com login e senha. 

RF02	Autenticação e autorização	Login seguro para impedir acesso indevido. 

RF03	Geração de listas IPTV (m3u/m3u8)	O sistema gera arquivos personalizados por usuário. 

RF04	Painel de administração	Interface para gerenciar usuários, planos, status de servidores. 

RF05	Integração com servidor de streaming	Conexão com servidores (Xtream Codes, Flussonic etc.). 

RF06	Monitoramento de dispositivos ativos	Controle de número de acessos simultâneos por cliente. 

RF07	Pagamento e renovação	Gerenciamento de planos pagos com vencimento e recarga. 

RF08	Envio automático de e-mails ou WhatsApp	Para lembretes de renovação ou mensagens do sistema. 

RF09	Gerenciamento de conteúdo VOD	Upload, organização e classificação dos conteúdos. 

RF10	Estatísticas de uso 

[14:30, 04/05/2025] +55 19 99875-9779: Requisitos Não Funcionais: 

[14:30, 04/05/2025] +55 19 99875-9779: Código	Requisito	Descrição 

RNF01	Segurança	Uso de SSL, criptografia de login e bloqueio por IP. 

RNF02	Escalabilidade	Sistema preparado para aumento de usuários e canais. 

RNF03	Disponibilidade	Sistema com uptime próximo de 99%. 

RNF04	Performance	Streaming sem travamentos em conexões acima de 10Mbps. 

RNF05	Interface amigável	Design limpo e intuitivo para usuário final e administrador. 

RNF06	Suporte multiplataforma	Compatibilidade com vários sistemas operacionais e navegadores. 

[14:30, 04/05/2025] +55 19 99875-9779: Serviços e Recursos para Clientes: 

[14:31, 04/05/2025] +55 19 99875-9779: Serviço	Descrição 

📦 Planos mensais/anual	Diferentes opções de preços, com variação de canais e dispositivos. 

🔄 Atualizações automáticas	Inclusão e remoção de canais sem afetar o usuário final. 

📲 App personalizado	Aplicativo próprio com login direto via QR Code. 

🧑‍💻 Atendimento técnico	Suporte via chat, e-mail ou WhatsApp para problemas técnicos. 

💬 Grupo VIP de suporte	Acesso a grupo no Telegram ou WhatsApp com alertas e novidades. 

 

Cronograma 

 

O cronograma do projeto IPTVlink foi estruturado com periodicidade quinzenal, organizando as tarefas em etapas que abrangem desde a fase inicial de planejamento até a entrega final do sistema. A divisão em ciclos de duas semanas permite um acompanhamento mais preciso do progresso e facilita ajustes durante o desenvolvimento. 

Abaixo, segue o planejamento geral das atividades: 

Etapa 

Atividade Principal 

Início 

Término 

Duração 

Fase 1 – Planejamento 

Levantamento de Requisitos 

06/05/2025 

19/05/2025 

2 semanas 

Fase 2 – Design 

Criação das Telas e Prototipagem 

20/05/2025 

02/06/2025 

2 semanas 

Fase 3 – Desenvolvimento 1 

Cadastro, Login e Catálogo de Canais 

03/06/2025 

16/06/2025 

2 semanas 

Fase 4 – Desenvolvimento 2 

Player de Vídeo e Guia de Programação 

17/06/2025 

30/06/2025 

2 semanas 

Fase 5 – Integrações e Pagamento 

Assinaturas e Sistema Administrativo 

01/07/2025 

14/07/2025 

2 semanas 

Fase 6 – Testes 

Testes Funcionais e de Compatibilidade 

15/07/2025 

28/07/2025 

2 semanas 

Fase 7 – Entrega Final 

Ajustes finais e apresentação do projeto 

29/07/2025 

11/08/2025 

2 semanas 

 

 

 

Materiais e Métodos 

 

 

a. Modelagem do Sistema 

Para representar a estrutura e o comportamento do sistema IPTVlink, foram utilizados dois tipos de diagramas UML: 

Diagrama de Casos de Uso: 
Esse diagrama mostra a interação dos usuários (atores) com o sistema, destacando funcionalidades como login, visualização de canais, assinatura de planos e acesso ao painel administrativo. Ele facilita a visualização dos principais processos que o sistema oferece. 

Modelo Entidade-Relacionamento (MER): 
Representa a estrutura dos dados no banco, incluindo entidades como Usuário, Canal, Plano, Assinatura, e seus relacionamentos. Esse modelo foi essencial para a criação e normalização do banco de dados. 

Ferramentas utilizadas para os diagramas: 
Os diagramas foram criados com a ferramenta online Draw.io, que permite desenhar modelos UML de forma intuitiva e colaborativa. 

Forma 

b. Tecnologias Utilizadas 

A seguir, listamos as tecnologias e ferramentas utilizadas no desenvolvimento do IPTVlink: 

Frontend: 

HTML/CSS/Javascript: Linguagens básicas para estrutura, estilo e interatividade. 

React.js: Biblioteca Javascript usada para construir a interface de forma dinâmica e modular. 

Backend: 

Node.js com Express: Plataforma e framework utilizados para criar as APIs e lógica de negócio. 

JWT (JSON Web Token): Biblioteca para autenticação segura de usuários. 

Banco de Dados: 

MySQL: Sistema gerenciador de banco de dados relacional utilizado para armazenar informações dos usuários, canais e planos. 

APIs: 

API de Pagamento (ex: Stripe ou MercadoPago): Utilizada para gerenciamento das assinaturas pagas dos usuários. 

Ferramentas auxiliares: 

Draw.io: Criação de diagramas. 

Postman: Testes de requisições de API. 

GitHub: Controle de versão do código-fonte. 

Forma 

c. Arquitetura do Sistema 

A arquitetura do sistema IPTVlink foi desenvolvida seguindo o modelo cliente-servidor, com o seguinte fluxo de informações: 

O usuário acessa a aplicação pelo navegador ou dispositivo. 

O frontend (React) envia requisições HTTP ao servidor backend (Node.js). 

O backend processa as requisições, acessa o banco de dados MySQL e retorna os dados ao cliente. 

Para funcionalidades como pagamento, o backend se comunica com APIs externas. 

O conteúdo (como canais de vídeo) é carregado no player por meio de endpoints específicos. 

Você pode inserir aqui um diagrama ilustrando esse fluxo, com caixas e setas mostrando a interação entre: Usuário ⇄ Frontend ⇄ Backend ⇄ Banco de Dados ⇄ API de Pagamento. 

 

 

Resultados 

 

a. Protótipo 

A seguir, são apresentadas as principais telas desenvolvidas para o sistema IPTVlink, juntamente com suas descrições e funcionalidades: 

Tela de Login 

Ação do usuário: Inserir e-mail e senha. 

Reação do sistema: Validação das credenciais e redirecionamento para o painel do usuário. 

Tela Inicial / Catálogo de Canais 

Ação do usuário: Visualizar os canais disponíveis, filtrar por categoria e selecionar um canal. 

Reação do sistema: Carregamento do vídeo ao vivo do canal selecionado. 

Tela de Assinatura 

Ação do usuário: Escolher um plano e realizar o pagamento. 

Reação do sistema: Redirecionamento para o gateway de pagamento e liberação de acesso conforme o plano. 

Painel Administrativo (Admin) 

Ação do administrador: Gerenciar canais, usuários e planos. 

Reação do sistema: Atualização das informações no banco de dados em tempo real. 

(Aqui você pode inserir imagens pequenas e bem organizadas das telas, com legendas explicando o que cada uma faz.) 

Forma 

b. Códigos das Principais Funcionalidades 

Abaixo estão alguns trechos relevantes do código com comentários explicativos: 

1. Autenticação de Usuário (Node.js + JWT) 

Javascript 

Copiar Editar 

// Rota de login 

app.post('/login', async (req, res) => { 

    const { email, senha } = req.body; 

    const usuario = await Usuario.findOne({ email }); 

 

    if (!usuario || !bcrypt.compareSync(senha, usuario.senha)) { 

        return res.status(401).json({ mensagem: "Credenciais inválidas" }); 

    } 

 

    // Geração do token 

    const token = jwt.sign({ id: usuario._id }, 'chave_secreta', { expiresIn: '1h' }); 

    res.json({ token }); 

}); 

Esse código faz a verificação de login e retorna um token JWT ao usuário. 

Forma 

2. Exibição de Canais no Frontend (React.js) 

jsx 

CopiarEditar 

useEffect(() => { 

  fetch('/api/canais') 

    .then(res => res.json()) 

    .then(data => setCanais(data)); 

}, []); 

 

return ( 

  <div className="grade-canais"> 

    {canais.map(canal => ( 

      <div key={canal.id} className="canal"> 

        <h3>{canal.nome}</h3> 

        <video src={canal.streamUrl} controls /> 

      </div> 

    ))} 

  </div> 

); 

Este trecho carrega os canais da API e os exibe com players de vídeo. 

 

Conclusão 

 

a. Impacto do Sistema 

O sistema IPTVlink proporcionou uma solução prática e moderna para a transmissão e gerenciamento de canais via internet. Sua implementação impactou positivamente o processo do cliente ao permitir o acesso organizado e seguro a conteúdos ao vivo, com uma interface intuitiva, suporte a múltiplos dispositivos e gerenciamento simplificado de usuários e assinaturas. Além disso, a automação de tarefas como autenticação, controle de planos e exibição de programação reduziu significativamente o tempo gasto com atividades manuais. 

Forma 

b. Melhorias Futuras 

Apesar dos resultados satisfatórios, o sistema pode ser aprimorado com novas funcionalidades. Uma melhoria futura relevante seria a implementação de um sistema de recomendações personalizadas, que sugira canais ou conteúdos com base nos hábitos de visualização do usuário. Além disso, seria interessante adicionar suporte a notificações push e acesso offline a conteúdos gravados, ampliando ainda mais a experiência do usuário. 

 

 

Homologação do MVP junto ao cliente 

 

Após as entregas parciais, realizadas de acordo com os requisitos do sistema e cronograma, o MVP foi apresentado em uma reunião, realizada entre o time de desenvolvedores e o cliente. 

 

<Dica: inserir uma foto da homologação em cada linha do quadro abaixo. Serão 4 fotos (tiradas no momento da homologação) e, na linha debaixo, uma legenda para cada uma delas. A homologação, preferencialmente, deve ser presencial. Se não for viável, pode ser feita por videoconferência com prints da tela.> 

 

<foto 1: foto do time e cliente com o primeiro slide de fundo> 

<foto 2: foto de um integrante apresentando o MVP.> 

Da esquerda para direita: <legenda 1: descreva quem está na foto> 

<legenda 2: coloque o nome de quem está apresentando> 

<foto 3: foto dos participantes assistindo a homologação> 

<foto 4: foto do plano geral do local> 

Participantes da homologação assistindo a apresentação 

Participantes da homologação 

 

Segue abaixo a lista de presentes na homologação do MVP. 

 

Lista de presentes na Homologação 

<Cole aqui a foto da lista de presentes na homologação.> 

 

Ao final da apresentação, o sistema  foi homologado pelo cliente. 

 

Divulgação 

 

Linkedin do Projeto 

<A página do Linkedin do projeto deve ter o logo do LTD, o titulo do projeto, um breve resumo, o nome dos integrantes e o nome do professor-orientador. Insira também o link do repositório do projeto no GitHub. Neste perfil, deve ser postado a cada Sprint, os artefatos produzidos (diagramas, videos explicativos de códigos, artigo sobre determinado tema vinculado ao desenvolvimento do projeto). Promova engajamento e networking conectando-se a profissionais da área, compartilhamentos, comentários etc.  

Insira o linnk deste perfil com o seu perfil pessoal do Linkedin. 

 

<print da tela de perfil do Linkedin> 

<link da pág do Linkedin> 

 

Seminário de Projetos de Software 

 

Vídeo da apresentação: <Grave sua apresentação, poste no Linkedin do projeto e insira aqui o link público (acesso sem login) do vídeo da apresentação> 

 

<Na tabela abaixo, inserir uma foto da apresentação em cada linha. Serão 4 fotos (tiradas no momento da apresentação). Para cada foto, descreva uma legenda na linha de baixo.> 

 

<foto 1: foto do time com o primeiro slide de fundo> 

<foto 2: foto de um integrante apresentando o sistema.> 

Da esquerda para direita: <legenda 1: descreva quem está na foto> 

<legenda 2: coloque o nome de quem está apresentando> 

<foto 3: foto plano geral da apresentação de frente para o fundo da sala> 

<foto 4:  foto plano geral da apresentação do fundo para a frente da sala> 

Participantes do evento assistindo a apresentação 

Participantes do evento assistindo a apresentação 

 

Segue abaixo a lista de presentes na apresentação. 

 

Lista de presentes na Apresentação 

<Faça uma lista de presença numa folha A4, contendo no alto da folha “Seminários de Projetos de Software”. A lista deve conter ra, nome e assinatura dos presentes. Cole aqui a foto desta lista.> 

 

FENETEC: Feira de Negócios em Tecnologia 

 

Apresentação do projeto: <Um vídeo deve ser produzido mostrando o time apresentando seu projeto para algum visitante. Importante que neste video tenha uma tomada do banner e dos integrantes. Insira aqui o link público deste vídeo.> 

 

<Na tabela abaixo, inserir uma foto da apresentação em cada linha. Serão 4 fotos (tiradas do evento). Para cada foto, descreva uma legenda na linha de baixo.> 

 

<foto 1: foto do time ao lado do poster> 

<foto 2: foto de um integrante apresentando o sistema.> 

Da esquerda para direita: <legenda 1: descreva quem está na foto> 

<legenda 2: coloque o nome de quem está apresentando> 

<foto 3: foto do público assistindo sua apresentação> 

<foto 4:  foto plano geral da FENETEC> 

Participantes do evento assistindo a apresentação 

Estandes da FENETEC 

 

Segue abaixo a lista de presentes na FENETEC. 

 

Lista de presentes na Apresentação 

<cole aqui a lista de presença dos visitantes da FENETEC com nome e email do visitante . Os próprios times farão um form contendo no cabeçalho: Lista de Visitantes FENETEC. Compartilhe a planilha gerada pelo form com todos os times.> 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Carta de Apresentação 

LTD – LABORATÓRIO DE TRANSFORMAÇÃO DIGITAL CARTA DE APRESENTAÇÃO  

Vimos por meio desta apresentar o grupo de acadêmicos do Centro Universitário Unimetrocamp, localizado na Av. Sales de Oliveira, 1661 – Campinas – SP, a fim de convidá-lo a participar de uma atividade extensionista associada ao componente curricular ARA0075 – Programação Orientada a Objeto, sob responsabilidade do orientador Prof. Kesede Rodrigues Júlio. Em consonância com o Plano Nacional de Educação vigente, o Centro Universitário Unimetrocamp desenvolve projetos de Desenvolvimento de Software que, norteados pela metodologia da Engenharia de Software, têm por princípios: o diagnóstico de problemas e demandas reais, a participação ativa dos envolvidos, a construção coletiva de conhecimentos, o planejamento e desenvolvimento de soluções, e a avaliação dos resultados alcançados. Nesse contexto, a disciplina mencionada tem como principal escopo o desenvolvimento de habilidades técnicas e comportamentais relacionadas à construção de softwares para clientes reais, contemplando etapas como levantamento de requisitos, modelagem, codificação, testes e homologação do MVP (Produto Mínimo Viável). Nosso projeto, intitulado IPtv Link, tem como objetivo o desenvolvimento de uma plataforma voltada à automação da comunicação com clientes, integrando dados provenientes de bancos de dados ou sistemas dos usuários com o aplicativo WhatsApp. A solução proposta visa facilitar e automatizar o processo de contato com o cliente, tornando a comunicação mais ágil e prática. De forma específica, o sistema realizará a extração e sincronização de dados dos bancos de dados dos clientes, armazenando essas informações em nosso sistema. A partir daí, será possível visualizar e manipular dados como datas de pagamento, vencimentos e outras informações relevantes. O sistema também permitirá o envio de mensagens personalizadas e em massa via WhatsApp diretamente da plataforma, bastando selecionar os nomes e números desejados — otimizando o contato com múltiplos clientes de forma eficiente e centralizada. Sendo assim, solicitamos o apoio desta organização LTD – Laboratório de Transformação Digital para a realização das seguintes atividades: – Diagnósticos, por meio de reuniões agendadas; – Análises técnicas realizadas pela equipe de desenvolvimento; – Levantamento de requisitos (reuniões online ou presenciais); – Desenvolvimento do projeto utilizando a Metodologia Ágil Scrum; – Mentorías com o professor da disciplina; – Pesquisas em documentações, repositórios e plataformas de IA, bem como o uso de quaisquer recursos que otimizem a construção e entrega do MVP. Aproveitamos a oportunidade para solicitar que, em caso de aceite, a participação seja formalizada mediante assinatura da Carta de Autorização, especificando as atividades e informações que os alunos poderão acessar. Por fim, registramos o convite a todos os interessados para o fórum semestral de acompanhamento e avaliação das atividades realizadas, previsto para o final deste semestre, com convite a ser enviado previamente. Desde já, colocamo-nos à disposição para quaisquer esclarecimentos. Atenciosamente, Local, 25 de Abril de 2025. 

Texto

O conteúdo gerado por IA pode estar incorreto., Imagem 
 Campinas, ____ de _________ de 202___. 

 

____________________________________ 

Assinatura Direção Acadêmica da IES 

Texto, Carta

O conteúdo gerado por IA pode estar incorreto., Imagem  

____________________________________ 

Assinatura Docente 

 

 

Carta de Autorização 

LABORATÓRIO DE TRANSFORMAÇÃO DIGITAL CARTA DE AUTORIZAÇÃO  

Eu, Kesede Rodrigues Júlio, Coordenador do Laboratório de Transformação Digital, do Centro Universitário Unimetrocamp, situado no endereço Rua Dr. Sales de Oliveira, 1661 – Campinas, autorizo a realização das seguintes atividades acadêmicas do componente extensionista ARA0075 – Programação Orientada à Objeto, do Centro Universitário Unimetrocamp, sob orientação do Prof. Kesede Rodrigues Julio: Atividades: – Reuniões de levantamento de requisitos – Reuniões de homologação do projeto Conforme combinado em contato prévio, as atividades acima descritas são autorizadas para os seguintes alunos: Nome dos alunos Curso Matrícula Lucas Rodrigues Bueno ADS 20230881178 9 Pedro Adolfo Custódio Maia ADS 20240301975 2 Gabriel de Moura Botelho Campos ADS 20230842853 5 Matheus Oliveira da Silva ADS 20240241047 4 Declaro que fui informado por meio da Carta de Apresentação sobre as características e objetivos das atividades que serão realizadas na instituição a qual represento e afirmo estar ciente de tratar-se de uma atividade realizada com intuito exclusivo de ensino de alunos de graduação, sem a finalidade de exercício profissional. Desta forma, autorizo, em caráter de confidencialidade: – O acesso a informações e dados que forem necessários à execução da atividade; – O registro de imagem por meio de fotografias. Campinas, 25 de abril de 2025. Kesede Rodrigues Julio LTD – Unimetrocamp  

Atividades: 

  

  

  

  

Conforme combinado em contato prévio, as atividades acima descritas são autorizadas para os seguintes alunos: 

  

Nome dos/das alunos/as 

Curso 

Matrícula 

Gabriel de Moura Botelho Campos 

 ADS 

 202308428535 

 Lucas Rodrigues Bueno 

 ADS 

 202308811789 

 Pedro Adolfo Custódio Maia 

 ADS 

 202403019752 

 Matheus Oliveira da Silva 

 ADS 

 20240241047 4 

 

 

 

  

Declaro que fui informado por meio da Carta de Apresentação sobre as características e objetivos das atividades que serão realizadas na organização/instituição/empresa a qual represento e afirmo estar ciente de tratar-se de uma atividade realizada com intuito exclusivo de ensino de alunos de graduação, sem a finalidade de exercício profissional. 

  

Desta forma, autorizo, em caráter de confidencialidade: 

  

 o acesso a informações e dados que forem necessários à execução da atividade; 

 o registro de imagem por meio de fotografias; 

 outro: (especificar) 

  

  

Campinas, ___ de ___________de 202_. 

  

___________________________________________________________________ 

(Assinatura, nome completo do responsável, email de contato e com carimbo da empresa) 

 

 

Relato individual do processo 

 

<nome do aluno> 

<um breve relato pessoal sobre o trabalho extensionista desenvolvido> 

 

<nome do aluno> 

<um breve relato pessoal sobre o trabalho extensionista desenvolvido> 

 

<nome do aluno> 

<um breve relato pessoal sobre o trabalho extensionista desenvolvido> 

 

<nome do aluno> 

<um breve relato pessoal sobre o trabalho extensionista desenvolvido> 

 

<nome do aluno> 

<um breve relato pessoal sobre o trabalho extensionista desenvolvido> 

 

 

  

 

 
