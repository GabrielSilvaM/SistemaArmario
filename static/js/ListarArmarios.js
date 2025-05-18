//Remove a classe selecionada de qualquer outra linha clicada antes e configura a atual
function selecionarLinha(linha) {
    document.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    linha.classList.add('selecionada');
    //Puxa o valor da primeira coluna da linha selecionada
    const idArmario = linha.querySelectorAll('td')[0].textContent;
    //Define o campo oculto para o ID correto no form
    document.getElementById('armarioId').value = idArmario;
    //Faz aparecer o form de reserva quando tem um armário selecionado
    document.getElementById('reservaForm').style.display = ''
}
function limparSelecao(){
    document.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    document.getElementById('armarioId').value = '';
    //Oculta o form quando limpar a seleção
    document.getElementById('reservaForm').style.display = 'none'
}
function confirmar(){
    const idArmario = document.getElementById('armarioId').value
    const inicio = document.getElementById('inicio').value
    const fim = document.getElementById('fim').value

    let confirmacao = confirm(`Confirmar reserva do armário ${idArmario} no período de ${inicio} até ${fim}?`)
    return confirmacao 
}