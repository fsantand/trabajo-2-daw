/**
 * Carrusel simple de imagenes con JS Nativo
 * No esta optimizado para 2 carruseles en el misma pagina actualmente
 */

var indiceCarrusel = 0;
var cantidadSlides = -1;
var selectores = [];
var photos = []

// Funcion de modulo para valores negativos
const mod = (n, m) => ((n % m) + m) % m;

const nextFoto = (n) => {
    if (n != indiceCarrusel) updateSlide((n != null ? n : indiceCarrusel + 1));
}

const prevFoto = (n) => {
    if (n != indiceCarrusel) updateSlide((n != null ? n : indiceCarrusel - 1));
}

const updateSlide = (n) => {
    indiceCarrusel = mod(n, cantidadSlides);
    now = indiceCarrusel;
    document.getElementsByClassName('carousel__selector--active')[0].classList.toggle('carousel__selector--active');
    selectores[now].classList.toggle('carousel__selector--active');
    for (let i = 0; i < photos.length; i++) {
        if (i != now) photos[i].style.display = 'none';
        else photos[i].style.display = 'inline-block';
    }
}

/**
 * Añade los selectores al carrusel
 * 
 * @param {Object} selectorRoot - La raiz donde se insertarán los selectores
 * @param {Number} n - El numero de selectores a añadir
 * @param {Number} firstActive - La primera slide que estará activa
 */
const addSelectors = (selectorRoot, n, firstActive = 0) => {
    // Construccion segura del elemento selector  
    const selectorElement = document.createElement("a");
    selectorElement.classList.toggle('carousel__selector');
    selectorElement.href = '#';

    // Limpieza de cualquier codigo html dentro del selector raiz
    selectorRoot.innerHTML = '';

    for (let i = 0; i < n; i++) {
        let currentSelector = selectorElement.cloneNode();
        if (i == firstActive)
            currentSelector.classList.toggle('carousel__selector--active');


        //Añadir evento a selector
        currentSelector.addEventListener('click', () => updateSlide(i));
        selectorRoot.appendChild(currentSelector);
    }

    return selectorRoot.childNodes;
}

const Carrusel = (id) => {
    const carrusel = document.getElementById(id);
    photos = carrusel.getElementsByClassName("carousel__item");
    cantidadSlides = photos.length;

    // Setear el primero visible
    if (cantidadSlides > 0) {
        indiceCarrusel = 0;
        photos[0].style.display = 'inline-block';
    } else {
        console.log("El carrusel debe tener al menos 1 foto");
    }

    // Añadir Selectores
    let selectoresRoot = carrusel.getElementsByClassName("carousel__selectors")[0];
    selectores = addSelectors(selectoresRoot, cantidadSlides);

    // Agregar eventos
    // Nav izquierda y derecha
    let navLeft = carrusel.getElementsByClassName("carousel__control--left");
    navLeft[0].addEventListener('click', () => prevFoto());
    let navRight = carrusel.getElementsByClassName("carousel__control--right");
    navRight[0].addEventListener('click', () => nextFoto());

    //Selectores


    return carrusel;
}