document.addEventListener("DOMContentLoaded", () => {
    console.log("👋 script.js cargado: modo prueba.");
  
    const btn = document.getElementById("modoOscuroBtn");
    if (!btn) {
      console.warn("❌ No se encontró el botón con id='modoOscuroBtn'.");
      return;
    }
    console.log("✅ Botón #modoOscuroBtn detectado.");
  
    btn.addEventListener("click", () => {
      console.log("🖱️ Se hizo clic en el botón. Cambiemos el modo.");
      alert("Botón clickeado. Modo oscuro hipotético.");
    });
  });
  