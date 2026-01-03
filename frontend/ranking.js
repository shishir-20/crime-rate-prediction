const BACKEND_URL = "http://127.0.0.1:5000/api";

async function loadMeta() {
  const res = await fetch(`${BACKEND_URL}/meta`);
  const data = await res.json();

  fill("crime", data.crime_types);
  fill("year", data.years);
}

function fill(id, items) {
  const select = document.getElementById(id);
  items.forEach(v => {
    const opt = document.createElement("option");
    opt.value = v;
    opt.textContent = v;
    select.appendChild(opt);
  });
}

async function loadRanking() {
  const res = await fetch(
    `${BACKEND_URL}/ranking?crime_type=${crime.value}&year=${year.value}`
  );
  const data = await res.json();

  let html = "<table width='100%'>";
  html += "<tr><th>Rank</th><th>State</th><th>Count</th></tr>";

  data.forEach((r, i) => {
    html += `<tr>
      <td>${i + 1}</td>
      <td>${r.State}</td>
      <td>${r.Count}</td>
    </tr>`;
  });

  html += "</table>";
  table.innerHTML = html;
}

loadMeta();
