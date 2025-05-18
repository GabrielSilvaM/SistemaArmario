const filtros = ['filtro-capacidade', 'filtro-local', 'filtro-disponibilidade'];

filtros.forEach(id => {
    document.getElementById(id).addEventListener('change', filtrar);
});

function filtrar() {
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