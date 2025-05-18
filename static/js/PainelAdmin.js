//Remove a classe selecionada de qualquer outra linha clicada antes e configura a atual
function selecionarLinha(linha) {
    document.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    linha.classList.add('selecionada');
    //Puxa o valor da primeira coluna da linha selecionada contendo o ID
    const idReserva = linha.querySelectorAll('td')[0].textContent;
    //Define o campo oculto para o ID correto no form
    document.getElementById('reservaId').value = idReserva;
    //Faz aparecer o form de reserva quando tem uma reserva selecionado
    document.getElementById('editarForm').style.display = ''
    //Preenche os inputs com as datas da reserva
    document.getElementById('inicio').value = linha.querySelectorAll('td')[1].textContent
    document.getElementById('fim').value = linha.querySelectorAll('td')[2].textContent
}
function limparSelecao(){
    document.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    document.getElementById('reservaId').value = '';
    //Oculta o form quando limpar a seleção
    document.getElementById('editarForm').style.display = 'none'
}
function confirmar(){
    //Caixa de confirmação
    const idReserva = document.getElementById('reservaId').value
    let confirmacao = confirm(`Confirmar ação na reserva ${idReserva}?`)
    return confirmacao 
}