document.addEventListener('DOMContentLoaded', () => {
    const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port +'/Chat_room');
    socket.on('connect', () => {
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.room;
                if(selection==="submit"){
                    alert("g8")
                    const message_text = document.getElementById("myInput").value;
                    socket.emit('submit message', {'message_text' : message_text});
                };
            };
        });
    });
    socket.on('broadcast message', data => {
        alert("g9")
        document.querySelector(`#m${data.message_counter}`).innerHTML = data['message_text'][data['message_text'].length -1];        
        
    });
});
