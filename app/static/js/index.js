async function personsData() {
    try {
        const response = await fetch("/api/pessoas");

        if (!response.ok) {
            throw new Error("Persons API error: " + response.status);
        }

        const data = await response.json();
        const tableBody = document.querySelector("#persons-data tbody");

        data.message.forEach(person => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td><a href="#" data-bs-toggle="modal" data-bs-target="#staticBackdrop" onclick="showPersonDetails(${person.id_pessoa})">${person.nome}</a></td>                
                <td>${person.data_admissao}</td>
                <td><a class="icon-action" href="/pessoa/${person.id_pessoa}"><img id="img-upload-icon" alt="" src="/static/img/edit_icon.svg"></a></td>
                <td><button type="button" class="icon-action" onclick="deletePerson(${person.id_pessoa})">
                <img alt="" src="/static/img/delete_icon.svg"> </button></td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error("There has been a problem with fetch:", error);
    }
}
function showPersonDetails(id_pessoa) {

    fetch(`/api/pessoa/${id_pessoa}`)
        .then(response => response.json())
        .then(data => {
            const personData = data.person;

            const modalBody = document.querySelector("#staticBackdrop .modal-body");
            modalBody.innerHTML = `
                <p>Nome: ${personData.nome}</p>
                <p>Data de Nascimento: ${personData.data_nascimento}</p>
                <p>RG: ${personData.rg}</p>
                <p>CPF: ${personData.cpf}</p>
                <p>Data de Admissão: ${personData.data_admissao}</p>
                <a class="icon-action" href="/pessoa/${personData.id_pessoa}"><img id="img-upload-icon" alt="" src="/static/img/edit_icon.svg"></a>
                <button type="button" class="icon-action" onclick="deletePerson(${personData.id_pessoa})">
                <img alt="" src="/static/img/delete_icon.svg"> </button>
                
            `;
        });
}

async function updatePerson(id_pessoa) {
    const nome = document.getElementById("nome").value;
    const rg = document.getElementById("rg").value;
    const cpf = document.getElementById("cpf").value;
    const data_admissao = document.getElementById("data_admissao").value;
    const data_nascimento = document.getElementById("data_nascimento").value;

    const data = {
        nome, 
        rg, 
        cpf, 
        data_admissao, 
        data_nascimento,
    };
    try {
        const response = await fetch(`/api/pessoa/${id_pessoa}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const responseData = await response.json();
            alert(responseData.message);
            window.location.reload();
        } else {
            const responseData = await response.json();
            alert(responseData.message);
            throw new Error(`Erro ao enviar os dados: ${responseData.message}`);
        }
    } catch (error) {
        console.error(error);
    }
}

async function deletePerson(id_pessoa) {
    try {
        const response = await fetch(`/api/pessoa/${id_pessoa}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (response.ok) {
            const responseData = await response.json();
            alert(responseData.message);
            window.location.href = "/";
        } else {
            const responseData = await response.json();
            alert(responseData.message);
            throw new Error(`Erro ao excluir os dados: ${responseData.message}`);
        }
    } catch (error) {
        console.error(error);
    }
}

function handleCheckboxChange(checkboxId, value) {
    const checkbox = document.getElementById(checkboxId);
    const dataFieldId = checkboxId.substring(9);
    const dataField = document.getElementById(dataFieldId);

    if (checkbox.checked) {
        dataField.type = 'date';
        dataField.removeAttribute('readonly');
        dataField.value = value;
    } else {
        dataField.type = 'text';
        dataField.setAttribute('readonly', 'true');
        dataField.value = value;
    }
}


async function registerPerson() {
    const nome = document.getElementById("nome").value;
    const rg = document.getElementById("rg").value;
    const cpf = document.getElementById("cpf").value;
    const data_admissao = document.getElementById("data_admissao").value;
    const data_nascimento = document.getElementById("data_nascimento").value;

    const data = {
        nome, 
        rg, 
        cpf, 
        data_admissao, 
        data_nascimento,
    };
    try {
        const response = await fetch("/api/pessoas", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const responseData = await response.json();
            alert(responseData.message);
            window.location.reload();
        } else {
            const responseData = await response.json();
            alert(responseData.message);
            throw new Error(`Erro ao enviar os dados: ${responseData.message}`);
        }
    } catch (error) {
        console.error(error);
    }
}

