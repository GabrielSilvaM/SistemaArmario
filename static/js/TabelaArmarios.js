const filtrosArmario = ['filtro-capacidade', 'filtro-local', 'filtro-disponibilidade'];

filtrosArmario.forEach(id => {
    document.getElementById(id).addEventListener('change', filtrarArmario);
});

function filtrarArmario() {
    const capacidade = document.getElementById('filtro-capacidade').value;
    const local = document.getElementById('filtro-local').value;
    const disponibilidade = document.getElementById('filtro-disponibilidade').value;

    document.querySelectorAll('#tabela-armarios tbody tr').forEach(row => {
        //Verifica se os valores são nulos e depois compara o valor selecionado com o valor da coluna
        const matchCapacidade = !capacidade || row.dataset.capacidade === capacidade;
        const matchLocal = !local || row.dataset.local === local;
        const matchDisponibilidade = !disponibilidade || row.dataset.disponibilidade === disponibilidade;
        //Exibe apenas os armários que correspondam aos 3 filtros
        row.style.display = (matchCapacidade && matchLocal && matchDisponibilidade) ? '' : 'none';
    });
}
//Remove a classe selecionada de qualquer outra linha clicada antes e configura a atual
function selecionarLinhaArmario(linha) {
    let tabelaArmarios = document.getElementById('tabela-armarios')
    tabelaArmarios.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    document.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    linha.classList.add('selecionada');
    //Puxa o valor da primeira coluna da linha selecionada
    const idArmario = linha.querySelectorAll('td')[0].textContent;
    //Define o campo oculto para o ID correto no form
    document.getElementById('armarioId').value = idArmario;
    //Faz aparecer o form de reserva quando tem um armário selecionado
    document.getElementById('reservaForm').style.display = ''
}
function limparSelecaoArmario(){
    let tabelaArmarios = document.getElementById('tabela-armarios')
    tabelaArmarios.querySelectorAll('tr').forEach(tr => tr.classList.remove('selecionada'));
    document.getElementById('armarioId').value = '';
    //Oculta o form quando limpar a seleção
    document.getElementById('reservaForm').style.display = 'none'
}
function confirmarArmario(){
    const idArmario = document.getElementById('armarioId').value
    const inicio = document.getElementById('inicioArmario').value
    const fim = document.getElementById('fimArmario').value

    let confirmacao = confirm(`Confirmar reserva do armário ${idArmario} no período de ${inicio} até ${fim}?`)
    console.log(confirmacao)
    return confirmacao 
}