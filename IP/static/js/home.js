// 导航栏滚动效果
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('py-2', 'shadow-md');
        navbar.classList.remove('py-4');
    } else {
        navbar.classList.add('py-4');
        navbar.classList.remove('py-2', 'shadow-md');
    }
});

// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// 返回顶部按钮
const backToTopButton = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTopButton.classList.remove('opacity-0', 'invisible');
        backToTopButton.classList.add('opacity-100', 'visible');
    } else {
        backToTopButton.classList.add('opacity-0', 'invisible');
        backToTopButton.classList.remove('opacity-100', 'visible');
    }
});

backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// 数字增长动画
const animateNumbers = () => {
    const numberElements = document.querySelectorAll('.animate-number');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const numberElement = entry.target;
                const target = parseInt(numberElement.getAttribute('data-target'));
                let current = 0;
                const increment = Math.ceil(target / 50); // 分50步完成动画

                const updateNumber = () => {
                    current += increment;
                    if (current < target) {
                        numberElement.textContent = current;
                        requestAnimationFrame(updateNumber);
                    } else {
                        numberElement.textContent = target;
                    }
                };

                updateNumber();
                observer.unobserve(numberElement);
            }
        });
    }, { threshold: 0.5 });

    numberElements.forEach(element => {
        observer.observe(element);
    });
};

// 页面加载完成后执行动画
window.addEventListener('load', () => {
    animateNumbers();
});