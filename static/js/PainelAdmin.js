let opcoesAdm = document.getElementById('opcoesAdm').querySelectorAll('a')

function alternarPainel(e){
    e.preventDefault()
    
    const paineis = document.querySelectorAll('.painel')
    for(let i = 0; i < paineis.length; i++){
        paineis[i].classList.remove('ativo');
    }
    for(let i = 0; i<opcoesAdm.length; i++){
        opcoesAdm[i].classList.remove('selecionado');
    }
    const painelAtual = document.getElementById(e.target.dataset.painel)
    painelAtual.classList.add('ativo')
    e.target.classList.add('selecionado')
   
}
for(let i = 0; i<opcoesAdm.length; i++){
    opcoesAdm[i].addEventListener('click', function(e){
        alternarPainel(e)
    });
}
