// ---------- Contador regressivo ENEM 2026 ----------
const dataEnem = new Date("2026-11-08T13:00:00-03:00");

function atualizarContador() {
  const elDias = document.getElementById('cd-days');
  if (!elDias) return; // essa página não tem o contador, ignora

  const agora = new Date();
  const diff = dataEnem - agora;

  if (diff <= 0) {
    document.getElementById('cd-days').textContent = "00";
    document.getElementById('cd-hours').textContent = "00";
    document.getElementById('cd-min').textContent = "00";
    document.getElementById('cd-sec').textContent = "00";
    return;
  }

  const dias = Math.floor(diff / (1000 * 60 * 60 * 24));
  const horas = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const min = Math.floor((diff / (1000 * 60)) % 60);
  const seg = Math.floor((diff / 1000) % 60);

  document.getElementById('cd-days').textContent = String(dias).padStart(2, '0');
  document.getElementById('cd-hours').textContent = String(horas).padStart(2, '0');
  document.getElementById('cd-min').textContent = String(min).padStart(2, '0');
  document.getElementById('cd-sec').textContent = String(seg).padStart(2, '0');
}

atualizarContador();
setInterval(atualizarContador, 1000);

// ---------- Correção de redação (só existe em app.html) ----------
const API_URL = "http://127.0.0.1:8000/corrigir";

const input = document.getElementById('essay-input');
const charCount = document.getElementById('char-count');
const submitBtn = document.getElementById('submit-btn');
const resultArea = document.getElementById('result-area');

if (input && submitBtn) {
  input.addEventListener('input', () => {
    charCount.textContent = `${input.value.length} caracteres`;
  });

  submitBtn.addEventListener('click', async () => {
    const texto = input.value.trim();

    if (texto.length < 50) {
      resultArea.innerHTML = `<div class="result-empty" style="border-color:#FF5C7C; color:#FF5C7C;">
        Escreva pelo menos 50 caracteres para poder corrigir.
      </div>`;
      return;
    }

    resultArea.innerHTML = `<div class="loading-dots"><span></span><span></span><span></span></div>`;
    submitBtn.disabled = true;
    submitBtn.textContent = "Corrigindo...";

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto })
      });

      if (!response.ok) throw new Error("Erro na correção");

      const data = await response.json();
      renderResult(data);
    } catch (err) {
      console.error(err);
      resultArea.innerHTML = `<div class="result-empty" style="border-color:#FF5C7C; color:#FF5C7C;">
        Não foi possível corrigir agora. Confira se o backend está rodando em localhost:8000.
      </div>`;
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = "Corrigir minha redação";
    }
  });
}

function renderResult(data) {
  const pct = Math.round((data.nota_total / 1000) * 100);

  resultArea.innerHTML = `
    <div class="result-score">
      <div class="score-ring" style="--pct:${pct}">
        <div class="score-ring-inner">${pct}%</div>
      </div>
      <div>
        <div class="result-score-label">Nota estimada</div>
        <div class="result-score-total">${data.nota_total} / 1000</div>
      </div>
    </div>
    <div class="paywall">
      <p>Veja a nota detalhada por competência, pontos fortes e o que melhorar.</p>
      <button class="btn btn-primary" id="unlock-btn">Desbloquear feedback completo — R$ 2,90</button>
    </div>
  `;

  document.getElementById('unlock-btn').addEventListener('click', () => {
    renderFullFeedback(data);
  });
}

function renderFullFeedback(data) {
  const compBars = data.competencias.map(c => `
    <div class="comp-bar-row">
      <div class="comp-bar-top"><span>C${c.numero} — ${c.titulo}</span><span>${c.nota}/200</span></div>
      <div class="comp-bar-track"><div class="comp-bar-fill" style="width:${(c.nota/200)*100}%"></div></div>
    </div>
  `).join('');

  const fortes = data.pontos_fortes.map(p => `<li>${p}</li>`).join('');
  const melhorias = data.pontos_melhoria.map(p => `<li>${p}</li>`).join('');

  const paywall = document.querySelector('.paywall');
  paywall.outerHTML = `
    ${compBars}
    <div class="feedback-lists">
      <div class="feedback-box good">
        <h5>Pontos fortes</h5>
        <ul>${fortes}</ul>
      </div>
      <div class="feedback-box improve">
        <h5>Pontos de melhoria</h5>
        <ul>${melhorias}</ul>
      </div>
    </div>
  `;
}

// ---------- FAQ (só existe em index.html) ----------
document.addEventListener('click', (e) => {
  const btn = e.target.closest('.faq-question');
  if (!btn) return;

  const item = btn.closest('.faq-item');
  const jaAberto = item.classList.contains('open');

  document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));

  if (!jaAberto) item.classList.add('open');
});