# Sistema-de-Armario
Processual na disciplina de Fabrica de Software II

Plano Técnico de Desenvolvimento (PTD)
Sistema Simples de Cadastro de Armários
Goiânia, 5 de maio de 2025

Introdução

Contextualização do Projeto

Nos dias atuais, muitas empresas e organizações enfrentam o desafio de gerenciar recursos compartilhados de forma eficiente. Um desses recursos frequentemente utilizado são os armários em ambientes de trabalho, onde funcionários ou colaboradores precisam armazenar seus pertences pessoais temporariamente. A gestão eficiente desses armários é essencial para garantir que todos tenham acesso justo e organizado ao recurso. A gestão de armários envolve monitorar a disponibilidade de cada unidade, permitir a reservação desses espaços e acompanhar a renovação mensal de cada armário ocupado. Apesar da importância desse controle, muitas empresas ainda utilizam métodos manuais ou desorganizados, o que pode gerar confusão e reduzir a eficiência operacional.

Objetivo do Projeto

Este projeto tem como objetivo o desenvolvimento de um sistema simples de gestão de armários para empresas, permitindo o gerenciamento digital de armários, facilitando a reserva, visualização da disponibilidade e renovação do uso mensal. A proposta é criar uma solução acessível e fácil de usar, onde os administradores e usuários poderão visualizar a disponibilidade dos armários em tempo real, realizar reservas e renovações mensais de maneira prática, sem a necessidade de processos manuais complexos.

Escopo do Projeto 
Objetivo Geral
Desenvolver um sistema web para gerenciar armários de uma empresa, permitindo que os funcionários visualizem a disponibilidade, reservem armários e renovem sua utilização mensalmente. O sistema tem como objetivo proporcionar uma solução simples, prática e acessível.

Objetivos Específicos
Criar um sistema onde os usuários possam visualizar os armários disponíveis e em uso, com uma interface simples e intuitiva.
Implementar a funcionalidade de cadastro de armários para registrar os armários disponíveis para reserva.
Permitir que os usuários façam reservas e renovações mensais de armários.
Desenvolver uma funcionalidade de alteração de status para que os administradores possam atualizar a situação de cada armário (se está em uso ou disponível).
Armazenar as informações sobre as reservas e renovações no banco de dados, garantindo o controle e a transparência das operações.
Implementar um sistema simples de login e autenticação para os administradores do sistema, permitindo que apenas usuários autorizados possam gerenciar o sistema.

Requisitos Funcionais

1. Cadastro de Armários
Descrição: O administrador deve ser capaz de cadastrar novos armários no sistema.
Funcionalidade: O administrador preenche um formulário com informações básicas (ex: número do armário, localização, capacidade) e o armário é adicionado ao banco de dados.
Requisito: O sistema deve garantir que cada armário tenha um identificador único.
2. Visualização de Armários
Descrição: O usuário deve ser capaz de visualizar a lista de armários disponíveis e em uso.
Funcionalidade: A interface exibirá os armários cadastrados e o status atual de cada um (disponível, em uso, reservado).
Requisito: O sistema deve apresentar a disponibilidade dos armários em tempo real, atualizando as informações automaticamente quando o status de um armário mudar.
3. Reserva de Armários
Descrição: O usuário deve ser capaz de reservar um armário disponível.
Funcionalidade: O usuário escolhe um armário da lista de armários disponíveis e efetua a reserva para um período determinado.
Requisito: O sistema deve permitir que o armário seja marcado como "reservado" após a reserva ser feita.
4. Renovação de Armários
Descrição: O usuário deve ser capaz de renovar a reserva de um armário para um novo período (mensal).
Funcionalidade: O sistema deve permitir que o usuário clique em "renovar" em sua reserva, automaticamente renovando o período de utilização do armário.
Requisito: O sistema deve verificar se o armário está disponível para renovação antes de realizar o processo.
5. Alteração de Status de Armários
Descrição: O administrador deve ser capaz de alterar o status dos armários (disponível, em uso, reservado).
Funcionalidade: O administrador pode alterar manualmente o status de um armário em caso de erro de reserva, de uso indevido ou para outras necessidades operacionais.
Requisito: O sistema deve atualizar automaticamente a lista de armários assim que o status for alterado.
6. Autenticação de Administradores
Descrição: O sistema deve permitir que os administradores façam login para acessar as funcionalidades administrativas.
Funcionalidade: O administrador deve inserir um nome de usuário e senha para acessar o painel de gerenciamento dos armários.
Requisito: O sistema deve garantir que somente administradores autenticados tenham acesso à funcionalidade de gerenciamento de armários.
7. Armazenamento de Dados de Reservas e Armários
Descrição: O sistema deve armazenar de forma persistente os dados relacionados aos armários, suas reservas e status.
Funcionalidade: As informações sobre o armário (número, status) e as reservas (usuário, data de reserva, data de renovação) devem ser armazenadas no banco de dados.
Requisito: O banco de dados deve ser consultado e atualizado automaticamente sempre que uma reserva ou alteração de status for realizada.
8. Interface Intuitiva e Simples
Descrição: O sistema deve apresentar uma interface simples e intuitiva para os usuários, com um layout claro e fácil de navegar.
Funcionalidade: A interface de reserva deve permitir que os usuários vejam a lista de armários, escolham um disponível, e façam a reserva com o mínimo de cliques.
Requisito: A interface deve ser fácil de usar, tanto em desktop quanto em dispositivos móveis.

Requisitos Não Funcionais

1. Desempenho
Descrição: O sistema deve ser capaz de realizar operações rapidamente, garantindo que os usuários possam interagir com a interface de forma fluida.
Requisito: O tempo de resposta do sistema para exibir a lista de armários, fazer reservas e renovação de armários deve ser inferior a 3 segundos.
2. Escalabilidade
Descrição: O sistema deve ser projetado para suportar o aumento do número de armários e usuários sem comprometer o desempenho.
Requisito: O banco de dados deve ser capaz de armazenar informações de até 500 armários e 1000 usuários simultaneamente sem perda de performance.
3. Segurança
Descrição: O sistema deve garantir a proteção das informações sensíveis, como dados de login e dados de reservas, evitando acessos não autorizados.
Requisito:
O sistema deve utilizar criptografia de senha (por exemplo, hash) para proteger as credenciais de login dos administradores.
O acesso ao painel de administração deve ser restrito a usuários autenticados.
O sistema deve ser protegido contra vulnerabilidades comuns, como injeções SQL e ataques de força bruta.
4. Usabilidade
Descrição: O sistema deve ser fácil de usar, com uma interface intuitiva, acessível para todos os tipos de usuários.
Requisito:
O layout deve ser simples, sem sobrecarregar o usuário com informações excessivas.
O sistema deve permitir que usuários sem experiência técnica consigam fazer reservas e renovação de armários facilmente.
5. Compatibilidade
Descrição: O sistema deve ser compatível com os principais navegadores web e dispositivos móveis, garantindo acessibilidade em diferentes plataformas.
Requisito:
O sistema deve funcionar corretamente em navegadores como Google Chrome, Mozilla Firefox, Safari e Microsoft Edge.
A interface deve ser responsiva, adaptando-se automaticamente ao tamanho da tela em dispositivos móveis e desktops.
6. Manutenibilidade
Descrição: O sistema deve ser fácil de manter, com código claro e bem documentado, para facilitar futuras atualizações e correções.
Requisito:
O código deve ser modular, utilizando boas práticas de programação, como o uso de funções e classes reutilizáveis.
A documentação do código e do sistema deve ser clara e acessível para os desenvolvedores que trabalharem na manutenção ou evolução do sistema.
7. Backup e Recuperação
Descrição: O sistema deve garantir que os dados possam ser recuperados em caso de falha, evitando perdas de informações importantes, como reservas de armários.
Requisito:
O banco de dados deve ser configurado para realizar backups automáticos periódicos, de preferência diários ou semanais, para garantir a recuperação de dados em caso de falhas.
8. Confiabilidade
Descrição: O sistema deve ser confiável, com baixo risco de falhas ou erros durante o uso.
Requisito:
O sistema deve ser capaz de lidar com situações de erro sem interromper a operação, como ao tentar reservar um armário já ocupado.
O sistema deve ser testado para garantir que o gerenciamento dos armários e suas reservas sejam realizados corretamente, sem perda de dados ou falhas críticas.
9. Internacionalização (se necessário no futuro)
Descrição: O sistema deve ser projetado de forma que seja fácil implementar versões em outros idiomas, caso necessário.
Requisito:
O sistema deve ser construído de forma que seja possível adicionar traduções de texto para diferentes idiomas sem alterar a estrutura do código base

Regras de Negócio

5. Principais Regras

Cadastro de Armário: Cada armário deve possuir um número único, uma localização definida e deve estar inicialmente como "disponível" após o cadastro.
Reserva de Armário: Um armário só pode ser reservado se estiver com status "disponível".
Renovação de Reserva: A renovação só pode ocorrer se a reserva estiver ativa e não vencida.
Liberação de Armário: Em casos como demissão do colaborador, o administrador pode liberar manualmente o armário, tornando-o "disponível" novamente.
Acesso Restrito: Apenas administradores autenticados podem cadastrar, alterar ou remover armários.
Registro de Ações: Toda reserva, renovação e liberação de armário deve ser registrada no sistema para controle de histórico.

5.2 Caso de Uso: Reserva de Armário

Nome: Reserva de Armário
Elemento
Descrição
Ator Primário
Usuário do Sistema
Resumo
O usuário seleciona um armário disponível para reservar por um mês.
Pré-condições
O usuário deve estar autenticado (se necessário) e o armário deve estar disponível.
Fluxo Principal
1. Usuário acessa a lista de armários disponíveis.
2. Usuário seleciona um armário.
3. Sistema solicita confirmação.
4. Sistema altera o status do armário para "reservado".
5. Sistema registra a data da reserva e o ID do usuário.
Fluxo Alternativo
Se o armário for reservado por outro usuário antes da confirmação, o sistema informa indisponibilidade e pede para selecionar outro.
Pós-condição
O armário está reservado para o usuário, e o sistema registra a ação.

Tecnologias Utilizadas
Frontend:
Python

Backend:
Python

Banco de Dados:
SQLite: Banco de dados levE.

Hospedagem:
Inicialmente rodando localmente.
    
