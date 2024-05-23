
const modal = document.getElementById('modal');
const btn = document.getElementById('openModalButton');
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

document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        const tabID = tab.getAttribute('data-tab');
        const tabContent = document.getElementById(tabID + '-content');

        document.querySelectorAll('.tab').forEach(item => {
            item.classList.remove('active');
        });
        document.querySelectorAll('.content').forEach(content => {
            content.classList.remove('active');
        });

        tab.classList.add('active');
        tabContent.classList.add('active');
    });
});




