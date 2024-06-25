function adicionarCampos() {
    var inputsContainer = document.getElementById('inputsContainer');
    var novaLinha = document.createElement('div');
    novaLinha.classList.add('row', 'mb-3');
    novaLinha.innerHTML = `
        <div class="col">
            <input type="text" class="form-control" name="peca" placeholder="Peca">
        </div>
        <div class="col">
            <input type="text" class="form-control" name="cor" placeholder="Cor">
        </div>
        <div class="col">
            <input type="number" class="form-control" name="qtd" placeholder="quantidade">
        </div>
    `;
    inputsContainer.appendChild(novaLinha);
}

document.getElementById('meuFormulario').addEventListener('submit', function(event) {
            event.preventDefault(); // Impede o envio padrão do formulário

            const formData = new FormData(this);

            fetch('/submit-form/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken') // Necessário para Django
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('ITEM SALVO!');
                    // Limpar apenas os campos desejados
                    document.getElementById('peca').value = '';
                    document.getElementById('cor').value = '';
                    document.getElementById('qtd').value = '';
                } else {
                    alert('Ocorreu um erro ao enviar o formulário.');
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Ocorreu um erro ao enviar o formulário.');
            });
        });
 // Função para obter o token CSRF
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Verifica se esse cookie corresponde ao nome desejado
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }