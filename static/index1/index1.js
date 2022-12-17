// constants
// Side Bar
const menuitem = document.querySelectorAll(".menu-item");
// messages
const messagenoti = document.querySelector('#messages-notification');
const message = document.querySelector('.messages');
// Theme Custom Button
const theme = document.querySelectorAll('.design');
const themeModel = document.querySelector('.customize-theme');
const fontsize = document.querySelectorAll(".choose-size span");
var root = document.querySelector(':root');

const cpallet = document.querySelectorAll(".choose-color span");
const bg1 = document.querySelector(".bg-1");
const bg2 = document.querySelector(".bg-2");
const bg3 = document.querySelector(".bg-3");
// post
const postButton = document.querySelectorAll(".post-bt")
const postModel = document.querySelector('.post');
const cancel = document.querySelector("#cancel-bt");
// code
// Clicked animation
const changeactiveness = () => {
    menuitem.forEach(item => {
        item.classList.remove("active");
    })
}
menuitem.forEach(item => {
    item.addEventListener("click", () => {
        changeactiveness();
        item.classList.add("active");
        // Notification pop Up
        if(item.id == "notifications"){
            document.querySelector(".notification-popup").style.display = 'block';
            
            document.querySelector("#notifications .notification-count").style.display = 'none';
        }
        else{
            document.querySelector(".notification-popup").style.display = 'none';
            
        }
    })
})

// Messages animation
messagenoti.addEventListener('click', () =>{
    messagenoti.querySelector('.notification-count').style.display = 'none';
    message.style.boxShadow = '0 0 1rem var(--color-primary)';
    setTimeout(() => {
        message.style.boxShadow = 'none';
    }, 2000);
})
//post
// open Model
postButton.forEach(bt =>{
    bt.addEventListener('click', () => {
        console.log("Hoooo")
        postModel.style.display = 'grid';
    });
})
// Close Model
const closepostmodel = (e) => {
    if(e.target.classList.contains('post')){
        postModel.style.display = 'none';
    }
}
postModel.addEventListener('click',closepostmodel);
// cancel.addEventListener('click', () =>{
//     console.log("Hit")
//     postModel.style.display = 'none';
// })

// Theme Customisation
// open Model


// theme.addEventListener('click', () => {
//     themeModel.style.display = 'grid';
// });
theme.forEach(item => {
    item.addEventListener('click', () => {
    themeModel.style.display = 'grid';
    console.log("hiii")
    });
})
// Close Model
const closethememodel = (e) => {
    if(e.target.classList.contains('customize-theme')){
        themeModel.style.display = 'none';
    }
}
themeModel.addEventListener('click',closethememodel);
// Fonts
const removeselector = () => {
    fontsize.forEach(op => {
        op.classList.remove("active");
    })
}

fontsize.forEach(op => {
    let size;
    
    op.addEventListener("click", () => {
        removeselector();
        op.classList.add("active");

        if(op.classList.contains('font-size-1')){
            size = '10px';
            root.style.setProperty('--sticky-top-left','5.4rem');
            root.style.setProperty('--sticky-top-right','5.4rem');
        }
        if(op.classList.contains('font-size-2')){
            size = '13px';
            root.style.setProperty('--sticky-top-left','5.4rem');
            root.style.setProperty('--sticky-top-right','-7rem');
        }
        if(op.classList.contains('font-size-3')){
            size = '16px';
            root.style.setProperty('--sticky-top-left','-2rem');
            root.style.setProperty('--sticky-top-right','-17rem');
        }
        if(op.classList.contains('font-size-4')){
            size = '19px';
            root.style.setProperty('--sticky-top-left','-5rem');
            root.style.setProperty('--sticky-top-right','-25rem');
        }
        if(op.classList.contains('font-size-5')){
            size = '22px';
            root.style.setProperty('--sticky-top-left','-12rem');
            root.style.setProperty('--sticky-top-right','-35rem');
        }
        // console.log(size);
        document.querySelector('html').style.fontSize = size;
    })    
})

// Color Pallet
const removeselectorcolor = () => {
    cpallet.forEach(op => {
        op.classList.remove("active");
    })
}
cpallet.forEach(op => {
    let color;

    op.addEventListener("click", () => {
        removeselectorcolor();
        
        op.classList.add("active");

        if(op.classList.contains("color-1")){
            color = 252;
        }
        if(op.classList.contains("color-2")){
            color = 52;
        }
        if(op.classList.contains("color-3")){
            color = 352;
        }
        if(op.classList.contains("color-4")){
            color = 152;
        }
        if(op.classList.contains("color-5")){
            color = 202;
        }
        // console.log(color);

        root.style.setProperty("--primary-color-hue", color)
    })
})

// Background

let lightcolorlightness;
let whitecolorlightness;
let darkcolorlightness;

const changeBG = () => {
    root.style.setProperty("--light-color-lightness", lightcolorlightness);
    root.style.setProperty("--white-color-lightness", whitecolorlightness);
    root.style.setProperty("--dark-color-lightness", darkcolorlightness);
}

bg1.addEventListener("click", () => {
    darkcolorlightness = "17%";
    whitecolorlightness = "100%";
    lightcolorlightness = "95%";

    bg1.classList.add("active");
    bg2.classList.remove("active");
    bg3.classList.remove("active");
    changeBG();
    // window.location.reload();
})

bg2.addEventListener("click", () => {
    darkcolorlightness = "95%";
    whitecolorlightness = "20%";
    lightcolorlightness = "15%";

    bg2.classList.add("active");
    bg1.classList.remove("active");
    bg3.classList.remove("active");
    changeBG();
})

bg3.addEventListener("click", () => {
    darkcolorlightness = "95%";
    whitecolorlightness = "10%";
    lightcolorlightness = "0%";

    bg3.classList.add("active");
    bg2.classList.remove("active");
    bg1.classList.remove("active");
    changeBG();
})

