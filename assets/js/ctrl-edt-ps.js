/* 
   * Carregar dados do Participante
 */

let id_user;

async function carregar_dados() 
{
   const url = new URL(window.location.href);
   const id = url.searchParams.get('id');

   try 
   {
      let resp = await fetch(`http://127.0.0.1:5000/sltcpus?id=${id}`);
      let dados = await resp.text();

      const [idUser, nomeUs, telefoneUs, campeonato, campId] = dados.split(',').map(item => item.trim());

      document.querySelector('#nome').value = nomeUs;
      document.querySelector('#telefone').value = telefoneUs;

      let resp_opt = await fetch(`http://127.0.0.1:5000/sltoptsus?id=${campId}`);
      let dados_opt = await resp_opt.text();

      const select = document.querySelector('#camp-slc');
      select.innerHTML = `<option value="${campId}" selected>${campeonato}</option>` + dados_opt;
      id_user = idUser;
   } 
   catch (error) 
   {
      console.error("Erro ao carregar os dados:", error);
      alert("Ocorreu um erro ao carregar os dados.");
   }
}

carregar_dados();

/* 
   * Editar dados do Participante
 */

let form_sl = document.querySelector('#form-upd-us');

async function editar_participante(event) 
{
   event.preventDefault();

   let nome = form_sl.nome.value;
   let telefone = form_sl.telefone.value;
   let campeonato = form_sl.camp.value;

   let url = `http://127.0.0.1:5000/updps?nome=${nome}&telefone=${telefone}&campeonato=${campeonato}&id=${id_user}`;

   try 
   {
      let response = await fetch(url);
      let data = await response.text();
      alert(data);

   } catch (error) 
   {
      console.error("Erro ao alterar participante:", error);
   }
}

form_sl.addEventListener('submit', editar_participante);