
function register(){
    documento = document.getElementById("document").value;
    nombre = document.getElementById("name").value;
    lastname = document.getElementById("lastname").value;
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;
    eel.registerPython(documento,nombre,lastname,username,password);
  
}

document.addEventListener('DOMContentLoaded', () => {
    eel.showPython()(callback); 
}) 

function callback(resultado){
    console.log(resultado)
    let mostrar = document.getElementById('mostrar');
    resultado.forEach(element => {
        console.log(element)
      
            mostrar.innerHTML += `
             <td>${element[0]}</td>
             <td>${element[1]}</td>
             <td>${element[2]}</td>
             <td>${element[3]}</td>
            `       
    });
}