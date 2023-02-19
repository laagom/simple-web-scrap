'use strict'
const loader    = document.querySelector('.loader')
const subTitle  = document.querySelector('.sub-title')
const form      = document.querySelector('.form');
const links     = document.querySelectorAll('.popular');

links.forEach((link) => {
    link.addEventListener('click', () => {
        loader.classList.remove('hidden');
        subTitle.classList.add('hidden');
    });
});

form.addEventListener('submit', () => {
    loader.classList.remove('hidden');
    subTitle.classList.add('hidden');
});
