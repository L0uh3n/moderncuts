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
input1.setAttribute("onchange", "confereSenha(event)");

let input2 = document.getElementById("id_confirma_senha");
input2.setAttribute("onkeyup", "confereSenha(event)");

function confereSenha() {
    
    const senha1 = document.getElementById("id_senha"), 
    senha2 = document.getElementById("id_confirma_senha");

    if (senha1.value != senha2.value || senha2.value != senha1.value) {
        senha2.setCustomValidity('Senhas não conferem!');
    } else {
        senha2.setCustomValidity('');
    }

    senha2.reportValidity();
};

const pwShowHide = document.querySelectorAll(".showHidePw"),
    pwFields = document.querySelectorAll(".password");

//   js code to show/hide password and change icon
pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        pwFields.forEach(pwField => {
            if (pwField.type === "password") {
                pwField.type = "text";

                pwShowHide.forEach(icon => {
                    icon.classList.replace("uil-eye-slash", "uil-eye");
                })
            } else {
                pwField.type = "password";

                pwShowHide.forEach(icon => {
                    icon.classList.replace("uil-eye", "uil-eye-slash");
                })
            }
        })
    })
})