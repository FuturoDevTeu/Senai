const fundo = document.querySelector('body')
const ney = document.querySelector('#ney')
const messi = document.querySelector('#messi')
const cr7 = document.querySelector('#cr7')

ney.addEventListener('click', neymar)
messi.addEventListener('click', et)
cr7.addEventListener('click', robo)

function neymar(){
    fundo.className = ney
}

function et(){
    fundo.className = messi
}

function robo(){
    fundo.className = cr7
}