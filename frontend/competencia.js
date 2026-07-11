const dadosCompetencias = {
  1: {
    tag: "C1",
    titulo: "Domínio da norma culta",
    intro: "Avalia se você escreve de acordo com a modalidade formal da língua portuguesa — a base de qualquer redação bem avaliada.",
    avaliado: "Ortografia, acentuação, concordância verbal e nominal, regência, pontuação e uso adequado do registro formal exigido pelo gênero dissertativo-argumentativo.",
    erros: [
      "Erros de concordância (ex: 'os direitos humanos é importante')",
      "Uso de gírias ou linguagem informal",
      "Pontuação que compromete a leitura do argumento",
      "Repetição de erros ortográficos básicos"
    ],
    atualizacao2025: "Os critérios de correção continuam rigorosos com a norma padrão, sem tolerância maior para desvios recorrentes — um texto com muitos erros pontuais tende a ficar limitado a notas intermediárias, mesmo com bom conteúdo.",
    icone: `<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>`
  },
  2: {
    tag: "C2",
    titulo: "Compreensão da proposta",
    intro: "Avalia se você entendeu o tema de verdade e se usa repertório sociocultural para sustentar seu argumento — não só pra decorar o texto.",
    avaliado: "Aplicação de conceitos de diferentes áreas (história, filosofia, atualidades, ciência) de forma articulada e pertinente ao tema proposto, dentro da estrutura dissertativo-argumentativa.",
    erros: [
      "Repertório genérico, decorado, sem conexão real com o argumento (o chamado 'repertório de bolso')",
      "Fugir parcialmente do tema proposto",
      "Citar dados ou autores sem explicar a relação com a tese",
      "Parágrafos que apenas descrevem o problema, sem aprofundar"
    ],
    atualizacao2025: "Repertório genérico ou mal contextualizado agora penaliza a nota tanto na Competência 2 quanto na Competência 3 simultaneamente — a mesma fragilidade rebaixa as duas notas, não é mais tratada como um problema isolado.",
    icone: `<circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.8"/><path d="M21 21l-4.35-4.35" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>`
  },
  3: {
    tag: "C3",
    titulo: "Organização de argumentos",
    intro: "Avalia sua capacidade de organizar informações, fatos e opiniões em uma progressão lógica e autoral, defendendo um ponto de vista.",
    avaliado: "Seleção, relação e organização de argumentos e fatos com autoria — ou seja, indo além de apenas reunir informações soltas, construindo um raciocínio próprio e consistente.",
    erros: [
      "Parágrafos desconectados entre si, sem progressão de ideias",
      "Argumentação superficial, sem aprofundamento",
      "Repetir o mesmo argumento com palavras diferentes",
      "Repertório usado apenas como enfeite, sem articulação com a tese"
    ],
    atualizacao2025: "Assim como na Competência 2, o uso de repertório genérico ('de bolso') sem articulação real com o argumento penaliza esta competência ao mesmo tempo — trate como uma única fragilidade, não dois problemas separados.",
    icone: `<path d="M4 6h16M4 12h10M4 18h16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>`
  },
  4: {
    tag: "C4",
    titulo: "Mecanismos linguísticos (coesão)",
    intro: "Avalia como você conecta frases, parágrafos e ideias — o que dá fluidez e clareza ao texto.",
    avaliado: "Uso de conectivos, pronomes, sinônimos e outros recursos coesivos que articulam as partes do texto, garantindo uma leitura fluida e sem repetições desnecessárias.",
    erros: [
      "Repetir sempre os mesmos conectivos ('além disso', 'portanto')",
      "Parágrafos que parecem blocos isolados, sem transição",
      "Uso mecânico de conectivos, sem real função argumentativa",
      "Ausência de conectivos entre introdução, desenvolvimento e conclusão"
    ],
    atualizacao2025: "Desde 2025, essa competência deixou de ser avaliada por contagem de conectivos e passou a ser qualitativa: seu repertório coesivo é classificado como pontual, regular, constante ou expressivo. Repetir conectivos, mesmo em quantidade suficiente, mantém a nota no máximo em 'regular'.",
    icone: `<path d="M9 6L4 12l5 6M15 6l5 6-5 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>`
  },
  5: {
    tag: "C5",
    titulo: "Proposta de intervenção",
    intro: "Avalia se você propõe uma solução viável e completa para o problema discutido, respeitando os direitos humanos.",
    avaliado: "Presença de 5 elementos: agente (quem faz), ação (o que faz), meio/modo (como faz), finalidade (para quê) e detalhamento (explicação mais aprofundada de um desses elementos).",
    erros: [
      "Proposta vaga, sem dizer quem vai executar a ação",
      "Ausência do elemento de ação (o que exatamente deve ser feito)",
      "Falta de detalhamento — só listar os elementos sem aprofundar nenhum",
      "Propostas que ferem direitos humanos (ex: pena de morte, eugenia)"
    ],
    atualizacao2025: "Segundo apuração do G1 baseada em documentos internos e relatos de corretores, a ausência do elemento 'ação' passou a ter desconto de 120 pontos nesta competência em 2025 (antes eram 40 pontos) — o INEP nega oficialmente qualquer mudança nos critérios, mas a orientação foi relatada por corretores envolvidos na correção.",
    icone: `<path d="M12 2v6m0 8v6M4.2 4.2l4.2 4.2m7.2 7.2l4.2 4.2M2 12h6m8 0h6M4.2 19.8l4.2-4.2m7.2-7.2l4.2-4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>`
  }
};

const params = new URLSearchParams(window.location.search);
const numeroComp = params.get('c') || '1';
const dados = dadosCompetencias[numeroComp] || dadosCompetencias['1'];

document.title = `${dados.tag} — ${dados.titulo} | Redify`;
document.getElementById('comp-tag').textContent = dados.tag;
document.getElementById('comp-title').textContent = dados.titulo;
document.getElementById('comp-intro').textContent = dados.intro;
document.getElementById('comp-avaliado').textContent = dados.avaliado;
document.getElementById('comp-2025').textContent = dados.atualizacao2025;
document.getElementById('comp-icon').innerHTML = `<svg width="28" height="28" viewBox="0 0 24 24" fill="none">${dados.icone}</svg>`;

const listaErros = document.getElementById('comp-erros');
dados.erros.forEach(erro => {
  const li = document.createElement('li');
  li.textContent = erro;
  listaErros.appendChild(li);
});