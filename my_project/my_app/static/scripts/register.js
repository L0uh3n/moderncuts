// regex nome
function regex_nome(evento) {
    const padrao = /[A-Z, a-z, '', á, é, í, ó, ú, ã, õ, â, ê, ô]/
    var tecla = evento.key
    if (!padrao.test(tecla)) {
        return evento.preventDefault()
    }
}

// regex phone number
function regex_telefone(evento) {
    const padrao = /[0-9]/
    var tecla = evento.key
    if (!padrao.test(tecla)) {
        return evento.preventDefault()
    }
}

function regex_telefone(evento) {
    const padrao = /[0-9]/
    var tecla = evento.key
    if (!padrao.test(tecla)) {
        return evento.preventDefault()
    }
    let txt = document.getElementById('id_num_telefone')
    if (txt.value.length == '') {
        txt.value += "("
    }

    if (txt.value.length == 1 && !txt.value.includes("(")) {
        txt.value = "(" + txt.value.substring(0)
    }

    if (txt.value.length == 3) {
        txt.value += ") "
    }

    if (txt.value.length == 10) {
        txt.value += "-"
    }
}

// confirmar senha
let input1 = document.getElementById("id_senha");
input1.setAttribute("onkeyup", "confereSenha(event)");

let input2 = document.getElementById("id_confirma_senha");
input2.setAttribute("onkeyup", "confereSenha(event)");

function confereSenha() {
    var senha1 = document.getElementById("id_senha");
    var senha2 = document.getElementById("id_confirma_senha");
    var btn = document.getElementById("cad-button");

    if (senha1.value != senha2.value || senha2.value != senha1.value) {
        senha2.setCustomValidity("Senhas diferentes!")
        btn.disabled = true
    } else {
        senha2.setCustomValidity("")
        btn.disabled = false
    }

    if (senha2.value == "") {
        senha2.setCustomValidity("Prencha esse campo!")
    }

    if (senha1.value == "" || senha2.value == "") {
        btn.disabled = true
    }
};