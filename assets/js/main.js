document.addEventListener('DOMContentLoaded', () => {

    // 1. Scroll Progress Bar
    // const scrollProgress = document.getElementById('scroll-progress');
    window.addEventListener('scroll', () => {
        /* scroll progress removed */
    });

    // 2. Sticky Navbar & Back to Top
    const navbar = document.querySelector('.navbar');
    const backTop = document.querySelector('.back-top');
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > lastScrollY && currentScrollY > 100) {
            navbar.classList.add('nav-hidden');
        } else {
            navbar.classList.remove('nav-hidden');
        }
        
        if (currentScrollY > 60) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScrollY = currentScrollY;
        
        if (backTop) {
            if (window.scrollY > 400) {
                backTop.classList.add('visible');
            } else {
                backTop.classList.remove('visible');
            }
        }
    });

    if(backTop) {
        backTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // 3. Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu-overlay');
    const closeMenu = document.querySelector('.mobile-menu-close');

    if (hamburger && mobileMenu) {
        hamburger.addEventListener('click', () => {
            mobileMenu.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    }
    
    if (closeMenu && mobileMenu) {
        closeMenu.addEventListener('click', () => {
            mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    }

    // Close mobile menu when a link is clicked
    const mobileLinks = document.querySelectorAll('.mobile-menu-overlay a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            if(mobileMenu) {
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    });

    // 4. Intersection Observer for .reveal animations
    const observerOptions = {
        threshold: 0.05,
        rootMargin: "0px 0px -20px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => {
        // Immediately reveal if already in viewport
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight) {
            el.classList.add('visible');
        } else {
            observer.observe(el);
        }
    });

    // 5. WhatsApp Booking Form Logic
    const dateInput = document.getElementById('pref-date');
    if (dateInput) {
        const today = new Date();
        const year = today.getFullYear();
        let month = today.getMonth() + 1;
        let day = today.getDate();
        if (month < 10) month = '0' + month;
        if (day < 10) day = '0' + day;
        const minDate = `${year}-${month}-${day}`;
        dateInput.setAttribute('min', minDate);

        dateInput.addEventListener('input', function(e) {
            const selectedDate = new Date(this.value);
            const dayOfWeek = selectedDate.getUTCDay();
            if(dayOfWeek === 0) {
                e.preventDefault();
                this.value = '';
                alert('Sundays are closed. Please select another day.');
            }
        });
    }

    const form = document.getElementById('whatsappForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const nameElem = document.getElementById('pat-name');
            const phoneElem = document.getElementById('pat-phone');
            const docElem = document.getElementById('pref-doc');
            const treatElem = document.getElementById('pref-treat');
            const sessionElem = document.querySelector('input[name="session"]:checked');
            const dateElem = document.getElementById('pref-date');
            const msgElem = document.getElementById('add-msg');

            const name = nameElem ? nameElem.value : 'Not provided';
            const phone = phoneElem ? phoneElem.value : 'Not provided';
            const doc = docElem ? docElem.value : 'Any Doctor';
            const treat = treatElem ? treatElem.value : 'General Checkup';
            const session = sessionElem ? sessionElem.value : 'Not specified';
            
            let formattedDate = 'Not specified';
            if (dateElem && dateElem.value) {
                formattedDate = new Date(dateElem.value).toLocaleDateString('en-GB');
            }

            const msg = msgElem && msgElem.value ? msgElem.value : 'None';

            const message = `Hello Vels Dental Clinic!\nI'd like to book an appointment.\n\nName: ${name}\nMy Number: ${phone}\nDoctor Preferred: ${doc}\nTreatment: ${treat}\nSession: ${session}\nDate: ${formattedDate}\nMessage: ${msg}`;

            const encoded = encodeURIComponent(message);
            const whatsappUrl = 'https://api.whatsapp.com/send?phone=919894888736&text=' + encoded;
            const newWindow = window.open(whatsappUrl, '_blank');
            if (!newWindow || newWindow.closed || typeof newWindow.closed == 'undefined') {
                window.location.href = whatsappUrl;
            }
        });
    }

    // 6. Auto-select treatment from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const treatmentParam = urlParams.get('treatment');
    if (treatmentParam) {
        const treatSelect = document.getElementById('pref-treat');
        if (treatSelect) {
            // Check if there is an option that exactly matches the treatment param
            let optionMatched = false;
            for (let i = 0; i < treatSelect.options.length; i++) {
                if (treatSelect.options[i].value === treatmentParam) {
                    treatSelect.selectedIndex = i;
                    optionMatched = true;
                    break;
                }
            }
            // If no exact match on value, try more flexible matching
            if (!optionMatched) {
                const lowerParam = treatmentParam.toLowerCase();
                for (let i = 0; i < treatSelect.options.length; i++) {
                    const optText = treatSelect.options[i].textContent.toLowerCase();
                    const optVal = treatSelect.options[i].value.toLowerCase();
                    
                    if (optText.includes(lowerParam) || lowerParam.includes(optText) || 
                        optVal.includes(lowerParam) || lowerParam.includes(optVal)) {
                        treatSelect.selectedIndex = i;
                        break;
                    }
                }
            }
        }
    }
    
    // 7. Custom Select UI Initialization
    const selects = document.querySelectorAll('select');
    selects.forEach(select => {
        if (select.nextElementSibling && select.nextElementSibling.classList.contains('custom-select-wrapper')) return;

        select.style.display = 'none';
        
        const wrapper = document.createElement('div');
        wrapper.className = 'custom-select-wrapper';
        
        const trigger = document.createElement('div');
        trigger.className = 'custom-select-trigger';
        const span = document.createElement('span');
        span.textContent = select.options[select.selectedIndex].textContent;
        const icon = document.createElement('i');
        icon.className = 'fas fa-chevron-down';
        
        trigger.appendChild(span);
        trigger.appendChild(icon);
        
        const optionsList = document.createElement('div');
        optionsList.className = 'custom-options';
        
        Array.from(select.options).forEach((option, index) => {
            const customOption = document.createElement('div');
            customOption.className = 'custom-option';
            if (index === select.selectedIndex) customOption.classList.add('selected');
            customOption.textContent = option.textContent;
            customOption.dataset.value = option.value;
            
            customOption.addEventListener('click', function(e) {
                e.stopPropagation();
                select.selectedIndex = index;
                select.dispatchEvent(new Event('change'));
                
                span.textContent = this.textContent;
                
                optionsList.querySelectorAll('.custom-option').forEach(opt => opt.classList.remove('selected'));
                this.classList.add('selected');
                
                wrapper.classList.remove('open');
            });
            
            optionsList.appendChild(customOption);
        });
        
        trigger.addEventListener('click', function(e) {
            e.stopPropagation();
            document.querySelectorAll('.custom-select-wrapper').forEach(w => {
                if (w !== wrapper) w.classList.remove('open');
            });
            wrapper.classList.toggle('open');
            
            // Scroll to selected option
            if (wrapper.classList.contains('open')) {
                const selectedOpt = optionsList.querySelector('.selected');
                if (selectedOpt) {
                    optionsList.scrollTop = selectedOpt.offsetTop - 10;
                }
            }
        });
        
        wrapper.appendChild(trigger);
        wrapper.appendChild(optionsList);
        
        select.parentNode.insertBefore(wrapper, select.nextSibling);
    });

    document.addEventListener('click', function() {
        document.querySelectorAll('.custom-select-wrapper').forEach(w => w.classList.remove('open'));
    });
});

// 7. Preloader fade out
setTimeout(() => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        preloader.style.opacity = '0';
        preloader.style.visibility = 'hidden';
        setTimeout(() => {
            preloader.remove();
        }, 500);
    }
}, 1000);
