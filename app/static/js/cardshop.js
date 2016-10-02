function setCartData(o){
		localStorage.setItem('cart', JSON.stringify(o));
		return false;
                        }
		
		
            function getCartData(){
		return JSON.parse(localStorage.getItem('cart'));
                        }
		
		
	function renderCard(){
		if (typeof(Storage) !== "undefined") {
			// Code for localStorage/sessionStorage.
			} else {
				alert('Корзина магазина не доступна для вашего браузера');
			// Sorry! No Web Storage support..
		}
		var cartData = getCartData() || {}
		if(cartData !== null) {
		itogo = 0;
                totalsum = $('#total').text();
                            for(var item in cartData) {
			itogo = itogo+Number(cartData[item][4]);
			if (cartData[item][4] === 0) {
				continue;
			}
			carditem =
			'<div class="shipping-item" id="' + item + '">' +
			'<span class="cross-icon"><i class="fa fa-times-circle" onclick="removeToCard('+ item +')"></i></span>' +
			'<div class="shipping-item-image">' +
			'<a href="' + cartData[item][2] + '">' +
			'<img src="' + cartData[item][1] + '"</a>' +
			'</div>' +
			'<div class="shipping-item-text">' +
			'<span class="count">' + cartData[item][4] + '<span class="pro-quan-x">x</span>' +
			'<a href="' + cartData[item][2] + '" class="pro-cat">' + cartData[item][0] + '</a></span>' +
			'<span class="pro-quality">'+
			'<a href="' + cartData[item][2] + '"></a></span><p>$' + cartData[item][3] + '</p>' +
			'</div></div>';
			$('#shopcard').append(carditem);
			totalsum = totalsum + cartData[item][3]*cartData[item][4];
					}
				}
			count = Number($('#count').text());
			$('#count').text(count+Number(itogo));
                        $('#total').text(totalsum);

			}

		window.onload = renderCard;			
                function addToCard(data) {
                    var cartData = getCartData() || {};
                    d = data.split(',');
                    itemId = d[0];
	        itelPrice = d[1];
                    itemTitle = d[2];
	        itemHref = d[3];
                    itemImage = d[4];
                    if(cartData.hasOwnProperty(itemId)){
		if (cartData[itemId][4] > 0) {
		itemCount = cartData[itemId][4]+1;
                        cartData[itemId] = [itemTitle, itelPrice, itemImage, itemHref, itemCount];
		$('#' + itemId + '').find('.shipping-item-text').find('.count').text(itemCount+'x');
		} else {
			carditem =
			'<div class="shipping-item" id="' + itemId + '">' +
			'<span class="cross-icon"><i class="fa fa-times-circle" onclick="removeToCard('+ itemId +')"></i></span>' +
			'<div class="shipping-item-image">' +
			'<a href="' + itemImage + '">' +
			'<img src="' + itelPrice + '"</a>' +
			'</div>' +
			'<div class="shipping-item-text">' +
			'<span class="count">' + 1 + '<span class="pro-quan-x">x</span>' +
			'<a href="' + itemImage + '" class="pro-cat">' + itemTitle + '</a></span>' +
			'<span class="pro-quality">'+
			'<a href="' + itemImage + '"></a></span><p>$' + itemHref + '</p>' +
			'</div></div>';
			$('#shopcard').append(carditem);
			cartData[itemId] = [itemTitle, itelPrice, itemImage, itemHref, 1];
		}
                        } else {
			$('#shopcard').append(carditem);
			}
			setCartData(cartData);
			count = Number($('#count').text());
			$('#count').text(count+1);

                    totalsum = $('#total').text();
                    $('#total').text(Number(totalsum)+Number(itemHref));
            }
                    
	        function removeToCard(id){
		var cartData = getCartData() || {};
			if (cartData[id][4] === 1) {
				$('#' + id + '').remove();
			} 
			itemCount = cartData[id][4]-1;
			cartData[id][4] = itemCount;
			cartData[id] = [cartData[id][0], cartData[id][1], cartData[id][2], cartData[id][3], itemCount];
			$('#' + id + '').find('.shipping-item-text').find('.count').text(itemCount+'x');
			setCartData(cartData);
			count = Number($('#count').text());
			$('#count').text(count-1);
			totalsum = $('#total').text();
			$('#total').text(Number(totalsum)-Number(cartData[id][3]));

                }

