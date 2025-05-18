const filtrosR = ['filtro-idarmario', 'filtro-idusuario', 'filtro-capacidadeR', 'filtro-local'];

filtrosR.forEach(id => {
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