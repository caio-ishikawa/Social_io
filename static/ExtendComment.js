const extendComment = (val) => {
    console.log(val)
    const div = document.getElementById(val)
    if (div.style.display === 'block'){
        div.style.display= 'none'
        console.log('visible')
    }
    else{
        div.style.display= 'block'
        console.log('invisible')
    }
}
