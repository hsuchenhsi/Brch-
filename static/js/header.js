let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let list = document.querySelector('.list');
let listCard = document.querySelector('.listCard');
let body = document.querySelector('.body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

openShopping.addEventListener('click',()=>{
    body.classList.add('active');
})

closeShopping.addEventListener('click',()=>{
    body.classList.remove('active');
})

const modal = document.getElementById('modal');
const login = document.getElementById('login');
const btn = document.getElementById('user');
const span = document.getElementsByClassName('close')[0];

btn.onclick = function() {
    modal.style.display = 'block';
}

span.onclick = function() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
// let products = [
//     {
//         id:1,
//         name:'我不知道這叫什麼',
//         img:'2.jpg',
//         price:299
//     },
//     {
//         id:2,
//         name:'我不知道這叫什麼',
//         img:'2.jpg',
//         price:299
//     },
//     {
//         id:3,
//         name:'我不知道這叫什麼',
//         img:'2.jpg',
//         price:299
//     },
//     {
//         id:4,
//         name:'我不知道這叫什麼',
//         img:'2.jpg',
//         price:299
//     },

// ];

// let listCards = [];
// function initApp(){
//     products.forEach((value, key)=>{
//         let newDiv = document.createElement('div');
//         newDiv.classList.add('item');
//         newDiv.innerHTML = `
//             <img src="img/${value.img}"/>;
//             <div class="title">${value.name}</div>
//             <div class="price">${value.price.toLocaleString()}</div>
//         `;
//         list.appendChild(newDiv);
//     })
// }
// initApp();


// function addToCard(key){
//     if(listCard[key] == null){
//         listCard[key] == product[key];
//         listCard[key].quantity = 1;
//     }
//     reloadCard();
// }
// function reloadCard(){
//     listCard.innerHTML = '';
//     let count = 0;
//     let totalPrice =0;
//     listCard.forEach((value, key) => {
//         totalPrice = totalPrice + value.price;
//         count = count + value.quantity;
//     })
//     total.innerHTML
// }