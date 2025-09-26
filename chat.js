function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value.trim();
    var chatBox = document.getElementById('chat-box');

    if (message !== '') {
        var messageElement = document.createElement('div');
        var timeStamp = new Date().toLocaleString();
        messageElement.innerHTML = `
            <div class="message sent">
                <span>${message}</span>
                <div class="timestamp">${timeStamp}</div>
            </div>`;
        chatBox.appendChild(messageElement);
        messageInput.value = '';
        chatBox.scrollTop = chatBox.scrollHeight; // Automatically scroll to the bottom
    }
}

