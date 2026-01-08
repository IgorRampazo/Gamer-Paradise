/* Carregar Tabelas  */
async function carregar_participantes() 
{
   let resp = await fetch("http://127.0.0.1:5000/sltps");
   let linhas = await resp.text();
   let tbody = document.querySelector('.data-ps');
   tbody.innerHTML = linhas;
}

carregar_participantes();