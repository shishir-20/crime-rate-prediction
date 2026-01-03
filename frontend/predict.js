const BACKEND_URL = "http://127.0.0.1:5000/api";

async function loadMeta() {
  const res = await fetch(`${BACKEND_URL}/meta`);
  const data = await res.json();

  fill("city", data.cities);
  fill("year", data.years);
  fill("crime", data.crime_types);
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

async function predictCrime() {
  const payload = {
    city: city.value,
    year: year.value,
    crime_type: crime.value
  };

  const res = await fetch(`${BACKEND_URL}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await res.json();

  const box = document.getElementById("result");
  box.style.display = "block";
  box.innerHTML = `
    <b>Predicted Crime Count:</b> ${data.prediction}<br>
    <b>Risk Level:</b> ${data.risk_level}
  `;
}

loadMeta();
