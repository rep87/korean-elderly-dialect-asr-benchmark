const percent = value => `${(value * 100).toFixed(2)}%`;
const memory = row => row.vram_mb ? `${Math.round(row.vram_mb).toLocaleString()} MB VRAM` : `${Math.round(row.ram_mb).toLocaleString()} MB RAM`;

async function loadResults() {
  const response = await fetch('../results/model-summary.json');
  if (!response.ok) throw new Error('Could not load result snapshot.');
  return response.json();
}

function setSummary(rows) {
  const best = rows[0];
  const fastGpu = rows.filter(row => row.device === 'CUDA' && row.standard_cer < 0.2).sort((a, b) => a.seconds - b.seconds)[0];
  const cpu = rows.filter(row => row.device === 'CPU').sort((a, b) => a.standard_cer - b.standard_cer)[0];
  document.querySelector('#bestCer').textContent = percent(best.standard_cer);
  document.querySelector('#bestCerName').textContent = `${best.model} · ${best.configuration}`;
  document.querySelector('#fastGpu').textContent = `${fastGpu.seconds.toFixed(2)}초`;
  document.querySelector('#fastGpuName').textContent = `${fastGpu.model} · ${percent(fastGpu.standard_cer)} CER`;
  document.querySelector('#cpuCandidate').textContent = percent(cpu.standard_cer);
  document.querySelector('#cpuCandidateName').textContent = `${cpu.model} · ${memory(cpu)}`;
}

function renderChart(rows) {
  const chart = document.querySelector('#barChart');
  chart.innerHTML = rows.slice(0, 12).map(row => `<div class="bar-row"><span class="bar-label" title="${row.model} · ${row.configuration}">${row.model} · ${row.configuration}</span><div class="bar-track"><div class="bar" style="width:${Math.min(row.standard_cer * 100, 100)}%"></div></div><strong class="bar-value">${percent(row.standard_cer)}</strong></div>`).join('');
}

function renderTable(rows) {
  document.querySelector('#resultRows').innerHTML = rows.map((row, index) => `<tr><td class="num">${index + 1}</td><td class="model">${row.model}<small>${row.configuration}${row.comparison_note ? ` · ${row.comparison_note}` : ''}</small></td><td>${row.device}</td><td class="num">${percent(row.standard_cer)}</td><td class="num">${percent(row.dialect_cer)}</td><td class="num">${row.seconds.toFixed(2)}초</td><td class="num">${memory(row)}</td></tr>`).join('');
}

loadResults().then(data => {
  const rows = data.results.slice().sort((a, b) => a.standard_cer - b.standard_cer);
  setSummary(rows); renderChart(rows); renderTable(rows);
  document.querySelector('#deviceFilter').addEventListener('change', event => renderTable(event.target.value === 'all' ? rows : rows.filter(row => row.device === event.target.value)));
}).catch(error => { document.querySelector('#barChart').textContent = error.message; });
