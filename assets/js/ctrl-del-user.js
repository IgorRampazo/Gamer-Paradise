function remover_user(campId) 
{
   if (confirm('Confirma a exclusão?')) 
   {
      try 
      {
         fetch(`http://127.0.0.1:5000/delps?id=${campId}`)
         alert('Registro excluído com sucesso.');
         window.location.reload();
      } 
      catch (error) 
      {
         alert('Erro ao excluir o registro.');
         
      }
   }
}