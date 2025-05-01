function loadRequest(requestNumber) {
  // This function loads a request based on the selected request number
  console.log(`Loading Request ${requestNumber}`);

  // You can customize the behavior, for now it will fill the form with mock data for illustration
  if (requestNumber === 1) {
    document.getElementById('http-method').value = 'GET';
    document.getElementById('api-url').value = 'https://api.example.com/data';
    // You can also load the params and body here as needed
  } else if (requestNumber === 2) {
    document.getElementById('http-method').value = 'POST';
    document.getElementById('api-url').value = 'https://api.example.com/submit';
    // Add different mock params or body for Request 2
  }
}

function showTab(tabName) {
  const tabs = document.querySelectorAll(".tab");
  const contents = document.querySelectorAll(".tab-content");
  tabs.forEach(t => t.classList.remove("active"));
  contents.forEach(c => c.style.display = "none");

  document.querySelector(`.tab[onclick="showTab('${tabName}')"]`).classList.add("active");
  document.getElementById(tabName).style.display = "block";
}

function addNewParam() {
  const table = document.querySelector(".param-table");
  const newRow = document.createElement("tr");
  newRow.innerHTML = `
    <td><input type="text" placeholder="Param name" /></td>
    <td><input type="text" placeholder="Param value" /></td>
  `;
  table.appendChild(newRow);
}

function addNewHeader() {
  const headersTable = document.getElementById('headers-table');
  const newRow = document.createElement('tr');
  newRow.innerHTML = `
    <td><input type="text" placeholder="Header name" /></td>
    <td><input type="text" placeholder="Header value" /></td>
  `;
  headersTable.appendChild(newRow);
}

function showResult() {
  const method = document.getElementById("http-method").value;
  const url = document.getElementById("api-url").value;

  // Collect parameters
  const paramRows = document.querySelectorAll(".param-table tr");
  const params = Array.from(paramRows).map(row => {
    const paramName = row.querySelector("input:nth-child(1)").value;
    const paramValue = row.querySelector("input:nth-child(2)").value;
    return `${paramName}=${paramValue}`;
  }).join("&");

  const body = document.querySelector("#body textarea").value;

  const result = `Method: ${method}\nURL: ${url}\nParams: ${params}\nBody:\n${body}`;
  document.getElementById("result-pane").textContent = result;
}
