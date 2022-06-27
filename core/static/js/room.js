

const roomName = JSON.parse(document.getElementById("room-name").textContent);
console.log(roomName)

const user_username = JSON.parse(document.getElementById('user_username').textContent);
console.log(user_username)

const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/Senami/' + roomName + '/'
);

chatSocket.addEventListener('error', function (event) {
    console.log('WebSocket error: ', event);
});

chatSocket.onmessage = function (param) {
    const data = JSON.parse(param.data);
    console.log(data)
    document.querySelector('#chat-log').value += (data.username + ':' + data.message + '\n');
};

chatSocket.onclose = function (param) {
    console.error("Chat socket closed unexpectedly");
};


document.querySelector("#chat-message-input").focus();
document.querySelector('#chat-message-input').onkeyup = function (param) {
    if (param.keycode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (param) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': user_username,
    }));
    messageInputDom.value = '';
};