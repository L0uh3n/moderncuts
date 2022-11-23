const container = document.querySelector(".container"),
      pwShowHide = document.querySelectorAll(".showHidePw"),
      pwFields = document.querySelectorAll(".password"),
      signUp = document.querySelector(".signup-link"),
      login = document.querySelector(".login-link");

    //   js code to show/hide password and change icon
    pwShowHide.forEach(eyeIcon =>{
        eyeIcon.addEventListener("click", ()=>{
            pwFields.forEach(pwField =>{
                if(pwField.type ==="password"){
                    pwField.type = "text";

                    pwShowHide.forEach(icon =>{
                        icon.classList.replace("uil-eye-slash", "uil-eye");
                    })
                }else{
                    pwField.type = "password";

                    pwShowHide.forEach(icon =>{
                        icon.classList.replace("uil-eye", "uil-eye-slash");
                    })
                }
            }) 
        })
    })

    // js code to appear signup and login form
    signUp.addEventListener("click", ( )=>{
        container.classList.add("active");
    });
    login.addEventListener("click", ( )=>{
        container.classList.remove("active");
    });

    // regex phone number
    function regex_telefone(evento){
        const padrao = /[0-9]/
        var tecla = evento.key
        if(!padrao.test(tecla)){
            return evento.preventDefault()
        }
    }
    
    function regex_telefone(evento){
        const padrao = /[0-9]/
        var tecla = evento.key
        if(!padrao.test(tecla)){
            return evento.preventDefault()
        }
        let txt = document.getElementById('id_num_telefone')
        if(txt.value.length==''){
            txt.value += "("
        }
        if(txt.value.length==3){
            txt.value += ") "
        }
        if(txt.value.length==10){
            txt.value += "-"
        }
    }