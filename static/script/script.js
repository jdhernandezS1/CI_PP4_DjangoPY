function timeout() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}

setTimeout(timeout() , 3000); 