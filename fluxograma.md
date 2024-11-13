## Fluxograma do Programa de Treinos

1. **Tela Inicial**
   - Pergunta: "Você já possui uma conta?"
     - **Sim** ➔ Redirecionar para a **Página da Conta**
     - **Não** ➔ Redirecionar para a **Tela de Criação de Conta**

2. **Tela de Criação de Conta**
   - Solicitar:
     - Email
     - Nome
     - Senha
   - Armazenar dados e redirecionar para a **Página da Conta**

3. **Página da Conta**
   - Opções:
     - **Treinos e Competições** ➔ Redirecionar para a **Tela de Treinos e Competições**
     - **Metas e Desafios** ➔ Redirecionar para a **Tela de Metas e Desafios**
     - **Sugerir Treino** ➔ Executar a função de sugestão de treino
     - **Gerenciar Conta** ➔ Redirecionar para a **Tela de Gerenciamento de Conta**

4. **Tela de Treinos e Competições**
   - Opções:
     - **Adicionar Treino ou Competição**
       - Solicitar informações do treino via input
       - Armazenar informações em uma lista
       - Salvar dados no arquivo CSV do usuário
     - **Visualizar Treino ou Competição**
       - Ler dados de treino do arquivo CSV do usuário
       - Exibir os treinos na tela
     - **Atualizar Treino ou Competição**
       - Modificar dados específicos pelo índice no arquivo CSV
     - **Excluir Treino ou Competição**
       - Excluir treino ou competição do arquivo CSV pelo índice

5. **Tela de Metas e Desafios**
   - Opções:
     - **Alterar Metas Pessoais**
       - Solicitar novas metas
       - Armazenar dados em um arquivo CSV na pasta do usuário
     - **Visualizar Metas Atingidas**
       - Analisar o arquivo CSV de treinos para:
         - Treinos do último mês que atingiram a meta de velocidade por treino
         - Verificar se a meta mensal de distância total foi atingida

6. **Função Sugerir Treino**
   - Analisar histórico de treinos no arquivo CSV do usuário
   - Gerar treino sugerido com metas de distância e tempo com base no histórico

7. **Tela de Gerenciamento de Conta**
   - Opções:
     - **Atualizar Senha**
       - Alterar senha armazenada na pasta do usuário
     - **Atualizar Nome**
       - Alterar nome armazenado na pasta do usuário
     - **Deletar Conta**
       - Excluir pasta do usuário e todos os dados associados
