const filtrosReserva = ['filtro-idarmario', 'filtro-idusuario', 'filtro-capacidadeR', 'filtro-localR'];

filtrosReserva.forEach(id => {
    document.getElementById(id).addEventListener('change', filtrarReserva);
});

function filtrarReserva() {
    const idArmario = document.getElementById('filtro-idarmario').value;
    const idUsuario = document.getElementById('filtro-idusuario').value;
    const capacidade = document.getElementById('filtro-capacidadeR').value;
    const local = document.getElementById('filtro-localR').value;

    document.querySelectorAll('#tabela-reservas tbody tr').forEach(row => {
        //Verifica se os valores são nulos e depois compara o valor selecionado com o valor da coluna
        const matchCapacidade = !capacidade || row.dataset.capacidade === capacidade;
        const matchLocal = !local || row.dataset.local === local;
        const matchIdArmario = !idArmario || row.dataset.idarmario === idArmario;
        const matchIdUsuario = !idUsuario || row.dataset.idusuario === idUsuario;
        //Exibe apenas os armários que correspondam aos 3 filtros
        row.style.display = (matchCapacidade && matchLocal && matchIdArmario && matchIdUsuario) ? '' : 'none';
    });
}

//Remove a classe selecionada de qualquer outra linha clicada antes e configura a atual
function selecionarLinhaReserva(linha) {
    let tabelaReservas = document.getElementById('tabela-reservas')
    tabelaReservas.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
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
function limparSelecaoReserva(){
    let tabelaReserva = document.getElementById('tabela-reservas')
    tabelaReserva.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    document.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    document.getElementById('reservaId').value = '';
    //Oculta o form quando limpar a seleção
    document.getElementById('editarForm').style.display = 'none'
}
function confirmarReserva(){
    //Caixa de confirmação
    const idReserva = document.getElementById('reservaId').value
    let confirmacao = confirm(`Confirmar ação na reserva ${idReserva}?`)
    return confirmacao 
}

function atualizarForm(){
    //Busca o elemento de opção que está marcado
    const opcao = document.querySelector('input[name="opcao"]:checked')

    if(opcao.value == 'editar'){
        document.getElementById('inicio').disabled = false
        document.getElementById('fim').disabled = false
    }
    else{
        document.getElementById('inicio').disabled = true
        document.getElementById('fim').disabled = true
    }
}