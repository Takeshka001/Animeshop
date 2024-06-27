function toNum(str) {
  const num = Number(str.replace(/ /g, ""));
  return num;
}

function toCurrency(num) {
  const format = new Intl.NumberFormat("ru-RU", {
    style: "currency",
    currency: "RUB",
    minimumFractionDigits: 0,
  }).format(num);
  return format;
}


// Попап

const popup = document.querySelector(".popup");
const popupClose = document.querySelector("#popup_close");
const body = document.body;
const popupContainer = document.querySelector("#popup_container");
const popupProductList = document.querySelector("#popup_product_list");
const popupCost = document.querySelector("#popup_cost");
const popupDiscount = document.querySelector("#popup_discount");
const popupCostDiscount = document.querySelector("#popup_cost_discount");

cart.addEventListener("click", (e) => {
  e.preventDefault();
  popup.classList.add("popup--open");
  body.classList.add("lock");
  popupContainerFill();
});

function popupContainerFill() {
  popupProductList.innerHTML = null;
  const savedCart = JSON.parse(localStorage.getItem("cart"));
  myCart.products = savedCart.products;
  const productsHTML = myCart.products.map((product) => {
    const productItem = document.createElement("div");
    productItem.classList.add("popup__product");

    const productWrap1 = document.createElement("div");
    productWrap1.classList.add("popup__product-wrap");
    const productWrap2 = document.createElement("div");
    productWrap2.classList.add("popup__product-wrap");

    const productImage = document.createElement("img");
    productImage.classList.add("popup__product-image");
    productImage.setAttribute("src", product.imageSrc);

    const productTitle = document.createElement("h2");
    productTitle.classList.add("popup__product-title");
    productTitle.innerHTML = product.name;

    const productPrice = document.createElement("div");
    productPrice.classList.add("popup__product-price");
    productPrice.innerHTML = toCurrency(toNum(product.priceDiscount));

    const productDelete = document.createElement("button");
    productDelete.classList.add("popup__product-delete");
    productDelete.innerHTML = "&#10006;";

    productDelete.addEventListener("click", () => {
      myCart.removeProduct(product);
      localStorage.setItem("cart", JSON.stringify(myCart));
      popupContainerFill();
    });

    productWrap1.appendChild(productImage);
    productWrap1.appendChild(productTitle);
    productWrap2.appendChild(productPrice);
    productWrap2.appendChild(productDelete);
    productItem.appendChild(productWrap1);
    productItem.appendChild(productWrap2);

    return productItem;
  });

  productsHTML.forEach((productHTML) => {
    popupProductList.appendChild(productHTML);
  });

  popupCost.value = toCurrency(myCart.cost);
  popupDiscount.value = toCurrency(myCart.discount);
  popupCostDiscount.value = toCurrency(myCart.costDiscount);
}

popupClose.addEventListener("click", (e) => {
  e.preventDefault();
  popup.classList.remove("popup--open");
  body.classList.remove("lock");
});

// script.js 
document.addEventListener('DOMContentLoaded', function() { 
  var cartButton = document.getElementById('cart'); 
  var cartPopup = document.getElementById('cart_popup'); 
  var popupCloseButton = document.getElementById('popup_close'); 
 
  cartButton.addEventListener('click', function() { 
      cartPopup.style.display = 'flex'; 
  }); 
 
  popupCloseButton.addEventListener('click', function() { 
      cartPopup.style.display = 'none'; 
  }); 
 
  // Optional: Close the popup when clicking outside of it 
  window.addEventListener('click', function(event) { 
      if (event.target == cartPopup) { 
          cartPopup.style.display = 'none'; 
      } 
  }); 
});

