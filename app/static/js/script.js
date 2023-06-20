var randomchange = document.getElementById('randomchange')
imgs = [
    '../mewtwo.jpg',
    '../charizard.jpg',
    '../blastoise.jpg',
    '../venusaur.jpg',
    '../pikachu.jpg',
    '../articuno.jpg',
    '../gengar.jpg',
    '../alakazam.jpg',
    '../gyarados.jpg',
    '../zapdos.jpg',
    '../moltres.jpg',
    '../kingler.jpg'
]

var imgCount = imgs.length

var number = Math.floor(Math.random() * imgCount)

window.onload = function(){

    randomchange.style.backgroundImage = 'url('+imgs[number]+')'

}

document.getElementById("demo").innerHTML = "Hello JavaScript!";