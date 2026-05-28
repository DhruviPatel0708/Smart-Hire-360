AOS.init({
    duration: 1200
});

gsap.from('.hero-title', {
    y: -80,
    opacity: 0,
    duration: 1.5
});

gsap.from('.hero-subtitle', {
    y: 50,
    opacity: 0,
    duration: 1.5,
    delay: 0.5
});

gsap.from('.hero-buttons', {
    y: 50,
    opacity: 0,
    duration: 1.5,
    delay: 1
});