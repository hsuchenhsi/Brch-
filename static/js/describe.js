document.addEventListener('DOMContentLoaded', function() {
    // 模態窗口相關
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

    // 標籤切換功能相關
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

    // 評星功能相關
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

    // 購物車數量和尺寸選擇相關
    const numElement = document.querySelector('.num');
    const plusButton = document.querySelector('.plus-btn');
    const minusButton = document.querySelector('.minus-btn');
    const addToCartButton = document.querySelector('.addToCart');
    const selectedSizeElement = document.querySelector('.selected-size');
    let num = 0;
    let quantity = 0;
    let selectedSize = null;

    plusButton.addEventListener('click', function() {
        num++;
        numElement.textContent = num;
    });

    minusButton.addEventListener('click', function() {
        if (num > 0) {
            num--;
            numElement.textContent = num;
        }
    });

    addToCartButton.addEventListener('click', function() {
        if (selectedSize !== null && num > 0) {
            quantity += num;
            num = 0;
            numElement.textContent = num;
            updateCartQuantity(quantity);
            selectedSizeElement.textContent = "未選擇";
        }
    });

    const sizeButtons = document.querySelectorAll('.size-buttons button');
    sizeButtons.forEach(button => {
        button.addEventListener('click', function() {
            selectedSize = this.getAttribute('data-size');
            selectedSizeElement.textContent = selectedSize;
        });
    });

    function updateCartQuantity(quantity) {
        const quantityElement = document.querySelector('.quantity');
        quantityElement.textContent = quantity;
    }

    // 提交評論相關
    const submitButton = document.querySelector('#modal button:last-of-type');
    const textarea = document.querySelector('#modal textarea');

    submitButton.onclick = function() {
        const comment = textarea.value;
        if (comment.length < 5 || currentRating === 0 || selectedSize === '') {
            alert('請填寫完整評論、評分和尺寸');
            return;
        }

        const product_id = 1; // 替換為你要評論的商品 ID

        fetch(`/submit_review/${product_id}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `rating=${currentRating}&comment=${comment}&size=${selectedSize}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('評論提交成功');
                modal.style.display = 'none';
            } else {
                alert('評論提交失敗');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('評論提交失敗');
        });
    }
});
