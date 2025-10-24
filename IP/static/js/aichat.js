// 页面加载后自动滚动到底部
window.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chatBox');
    chatBox.scrollTop = chatBox.scrollHeight;
});

const typingIndicator = document.getElementById('typingIndicator');
const chatBox = document.getElementById('chatBox');

function showTyping() {
    typingIndicator.style.opacity = '1';
    chatBox.scrollTop = chatBox.scrollHeight;
}

function hideTyping() {
    typingIndicator.style.opacity = '0';
}
