/*==================== SHOW MENU ====================*/
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId)


    if (toggle && nav) {
        toggle.addEventListener('click', () => {

            nav.classList.toggle('show-menu')
        })
    }
}
showMenu('nav-toggle', 'nav-menu')

/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction() {
    const navMenu = document.getElementById('nav-menu')

    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*==================== SCROLL SECTIONS ACTIVE LINK ====================*/
const sections = document.querySelectorAll('section[id]')

function scrollActive() {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
        } else {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

/*==================== CHANGE BACKGROUND HEADER ====================*/
function scrollHeader() {
    const nav = document.getElementById('header')

    if (this.scrollY >= 200) nav.classList.add('scroll-header');
    else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

/*==================== SHOW SCROLL TOP ====================*/
function scrollTop() {
    const scrollTop = document.getElementById('scroll-top');

    if (this.scrollY >= 560) scrollTop.classList.add('show-scroll');
    else scrollTop.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollTop)

/*==================== DARK LIGHT THEME ====================*/
const themeButton = document.getElementById('theme-button')
const darkTheme = 'dark-theme'
const iconTheme = 'bx-toggle-right'


const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')


const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx-toggle-left' : 'bx-toggle-right'


if (selectedTheme) {

    document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
    themeButton.classList[selectedIcon === 'bx-toggle-left' ? 'add' : 'remove'](iconTheme)
}


themeButton.addEventListener('click', () => {

    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)

    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})

/*==================== MENU ====================*/
const btns = document.querySelectorAll('.btn');
const dropMenus = document.querySelectorAll('.drop-menu');

btns.forEach(btn => {
    btn.addEventListener('click', () => {
        removeActive();
        btn.classList.add('active');
        document.querySelector(btn.dataset.target).classList.add('active');
    })
})

const removeActive = () => {
    btns.forEach(btn => btn.classList.remove('active'));
    dropMenus.forEach(dropmenu => dropmenu.classList.remove('active'));
}

window.onclick = (e) => {
    if (!e.target.matches('.btn')) {
        removeActive()
    }
}




/*==================== PRODUCT COLORS ====================*/

const imgs = document.querySelectorAll(".img-select a");
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener("click", (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage() {
    const displayWidth = document.querySelector(".img-showcase img:first-child").clientWidth;

    document.querySelector(".img-showcase").style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}








/*==================== PRODUCT QUANTITY PLUS MINUS ====================*/

window.onload = function () {
    var minusBtn = document.getElementById("minus"),
        plusBtn = document.getElementById("plus"),
        num__input = document.getElementById("num__input"),
        number = 0,
        min = 0,
        max = document.getElementById("product__stock").innerHTML;

    minusBtn.onclick = function () {
        let selectedQuantity = document.getElementById('selected__quantity');
        selectedQuantity.innerHTML = "";
        if (number > min) {
            number = number - 1;
            num__input.innerText = number;

            selectedQuantity.innerHTML = num__input.innerText;

        }
        if (number == min) {
            num__input.style.color = "red";
            setTimeout(function () {
                num__input.style.color = "black"
            }, 500)
        } else {
            num__input.style.color = "black";
        }

    }

    plusBtn.onclick = function () {
        let selectedQuantity = document.getElementById('selected__quantity');
        selectedQuantity.innerHTML = "";
        if (number < max) {
            number = number + 1;
            num__input.innerText = number;

            selectedQuantity.innerHTML = num__input.innerText;

        }
        if (number == max) {
            num__input.style.color = "red";
            setTimeout(function () {
                num__input.style.color = "black"
            }, 500)
        } else {
            num__input.style.color = "black";

        }


    }

    let selectedQuantity = document.getElementById('selected__quantity');
    selectedQuantity.innerHTML = "";

    selectedQuantity.innerHTML = number;



}



/*==================== PRODUCT COLORS ====================*/
const sizes = document.querySelectorAll('.size');
const gradients = document.querySelectorAll('.gradient');
const colors = document.querySelectorAll('.color');
const overlayBg = document.querySelector('.img-showcase');
const colorChange = document.querySelectorAll('.product__img');
let prevColor = "yellow";
let animationEnd = true;


function changeSize() {
    let selectedSize = document.getElementById('selected__size');
    selectedSize.innerHTML = "";

    sizes.forEach(size => size.classList.remove('active'));
    this.classList.add('active');
    selectedSize.innerHTML = this.innerHTML;
}

function changeColor() {
    if (!animationEnd) return;
    let primary = this.getAttribute('primary');
    let color = this.getAttribute('color');
    let product__img = document.querySelector(`.product__img[color="${color}"]`);
    let gradient = document.querySelector(`.gradient[color="${color}"]`);
    let prevGradient = document.querySelector(`.gradient[color="${prevColor}"]`);
    let selected = document.getElementById('select__color');
    selected.innerHTML = "";

    if (color == prevColor) return;

    colors.forEach(c => c.classList.remove('active'));
    this.classList.add('active');
    selected.innerHTML = this.getAttribute('color');

    document.documentElement.style.setProperty('--primary', primary);

    colorChange.forEach(s => s.classList.remove('show'));
    product__img.classList.add('show');

    gradients.forEach(g => g.classList.remove('first', 'second'));
    gradient.classList.add('first');
    prevGradient.classList.add('second');

    prevColor = color;
    animationEnd = false;

    gradient.addEventListener('animationend', () => {
        animationEnd = true;
    })
}
sizes.forEach(size => size.addEventListener('click', changeSize));
colors.forEach(c => c.addEventListener('click', changeColor));