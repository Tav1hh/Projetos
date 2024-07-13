
const nome = document.getElementById('nome')
const senha= document.getElementById('senha')
const buttom = document.getElementById('button')
const login = document.getElementById('login')


var log = ['trevoso','virmondes','sylvair','kaua'];
var sen = ['P@cienc1a','pessego','2323','lemes'];


buttom.addEventListener('click', function(){
    var vnome = nome.value 
    var vsenha = senha.value
    let i = 0

    login.innerText = "Erro";

    while (i < 30){
         if(vnome.toLowerCase() == log[i] &&vsenha  == sen[i]){
        login.innerText='Logado'
        location.href ="2c.html"
        }
         i++
        }
        
    }
)
