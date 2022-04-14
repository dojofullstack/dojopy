console.log("hola Miguel \n vamos a la siguiente linea");


// esto es una variable tipo String
var name =  "miguel";

// variable tipo numeral entero
var age = 20;

// variable tipo numeral floar
var age = 20.9;


//variable tipo booleando true o false
var isAdmin = false;

// varibale tipo objeto array
var MiguelTech = ["python", "javascript", "java", 100];


// variable objeto diccionario

var Productos = {
    "title": "iphone",
    "price": 20.9,
    "url_product": "https://www.web.com",
    "description": "producto nuevo etc",
}

console.log(name);
console.log(age);
console.log(isAdmin);
console.log(MiguelTech);
console.log(Productos);


name = "henry";

// var token = '019291abc';
// console.log(token);

const token = '019291abc';



if (true){
    let email = "hola@dojopy.com";
    var nombre = "pedro";
    console.log(email);
}







function cambiarColor(color, title){

    const botonUno =  document.getElementById('boton_1');
    // botonUno.append(" :D");
    // botonUno.firstChild.data = "nuevo boton";
    botonUno.innerText = title;
    botonUno.style.color = "white";
    botonUno.style.backgroundColor = color;

}



var job_profile = 'full stack'

// condicional simple
if (job_profile.length  >= 3) {
    console.log('es true', job_profile);
}


// condicional compuesta
if (job_profile.length  >= 20) {
    console.log('es true', job_profile);
} else {
    console.log('ota ejecucion')
}


// condicional anidada
if (job_profile.length  >= 20) {
    console.log('es true', job_profile);
} else if (job_profile === 'full') {
    console.log('segunda valicion')
} else if (job_profile === 'full stack')  {
    console.log('segunda valicion')
} else {
    console.log('ota ejecucion')
}





function sleep(seconds){
    var waitUntil = new Date().getTime() + seconds*1000;
    while(new Date().getTime() < waitUntil) 
        true;
}



var estado_del_chat = 'activo';
var contador = 0;

// while (estado_del_chat === 'activo') {
//     cambiarColor('red', 'otro boton');
//     sleep(1);
//     contador += 1;
//     if (contador >= 3){
//         estado_del_chat = 'inactivo';
//     }
// }



// switch (numero) {
//     case 1:
//         console.log('ingresate 1');
//         break;
//     case 2:
//         console.log('ingresate 2');
//         break;
//     default:
//         console.log('ninguna opcion');
//         break;
// }



console.log('------------')
// iteradores en javascript

lista_tareas = ['aprender javascript', 'learn js', 'crear proyecto']
let index = 0;

for (index; index < lista_tareas.length; index += 1) {
     console.log(lista_tareas[index]);
    //  if (lista_tareas[index] === 'learn js'){
    //      console.log('encontramos el elemnto, rompiendo bucle')
    //     //  break
    //  }

    continue;
    console.log('otra operacion');
}




// try {
//     console.log('hola mundo', data_user)

// } catch (error) {
//     console.log('error detectado', error)
//     if (error instanceof ReferenceError){
//         console.log('olvidaste definir tu variable amigo')
//     }
// }



// try {
//     var email = prompt("Cual es tu Email?");
//     // email = Number(email);
//     console.log(email);
// } catch (e) {
//     console.log('tienes el siguiente error: ',e)
// } finally {
//     console.log('finalizo el programa');
// }





const books = ['principito', 'dracula', 'titanic'];

// var book1 = books[0];
// var book2 = books[1];
// var book3 = books[2];

// console.log(book1, book2, book3)


// const [book1, book2, book3] = books;
// console.log(book1, book2, book3)


const books_data = {
    'title': 'principito',
    'autor': 'Jose',
    'price': 10,
    'ASN': '1029192',
    'stock': true
}


// var title = books_data.title;
// var autor = books_data.autor;
// var price = books_data.price;
// var ASN = books_data.ASN;
// var stock = books_data.stock;
// console.log(title, autor);



// const {title, autor, price, ASN, stock} = books_data;
// console.log(title, autor, price, ASN, stock);


function Universo(planetas, galaxias, black_holes){
    this.planetas = planetas;
    this.galaxias = galaxias;
    this.black_holes = black_holes;
    this.constelacion = function (saludar){
        console.log('ejutando mi metodo constelacion, ',saludar);
    } 
}


var nuevaPlaneta = ['tierra', 'marte'];
var nuevaGalaxia =  ['via lactea', 'via andromeda'];
var nuevaBlackHole = 'blackX';

const univeso11 = new Universo(nuevaPlaneta, nuevaGalaxia, nuevaBlackHole);
console.log(univeso11);
console.log(univeso11.planetas)



const univeso12 = new Universo(['jupiter', 'saturno'], ['atena', 'andromeda'], 'BlackholeZ');
console.log(univeso12);
console.log(univeso12.planetas);

console.log(univeso12.constelacion('hola universo'));

delete univeso12.planetas;
console.log(univeso12);

