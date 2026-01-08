/* 
   * Cadastrar Jogador
 */

// Formularios
let form_sl = document.querySelector('#form-sl');


async function gravar_participante(event) 
{
   event.preventDefault();

   let nome = form_sl.nome.value;
   let telefone = form_sl.telefone.value;
   let campeonato = form_sl.camp.value;

   let url = `http://127.0.0.1:5000/cadps?nome=${nome}&telefone=${telefone}&campeonato=${campeonato}`;

   try 
   {
      let response = await fetch(url);
      let data = await response.text();
      alert(data);

   } catch (error) 
   {
      console.error("Erro ao cadastrar participante:", error);
   }
}

form_sl.addEventListener('submit', gravar_participante);