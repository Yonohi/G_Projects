let formFour = document.getElementsByClassName('form_fournisseur')[0];
let newFour = document.getElementsByClassName('new_fournisseur')[0];
let formGross = document.getElementsByClassName('form_grossiste')[0];
let newGross = document.getElementsByClassName('new_grossiste')[0];
let formPart = document.getElementsByClassName('form_partenaire')[0];
let newPart = document.getElementsByClassName('new_partenaire')[0];
let hasObjectif = document.getElementById('id_has_objectif');
let objectif = document.getElementsByClassName('objectif_form')[0];

// Attribution de la valeur adéquate
formFour.style.display = 'none'
formGross.style.display = 'none'
formPart.style.display = 'none'
objectif.style.display = 'none'

// Fonction d'affichage ou de fermeture d'un formulaire
function openClose(elmt, elmtDisplay='block') {
    if (elmt.style.display == 'none') 
        elmt.style.display = elmtDisplay;
    else 
        elmt.style.display = 'none';
};

// Mise à l'écoute des éléments voulus
newFour.addEventListener('click', function() {openClose(formFour)})
newGross.addEventListener('click', function() {openClose(formGross)})
newPart.addEventListener('click', function() {openClose(formPart)})
hasObjectif.addEventListener('click', function() {openClose(objectif,elmtDisplay='flex')})
