let formFour = document.getElementsByClassName('form_fournisseur')[0];
let newFour = document.getElementsByClassName('new_fournisseur')[0];
let formGross = document.getElementsByClassName('form_grossiste')[0];
let newGross = document.getElementsByClassName('new_grossiste')[0];
let formPart = document.getElementsByClassName('form_partenaire')[0];
let newPart = document.getElementsByClassName('new_partenaire')[0];
formFour.style.display = 'none'
formGross.style.display = 'none'
formPart.style.display = 'none'

newFour.addEventListener('click', function() {
    if (formFour.style.display == 'none') {
        formFour.style.display = 'block';
    }
    else {
        formFour.style.display = 'none'
    }
})

newGross.addEventListener('click', function() {
    if (formGross.style.display == 'none') {
        formGross.style.display = 'block';
    }
    else {
        formGross.style.display = 'none'
    }
})

newPart.addEventListener('click', function() {
    if (formPart.style.display == 'none') {
        formPart.style.display = 'block';
    }
    else {
        formPart.style.display = 'none'
    }
})

// Etrange... ne fonctionne pas
// function openClose(form) {
//     if (form.style.display == 'none') {
//         form.style.display = 'block';
//     }
//     else {
//         formFour.style.display = 'none'
//     }
// }
