// 生成验证码
function generateCaptcha() {
    const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let captcha = '';
    for (let i = 0; i < 4; i++) {
        captcha += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return captcha;
}

// 切换密码可见性
const togglePassword = document.getElementById('togglePassword');
const passwordInput = document.getElementById('password');

togglePassword.addEventListener('click', () => {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    togglePassword.querySelector('i').classList.toggle('fa-eye');
    togglePassword.querySelector('i').classList.toggle('fa-eye-slash');
});

// 初始化验证码
let currentCaptcha = generateCaptcha();
const captchaText = document.getElementById('captchaText');
const captchaBox = document.getElementById('captchaBox');

captchaText.textContent = currentCaptcha;

captchaBox.addEventListener('click', () => {
    currentCaptcha = generateCaptcha();
    captchaText.textContent = currentCaptcha;
    captchaBox.classList.add('animate-pulse');
    setTimeout(() => captchaBox.classList.remove('animate-pulse'), 500);
});

// 表单验证
document.getElementById('loginForm').addEventListener('submit', (e) => {
    e.preventDefault();

    const phoneInput = document.getElementById('phone');
    const captchaInput = document.getElementById('captcha');
    const phoneError = document.getElementById('phoneError');
    const passwordError = document.getElementById('passwordError');
    const captchaError = document.getElementById('captchaError');

    let isValid = true;

    const phoneRegex = /^1[3-9]\d{9}$/;
    if (!phoneRegex.test(phoneInput.value)) {
        phoneError.classList.remove('hidden');
        isValid = false;
    } else {
        phoneError.classList.add('hidden');
    }

    if (passwordInput.value.trim() === '') {
        passwordError.classList.remove('hidden');
        isValid = false;
    } else {
        passwordError.classList.add('hidden');
    }

    if (captchaInput.value.trim() === '' || captchaInput.value.toUpperCase() !== currentCaptcha) {
        captchaError.classList.remove('hidden');
        isValid = false;
    } else {
        captchaError.classList.add('hidden');
    }

    if (isValid) {
        loginForm.submit();
    }
});
