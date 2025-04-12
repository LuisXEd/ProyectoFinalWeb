document.addEventListener("DOMContentLoaded", function () {
    // --- MODO OSCURO ---
    const modoOscuroBtn = document.getElementById("modoOscuroBtn");
    const body = document.body;
  
    // Verificar si el modo oscuro está activado en localStorage
    if (localStorage.getItem("modoOscuro") === "true") {
      body.classList.add("dark-mode");
      if (modoOscuroBtn) {
        modoOscuroBtn.textContent = "☀️ Modo Claro";
      }
    }
  
    // Configurar el evento para cambiar el modo
    if (modoOscuroBtn) {
      modoOscuroBtn.addEventListener("click", function () {
        body.classList.toggle("dark-mode");
        localStorage.setItem("modoOscuro", body.classList.contains("dark-mode"));
        modoOscuroBtn.textContent = body.classList.contains("dark-mode") ? "☀️ Modo Claro" : "🌙 Modo Oscuro";
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
  
    // --- AJUSTAR ALTURA DE TARJETAS AUTOMÁTICAMENTE ---
    function ajustarAlturaTarjetas() {
      let tarjetas = document.querySelectorAll(".news-card");
      let maxAltura = 0;
  
      // Resetear la altura antes de medir
      tarjetas.forEach(tarjeta => {
        tarjeta.style.height = "auto";
      });
  
      // Calcular la altura máxima
      tarjetas.forEach(tarjeta => {
        let altura = tarjeta.offsetHeight;
        if (altura > maxAltura) {
          maxAltura = altura;
        }
      });
  
      // Asignar la misma altura a todas las tarjetas
      tarjetas.forEach(tarjeta => {
        tarjeta.style.height = maxAltura + "px";
      });
    }
    ajustarAlturaTarjetas();
    window.addEventListener("resize", ajustarAlturaTarjetas);
  
    // --- BÚSQUEDA AJAX GENÉRICA ---
    const ajaxSearchInputs = document.querySelectorAll(".buscador-ajax");
    ajaxSearchInputs.forEach(input => {
      const url = input.getAttribute("data-url");
      const targetId = input.getAttribute("data-target");
      const container = document.getElementById(targetId);
      if (!url || !container) return; // Si falta algún atributo, sale
  
      input.addEventListener("input", function () {
        const query = input.value;
        // Realizamos la petición a la URL pasando el parámetro "q" (o el que definas)
        fetch(`${url}?q=${encodeURIComponent(query)}`, {
          headers: {
            "X-Requested-With": "XMLHttpRequest"
          }
        })
        .then(response => response.json())
        .then(data => {
          container.innerHTML = data.html;
        })
        .catch(err => console.error("Error en la búsqueda AJAX:", err));
      });
    });
  });

  
function mostrarReceta(titulo, imagen, pelicula, ingredientes, preparacion) {
  document.getElementById("modalRecetaLabel").textContent = titulo;
  document.getElementById("recetaImagen").src = imagen;
  document.getElementById("recetaImagen").alt = titulo;
  document.getElementById("peliculaReferencia").textContent = "📽️ Inspirado en: " + pelicula;

  const listaIngredientes = document.getElementById("recetaIngredientes");
  listaIngredientes.innerHTML = "";
  ingredientes.replace(/[\[\]']/g, '').split(',').forEach(item => {
    const li = document.createElement("li");
    li.textContent = item.trim();
    listaIngredientes.appendChild(li);
  });

  document.getElementById("recetaPreparacion").textContent = preparacion;

  const modal = new bootstrap.Modal(document.getElementById("modalReceta"));
  modal.show();
}
