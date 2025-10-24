// register.js

// 头像上传预览
const avatarUpload = document.getElementById('avatarUpload');
const avatarImage = document.getElementById('avatarImage');

avatarUpload?.addEventListener('change', function () {
    if (this.files && this.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            avatarImage.src = e.target.result;
        }
        reader.readAsDataURL(this.files[0]);
    }
});

// 切换密码可见性
document.querySelectorAll('.togglePassword').forEach(button => {
    button.addEventListener('click', () => {
        const passwordInput = button.parentElement.querySelector('input');
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);

        // 切换图标
        const icon = button.querySelector('i');
        icon.classList.toggle('fa-eye');
        icon.classList.toggle('fa-eye-slash');
    });
});

// 表单提交验证
const form = document.getElementById('registerForm');

document.getElementById('registerForm')?.addEventListener('submit', (e) => {
    e.preventDefault();

    const usernameInput = document.getElementById('username');
    const phoneInput = document.getElementById('phone');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const termsInput = document.getElementById('terms');

    const usernameError = document.getElementById('usernameError');
    const phoneError = document.getElementById('phoneError');
    const passwordError = document.getElementById('passwordError');
    const confirmPasswordError = document.getElementById('confirmPasswordError');
    const termsError = document.getElementById('termsError');

    let isValid = true;

    // 用户名验证
    if (usernameInput.value.trim() === '') {
        usernameError.classList.remove('hidden');
        isValid = false;
    } else {
        usernameError.classList.add('hidden');
    }

    // 手机号验证
    const phoneRegex = /^1[3-9]\d{9}$/;
    if (!phoneRegex.test(phoneInput.value)) {
        phoneError.classList.remove('hidden');
        isValid = false;
    } else {
        phoneError.classList.add('hidden');
    }

    // 密码验证
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(passwordInput.value)) {
        passwordError.classList.remove('hidden');
        isValid = false;
    } else {
        passwordError.classList.add('hidden');
    }

    // 确认密码验证
    if (confirmPasswordInput.value !== passwordInput.value) {
        confirmPasswordError.classList.remove('hidden');
        isValid = false;
    } else {
        confirmPasswordError.classList.add('hidden');
    }

    // 同意协议验证
    if (!termsInput.checked) {
        termsError.classList.remove('hidden');
        isValid = false;
    } else {
        termsError.classList.add('hidden');
    }

    if (isValid && form) {
        form.submit();
    }
});