let btnGenerar = document.getElementById("idbtngenerarreporte");
let btnOcultarReporte = document.getElementById("idbtnocultararreporte");
let contenedor = document.getElementById("conenedor");



btnGenerar.addEventListener('click', (evento) =>{
    evento.preventDefault()
    contenedor.classList.remove("d-none");
})
