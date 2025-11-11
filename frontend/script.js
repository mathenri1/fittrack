const apiBase = "http://127.0.0.1:5000/api";

document.addEventListener("DOMContentLoaded", () => {
  // Treinos (já existia)
  const treinoForm = document.getElementById("formTreino");
  if (treinoForm) {
    treinoForm.addEventListener("submit", async e => {
      e.preventDefault();
      const obs = document.getElementById("observacoes").value;
      const esforco = document.getElementById("esforco").value;
      await fetch(`${apiBase}/treinos/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ usuario_id: 1, observacoes: obs, percepcao_esforco: esforco })
      });
      treinoForm.reset();
      carregarTreinos();
    });
    carregarTreinos();
  }

  // Refeições (NOVIDADE)
  const refeicaoForm = document.getElementById("formRefeicao");
  if (refeicaoForm) {
    refeicaoForm.addEventListener("submit", async e => {
      e.preventDefault();
      const descricao = document.getElementById("descricao").value;
      const proteina = parseFloat(document.getElementById("proteina").value || 0);
      const carbo = parseFloat(document.getElementById("carbo").value || 0);
      const gordura = parseFloat(document.getElementById("gordura").value || 0);

      await fetch(`${apiBase}/refeicoes/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          usuario_id: 1,
          descricao,
          proteina_g: proteina,
          carbo_g: carbo,
          gordura_g: gordura
        })
      });
      refeicaoForm.reset();
      carregarRefeicoes();
    });
    carregarRefeicoes();
  }
});

// funções
async function carregarTreinos() {
  const ul = document.getElementById("listaTreinos");
  if (!ul) return;
  const res = await fetch(`${apiBase}/treinos/`);
  const data = await res.json();
  ul.innerHTML = "";
  data.forEach(t => {
    const li = document.createElement("li");

    const info = document.createElement("div");
    const dataStr = t.data_hora ? t.data_hora.split("T")[0] : "";
    info.innerHTML = `<strong>${dataStr}</strong> — ${t.observacoes || "(sem observações)"} 
      <span class="item-meta">Esforço ${t.percepcao_esforco ?? "-"}</span>`;

    const actions = document.createElement("div");
    actions.className = "actions";
    const btnDel = document.createElement("button");
    btnDel.className = "danger";
    btnDel.textContent = "Excluir";
    btnDel.onclick = async () => {
      if (!confirm("Apagar este treino?")) return;
      await fetch(`${apiBase}/treinos/${t.id}`, { method: "DELETE" });
      carregarTreinos();
    };

    actions.appendChild(btnDel);
    li.appendChild(info);
    li.appendChild(actions);
    ul.appendChild(li);
  });
}

async function carregarRefeicoes() {
  const ul = document.getElementById("listaRefeicoes");
  if (!ul) return;
  const res = await fetch(`${apiBase}/refeicoes/`);
  const data = await res.json();
  ul.innerHTML = "";
  data.forEach(r => {
    const li = document.createElement("li");

    const info = document.createElement("div");
    const dataStr = r.data_hora ? r.data_hora.split("T")[0] : "";
    const p = (r.proteina_g ?? 0);
    const c = (r.carbo_g ?? 0);
    const g = (r.gordura_g ?? 0);
    info.innerHTML = `<strong>${dataStr}</strong> — ${r.descricao}
      <span class="item-meta">P:${p}g C:${c}g G:${g}g</span>`;

    const actions = document.createElement("div");
    actions.className = "actions";
    const btnDel = document.createElement("button");
    btnDel.className = "danger";
    btnDel.textContent = "Excluir";
    btnDel.onclick = async () => {
      if (!confirm("Apagar esta refeição?")) return;
      await fetch(`${apiBase}/refeicoes/${r.id}`, { method: "DELETE" });
      carregarRefeicoes();
    };

    actions.appendChild(btnDel);
    li.appendChild(info);
    li.appendChild(actions);
    ul.appendChild(li);
  });
}

