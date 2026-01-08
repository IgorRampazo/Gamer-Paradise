/* Carregar Opções  */
async function carregar_campeonatos() 
{
   let resp = await fetch("http://127.0.0.1:5000/sltcp");
   let opcoes = await resp.text();
   let select = document.querySelector('#camp-slc');
   select.innerHTML = `<option value="" selected disabled>Selecione</option>` + opcoes;
}

carregar_campeonatos();