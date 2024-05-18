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

let products = [
    {
        id:1,
        name:'我不知道這叫什麼',
        img:'2.jpg',
        price:299
    },
    {
        id:2,
        name:'我不知道這叫什麼',
        img:'2.jpg',
        price:299
    },
    {
        id:3,
        name:'我不知道這叫什麼',
        img:'2.jpg',
        price:299
    },
    {
        id:4,
        name:'我不知道這叫什麼',
        img:'2.jpg',
        price:299
    },

];

let listCards = [];
function initApp(){
    products.forEach((value, key)=>{
        let newDiv = document.createElement('div');
        newDiv.classList.add('item');
        newDiv.innerHTML = `
            <img src="img/${value.img}"/>;
            <div class="title">${value.name}</div>
            <div class="price">${value.price.toLocaleString()}</div>
        `;
        list.appendChild(newDiv);
    })
}
initApp();
