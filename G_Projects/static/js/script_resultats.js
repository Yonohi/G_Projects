let linkRes = document.getElementsByClassName('link_results')[0];
let reste = document.getElementsByClassName('reste')[0];

reste.style.display = 'none'


linkRes.addEventListener('click', function() {
    if (reste.style.display == 'none') {
        reste.style.display = 'block';
        linkRes.innerHTML = 'Ne plus afficher';
    } else {
        reste.style.display = 'none';
        linkRes.innerHTML = 'Afficher plus de résultats';  
    }
})
