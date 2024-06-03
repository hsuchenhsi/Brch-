
document.addEventListener('DOMContentLoaded', function() {
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
});

document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star');
    const ratingDisplay = document.getElementById('rating');
    let currentRating = 0;

    stars.forEach(star => {
        star.addEventListener('mouseover', function() {
            const value = this.getAttribute('data-value');
            highlightStars(value);
            ratingDisplay.textContent = value;
        });

        star.addEventListener('mouseout', function() {
            if (currentRating === 0) {
                resetStars();
                ratingDisplay.textContent = '0';
            } else {
                highlightStars(currentRating);
                ratingDisplay.textContent = currentRating;
            }
        });

        star.addEventListener('click', function() {
            const value = this.getAttribute('data-value');
            currentRating = value;
            highlightStars(value);
            ratingDisplay.textContent = value;
        });
    });

    function highlightStars(value) {
        stars.forEach(star => {
            star.style.color = star.getAttribute('data-value') <= value ? 'Pink' : 'lavenderblush';
        });
    }

    function resetStars() {
        stars.forEach(star => {
            star.style.color = 'lightgrey';
        });
    }
    });



