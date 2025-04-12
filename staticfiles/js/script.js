document.addEventListener("DOMContentLoaded", function () {
    const modoOscuroBtn = document.getElementById("modoOscuroBtn");
    const body = document.body;

    // 🌙 Verificar si el modo oscuro está activado en localStorage
    if (localStorage.getItem("modoOscuro") === "true") {
        body.classList.add("dark-mode");
        if (modoOscuroBtn) modoOscuroBtn.textContent = "☀️ Modo Claro";
    }

    // --- ALERTAS DE BIENVENIDA SEGÚN LA PÁGINA ---
    const currentPage = window.location.pathname; // Obtiene el nombre del archivo HTML
    switch (currentPage) {
        case "peliculas":
            setTimeout(() => {
                alert("🎬 Bienvenido a la sección de Películas. Encuentra las mejores opciones para tu noche de cine.");
            }, 1000);
            break;
        case "/comida/":
            setTimeout(() => {
                alert("🍕 Bienvenido a la sección de Comida. Descubre recetas deliciosas para acompañar tus películas.");
            }, 1000);
            break;
        case "/decoracion/":
            setTimeout(() => {
                alert("🏠 Bienvenido a la sección de Decoración. Crea el mejor ambiente para tu cine en casa.");
            }, 1000);
            break;
        case "/contacto/":
            setTimeout(() => {
                alert("📩 ¡Bienvenido a Contacto! Escríbenos para cualquier consulta o sugerencia.");
            }, 1000);
            break;
        case "/enlaces/":
            setTimeout(() => {
                alert("🔗 Explora Enlaces de Interés con videos y ubicaciones especiales para cinéfilos.");
            }, 1000);
            break;
        case "/noticias/":
            setTimeout(() => {
                alert("📰 Mantente informado con las últimas noticias del cine y la gastronomía.");
            }, 1000);
            break;
    }

    // --- ALERTA AL ACTIVAR/DESACTIVAR MODO OSCURO ---
    if (modoOscuroBtn) {
        modoOscuroBtn.addEventListener("click", function () {
            body.classList.toggle("dark-mode");
            let modo = body.classList.contains("dark-mode") ? "🌙 Modo oscuro activado" : "☀️ Modo claro activado";
            alert(modo);

            // Guardar preferencia en localStorage
            localStorage.setItem("modoOscuro", body.classList.contains("dark-mode"));
            modoOscuroBtn.textContent = body.classList.contains("dark-mode") ? "☀️ Modo Claro" : "🌙 Modo Oscuro";
        });
    }

    // --- ALERTA AL ENVIAR MENSAJE EN CONTACTO ---
    const btnEnviar = document.getElementById("btnEnviar");
    if (btnEnviar) {
        btnEnviar.addEventListener("click", function () {
            alert("✅ Tu mensaje ha sido enviado. ¡Gracias por contactarnos!");
        });
    }

    // --- MODAL PARA NOTICIAS ---
    const botonesNoticias = document.querySelectorAll(".btn-noticia");
    botonesNoticias.forEach(boton => {
        boton.addEventListener("click", function () {
            const noticiaTitulo = this.getAttribute("data-title");
            const noticiaContenido = this.getAttribute("data-content");

            document.getElementById("modalNoticiaLabel").textContent = noticiaTitulo;
            document.getElementById("modalNoticiaBody").textContent = noticiaContenido;

            const modal = new bootstrap.Modal(document.getElementById("modalNoticia"));
            modal.show();
        });
    });

    // --- ALERTA AL HACER CLICK EN UN MAILTO ---
    const mailtoLinks = document.querySelectorAll("a[href^='mailto']");
    mailtoLinks.forEach(link => {
        link.addEventListener("click", function () {
            alert("📩 Redirigiendo a tu correo para enviar un mensaje...");
        });
    });

    // --- ALERTA AL VISITAR UNA RED SOCIAL ---
    const socialIcons = document.querySelectorAll(".social-icons a");
    socialIcons.forEach(icon => {
        icon.addEventListener("click", function () {
            alert("🌍 Abriendo redes sociales en una nueva pestaña...");
        });
    });

    // --- AJUSTAR ALTURA DE TARJETAS AUTOMÁTICAMENTE ---
    function ajustarAlturaTarjetas() {
        let tarjetas = document.querySelectorAll(".news-card");
        let maxAltura = 0;

        // Resetear la altura antes de calcular (para evitar acumulación)
        tarjetas.forEach(tarjeta => {
            tarjeta.style.height = "auto";
        });

        // Obtener la altura máxima entre todas las tarjetas
        tarjetas.forEach(tarjeta => {
            let altura = tarjeta.offsetHeight;
            if (altura > maxAltura) {
                maxAltura = altura;
            }
        });

        // Aplicar la misma altura a todas las tarjetas
        tarjetas.forEach(tarjeta => {
            tarjeta.style.height = maxAltura + "px";
        });
    }

    // Ejecutar cuando se cargue la página
    ajustarAlturaTarjetas();

    // Volver a ejecutar cuando se cambia el tamaño de la ventana
    window.addEventListener("resize", ajustarAlturaTarjetas);
});
