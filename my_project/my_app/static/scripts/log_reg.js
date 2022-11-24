const container = document.querySelector(".container"),
    pwShowHide = document.querySelectorAll(".showHidePw"),
    pwFields = document.querySelectorAll(".password"),
    signUp = document.querySelector(".signup-link"),
    login = document.querySelector(".login-link");

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

// js code to appear signup and login form
signUp.addEventListener("click", () => {
    container.classList.add("active");
});
login.addEventListener("click", () => {
    container.classList.remove("active");
});

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
    if (txt.value.length == 3) {
        txt.value += ") "
    }
    if (txt.value.length == 10) {
        txt.value += "-"
    }
}

// confirmar senha
let input1 = document.getElementById("id_confirma_senha");
input1.setAttribute("onkeyup", "confereSenha()");

let input2 = document.getElementById("id_senha");
input2.setAttribute("onkeyup", "confereSenha()");


function confereSenha() {
    let senha1 = document.getElementById("id_senha");
    let senha2 = document.getElementById("id_confirma_senha");
    let btn = document.getElementById("btn");

    let result = document.getElementById("result");

    if (senha1.value != senha2.value || senha2.value != senha1.value) {
        result.innerText = "As senhas não conferem"
        btn.disabled = true
    } else {
        result.innerText = ""
        btn.disabled = false
    }

    if (senha2.value == "") {
        result.innerText = ""
    }

    if (senha1.value == "" || senha2.value == "") {
        btn.disabled = true
    }

    if (!texto.test(usuario.value) || "") {
        result.innerText = "Usuario deve conter letras"
        btn.disabled = true
    }
};