"use strict";
const defaultMessage = 'Bonjour RUBY CLEANING SERVICES, je souhaite obtenir un devis pour vos services de nettoyage.';
document.querySelectorAll('[data-wa], [data-service]').forEach(link => {
 const message = link.dataset.service ? `Bonjour RUBY CLEANING SERVICES, je souhaite obtenir un devis pour le service : ${link.dataset.service}.` : defaultMessage;
 link.href = `https://wa.me/212668192422?text=${encodeURIComponent(message)}`;
 link.target = '_blank'; link.rel = 'noopener noreferrer';
});
const backTop = document.querySelector('.back-top');
window.addEventListener('scroll', () => backTop.classList.toggle('visible', window.scrollY > 500), { passive: true });
backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' }));
