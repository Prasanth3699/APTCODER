// for cart value 
$(document).ready(function () {
  $(".increase-btn").click(function (e) { 
    e.preventDefault();
    
    var inc_val = $(this).closest(".product_data").find(".item-quantity").val();
    var value = parseInt(inc_val,10);
    value = isNaN(value) ? 0 : value;
    if (value < 10)
    {
      value++;
      $(this).closest(".product_data").find(".item-quantity").val(value);
    }
    
  });

  $(".decrease-btn").click(function (e) { 
    e.preventDefault();
    
    var dec_val = $(this).closest(".product_data").find(".item-quantity").val();
    var value = parseInt(dec_val,10);
    value = isNaN(value) ? 0 : value;
    if (value > 1)
    {
      value--;
      $(this).closest(".product_data").find(".item-quantity").val(value);
    }
    
  });

// change cart item
$('.changeQuantity').click(function (e) { 
  e.preventDefault();

  var itemId = $(this).closest('.product_data').find('.item-id').val();
  var token = $('input[name=csrfmiddlewaretoken]').val();
  var itemQuantity = $(this).closest('.product_data').find('.item-quantity').val();
  
  $.ajax({
    type: "POST",
    url: "/updateCart",
    data: {
      'itemId':itemId,
      'itemQuantity':itemQuantity,
      csrfmiddlewaretoken: token
    },
    
    success: function (response) {
      alertify.success(response.status)
    }
  });
});

});


// add To Cart 
$('.addToCartBtn').click(function (e) { 
  e.preventDefault();

  var itemId = $('.item-id').val();
  var itemQuantity = $('.item-quantity').val();
  var token = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
    type: "POST",
    url: "/addToCart",
    data: {
      'itemId':itemId,
      'itemQuantity':itemQuantity,
      csrfmiddlewaretoken: token,
    },
    success: function (response) {
      alertify.success(response.status)
    }
  });
});

$('.delete-cart-item').click(function (e) { 
  e.preventDefault();
  var itemId = $(this).closest('.product_data').find('.item-id').val();
  var token = $('input[name=csrfmiddlewaretoken]').val();
  
  $.ajax({
    type: "POST",
    url: "deleteCartItem",
    data: {
      'itemId':itemId,
      csrfmiddlewaretoken: token,
    },
    success: function (response) {
      $('.cartdata').load(location.href + " .cartdata");
    }
  });
});

