/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';

let items=[]
let cost=0



function readcart() {

    var json_str = getCookie('itemlist');
    var items = JSON.parse(json_str);

    var cost = getCookie('cost')
    
    let cart = document.querySelector("#total")
    

    while (cart.firstChild) {
        cart.removeChild(cart.firstChild);
    } 

    
    
    
    let displaycost = document.createElement("p")
    displaycost.innerHTML = "Your total is " + cost
    cart.appendChild(displaycost)

    let list = document.createElement("ul")
    list.setAttribute("id", "totallist")
    list.setAttribute("class", "list-group list-group-flush")
    




    for (var i = 0; i <=items.length-1; i++) {
        
        let displaycart = document.createElement("li")
        displaycart.setAttribute("class", "list-group-item")
        displaycart.innerHTML = items[i]
        list.appendChild(displaycart)
    }
    

    cart.appendChild(list)

    let button = document.createElement("button")
    button.innerHTML = "X"
    button.setAttribute("onclick", "removecart()")
    button.setAttribute("class", "btn btn-dark ")

    cart.appendChild(button)
    
}

function removecart() {
    let cart = document.querySelector("#total")
    

    while (cart.firstChild) {
        cart.removeChild(cart.firstChild);
    } 
}






function addtocart(name, price){
    
    
    cost = parseFloat(cost)+parseFloat(price)
    items.push(name)

    var json_str = JSON.stringify(items);
    setCookie('itemlist', json_str, 1);
    setCookie('cost', cost, 1)
}

function removetocart(name, price){
    
    let bool = false

    for( var i = 0; i <= items.length; i++){ 
    
        if ( items[i] === name) { 
    
            bool = true 
        }
        
    
    }
    if (bool == true) {
    
    
    if (cost > 0) {
        cost = parseFloat(cost)-parseFloat(price)
    }
    for( var i = 0; i <= items.length; i++){ 
    
        if ( items[i] === name) { 
    
            items.splice(i, 1); 
            break
            
        }
        else if (items.length == 1) {
            items.shift()
        
        }
        bool = false
    
    }}
    
    var json_str = JSON.stringify(items);
    setCookie('itemlist', json_str, 1);
    setCookie('cost', cost, 1)
    
}




function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }




function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }




