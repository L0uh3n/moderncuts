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