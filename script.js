const openButton = document.getElementById('open-sidebar-button')
const navbar = document.getElementById('navbar')

const media = window.matchMedia("(width < 700px)")

media.addEventListener('change', (e) => updateNavbar(e))

function updateNavbar(e){
  const isMobile = e.matches
  console.log(isMobile)
  if(isMobile){
    navbar.setAttribute('inert', '')
  }
  else{
    // desktop device
    navbar.removeAttribute('inert')
  }
}

function openSidebar(){
  navbar.classList.add('show')
  openButton.setAttribute('aria-expanded', 'true')
  navbar.removeAttribute('inert')
}

function closeSidebar(){
  navbar.classList.remove('show')
  openButton.setAttribute('aria-expanded', 'false')
  navbar.setAttribute('inert', '')
}

// For Bookmark Links
// const navLinks = document.querySelectorAll('nav a')
// navLinks.forEach(link => {
//   link.addEventListener('click', () => {
//     closeSidebar()
//   })
// })

updateNavbar(media)
let slide = document.getElementById('slide');
let upArrowb = document.getElementById('upArrowb');
let downArrowb = document.getElementById('downArrowb');

var a = 0;
upArrowb.addEventListener('click' , ()=>{
   
    if(a < 0){
        a = a+300;
        slide.style.top=a+"px";

    }

})

downArrowb.addEventListener('click' , ()=>{
   
    if(a > "-900"){
        a = a - 300;
        slide.style.top=a+"px";

    }

})

