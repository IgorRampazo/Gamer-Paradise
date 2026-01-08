/* 
   * Cadastrar Grupo
 */

let form_gp = document.querySelector('#form-gp');

async function gravar_grupo(event) 
{
   event.preventDefault();

   let nome = form_gp.team_name.value;
   let membro_1 = form_gp.mb_1.value;
   let membro_2 = form_gp.mb_2.value;
   let membro_3 = form_gp.mb_3.value;
   let membro_4 = form_gp.mb_4.value;
   let membro_5 = form_gp.mb_5.value;
   let telefone = form_gp.telefone.value;
   let campeonato = form_gp.mb.value;

   let url = `http://127.0.0.1:5000/cadgp?nome=${nome}&mb1=${membro_1}&mb2=${membro_2}&mb3=${membro_3}&mb4=${membro_4}&mb5=${membro_5}&telefone=${telefone}&campeonato=${campeonato}`;

   try 
   {
      let response = await fetch(url);
      let data = await response.text();
      alert(data);

   } catch (error) 
   {
      console.error("Erro ao cadastrar o Grupo:", error);
   }
}

form_gp.addEventListener('submit', gravar_grupo);