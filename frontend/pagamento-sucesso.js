const dadosSalvos = sessionStorage.getItem('redify_correcao');
const resultArea = document.getElementById('result-area');

if (!dadosSalvos) {
  resultArea.innerHTML = `<p style="color:var(--ink-soft)">Nenhuma correção encontrada. Volte e teste novamente.</p>`;
} else {
  const data = JSON.parse(dadosSalvos);

  const compBars = data.competencias.map(c => `
    <div class="comp-bar-row">
      <div class="comp-bar-top"><span>C${c.numero} — ${c.titulo}</span><span>${c.nota}/200</span></div>
      <div class="comp-bar-track"><div class="comp-bar-fill" style="width:${(c.nota/200)*100}%"></div></div>
    </div>
  `).join('');

  const fortes = data.pontos_fortes.map(p => `<li>${p}</li>`).join('');
  const melhorias = data.pontos_melhoria.map(p => `<li>${p}</li>`).join('');

  resultArea.innerHTML = `
    <h1 style="margin-bottom:20px;">✅ Pagamento aprovado!</h1>
    <p style="color:var(--ink-soft); margin-bottom:24px;">Nota total: <strong>${data.nota_total} / 1000</strong></p>
    ${compBars}
    <div class="feedback-lists">
      <div class="feedback-box good"><h5>Pontos fortes</h5><ul>${fortes}</ul></div>
      <div class="feedback-box improve"><h5>Pontos de melhoria</h5><ul>${melhorias}</ul></div>
    </div>
  `;
}