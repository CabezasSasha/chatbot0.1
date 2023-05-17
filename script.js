// Seleccionamos los elementos HTML necesarios
const userInput = document.querySelector('#userInput');
const sendButton = document.querySelector('#sendButton');
const conversation = document.querySelector('.conversation');


// Función para agregar un mensaje a la conversación
function addMessage(msg, className) {
    const msgContainer = document.createElement('div');
    msgContainer.classList.add('msg-container', className);

    const msgElement = document.createElement('div');
    msgElement.classList.add('msg');
    msgElement.textContent = msg;

    msgContainer.appendChild(msgElement);
    conversation.appendChild(msgContainer);

    conversation.scrollTop = conversation.scrollHeight;
}

// Evento para enviar un mensaje al bot
sendButton.addEventListener('click', () => {
    const userText = userInput.value.trim();

    if (userText !== '') {
        addMessage(userText, 'user');
        userInput.value = '';
        fetch(`/get?msg=${userText}`)
            .then(response => response.text())
            .then(botResponse => {
                addMessage(botResponse, 'bot');
            });
    }
});

// Evento para enviar un mensaje al bot al presionar Enter
userInput.addEventListener('keydown', event => {
    if (event.keyCode === 13) {
        event.preventDefault();
        sendButton.click();
    }
});
