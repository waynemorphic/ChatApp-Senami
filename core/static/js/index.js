
document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function (param) {
    if (param.keycode === 13) {
        document.querySelector('#room-name-submit').onclick();
    }
};

document.querySelector('#room-name-submit').onclick = function (param) {
    let roomName = document.querySelector('#room-name-input').value;
    window.location.pathname = '/Senami/' + roomName + '/';
    if (roomName === '') {
        window.location.pathname = '/Senami/';
    }

};