let formClient = document.getElementsByClassName('form_client')[0];
let newClient = document.getElementsByClassName('new_client')[0];
formClient.style.display = 'none'

newClient.addEventListener('click', function() {
    formClient.style.display = 'block';
})
