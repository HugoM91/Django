var help_sell_binance = 0
var help_buy_binance = 0
var help_sell_bitfinex = 0
var help_buy_bitfinex = 0
var help_sell_coinbase = 0
var help_buy_coinbase = 0
var help_sell_kraken = 0
var help_buy_kraken = 0

function add_python_mkOrders(exchange,side, price, quantity, symbol){
  var text = quantity;
  $.ajax(
      {
        url:"market_orders/testcall",
        type:'POST',
        data: {
          text: text,
         },
        success: function callback(response){

          console.log('SUCESSOOO!!!!!!!!!!');
        }
      }
  )
}

function update_ticker_sell_binance(exchange,side, price, quantity, symbol){
  let quantity_sell_binance = document.querySelector('#update_ticker_sell_'+exchange)
  help_sell_binance = help_sell_binance + parseFloat(quantity.toFixed(2))
  quantity_sell_binance.innerHTML = parseFloat(help_sell_binance.toFixed(0))
}

function update_ticker_buy_binance(exchange,side, price, quantity, symbol){
  let quantity_buy_binance = document.querySelector('#update_ticker_buy_'+exchange)
  help_buy_binance = help_buy_binance + parseFloat(quantity.toFixed(2))
  quantity_buy_binance.innerHTML = parseFloat(help_buy_binance.toFixed(0))
}

function update_ticker_sell_bitfinex(exchange,side, price, quantity, symbol){
  let quantity_sell_bitfinex = document.querySelector('#update_ticker_sell_'+exchange)
  help_sell_bitfinex = help_sell_bitfinex + parseFloat(quantity.toFixed(2))
  quantity_sell_bitfinex.innerHTML = parseFloat(help_sell_bitfinex.toFixed(0))
}

function update_ticker_buy_bitfinex(exchange,side, price, quantity, symbol){
  let quantity_buy_bitfinex = document.querySelector('#update_ticker_buy_'+exchange)
  help_buy_bitfinex = help_buy_bitfinex + parseFloat(quantity.toFixed(2))
  quantity_buy_bitfinex.innerHTML = parseFloat(help_buy_bitfinex.toFixed(0))
}

function update_ticker_sell_coinbase(exchange,side, price, quantity, symbol){
  let quantity_sell_coinbase = document.querySelector('#update_ticker_sell_'+exchange)
  help_sell_coinbase = help_sell_coinbase + quantity
  quantity_sell_coinbase.innerHTML = help_sell_coinbase
}

function update_ticker_buy_coinbase(exchange,side, price, quantity, symbol){
  let quantity_buy_coinbase = document.querySelector('#update_ticker_buy_'+exchange)
  help_buy_coinbase = help_buy_coinbase + quantity
  quantity_buy_coinbase.innerHTML = help_buy_coinbase
}

function update_ticker_sell_kraken(exchange,side, price, quantity, symbol){
  let quantity_sell_kraken = document.querySelector('#update_ticker_sell_'+exchange)
  help_sell_kraken = help_sell_kraken + parseFloat(quantity.toFixed(2))
  quantity_sell_kraken.innerHTML = parseFloat(help_sell_kraken.toFixed(0))
}

function update_ticker_buy_kraken(exchange,side, price, quantity, symbol){
  let quantity_buy_kraken = document.querySelector('#update_ticker_buy_'+exchange)
  help_buy_kraken = help_buy_kraken + parseFloat(quantity.toFixed(2))
  quantity_buy_kraken.innerHTML = parseFloat(help_buy_kraken.toFixed(0))
}


function Binance_mkOrders(){
  let table = document.querySelector('#table_binance')
  var URL = window.location.host
  let url = "wss://stream.binance.com:9443/ws/manausdt@trade/avaxusdt@trade/trxusdt@trade/datausdt@trade/waxpusdt@trade/ltcusdt@trade/xrpusdt@trade"
  let side = 'ERRO'
  const chatSocket = new WebSocket(url)
  console.log("Connected to Binance Websocket");

  chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data)
    if (data['q']*data['p'] >= 3500){
      if (data['m'] == true){
        side = "sell";
        table_class = ' class="table-danger "'
        update_ticker_sell_binance('binance',side,data['p'],data['q']*data['p'],data['s'])

      } else {
        side = "buy";
        table_class = ' class="table-success "'
        update_ticker_buy_binance('binance',side,data['p'],data['q']*data['p'],data['s'])
      }


      let quantity = data['q']*data['p']
      let price = data['p']
      let symbol = data['s']
      let template ='<tr><td'+table_class+'>'+symbol+'</td><td'+table_class+'>'+price+'</td><td'+table_class+'>'+quantity+'</td><td'+table_class+'>'+side+'</td></tr>'
      table.innerHTML += template
      /*table.prepend(template)*/
      }
    }
}
function Coinbase_mkOrders() {
  let table2 = document.querySelector('#table_coinbase')
  var URL2 = window.location.host
  let url2 = "wss://ws-feed.exchange.coinbase.com"
  let side2 = 'nada'
  const chatSocket2 = new WebSocket(url2)

  chatSocket2.onopen = function () {
    console.log("Connected to Coinbase Websocket");
    chatSocket2.send('{"type": "subscribe","product_ids": ["BTC-USD","ETH-USD"],"channels": ["level2","heartbeat",{"name": "ticker","product_ids": ["BTC-USD"]}]}');
  }

  chatSocket2.onmessage = function(e2){
    let data2 = JSON.parse(e2.data)
    if (data2['type'] == 'l2update') {

      let helpfull_var2 = data2['changes'][0]
      let price2 = helpfull_var2[1]
      let quantity2 = helpfull_var2[2]
      let side2 = helpfull_var2[0]
      let symbol2 = data2['product_id']
        if (quantity2 >= 15000){
          if (side2 == 'sell'){
            table_class = ' class="table-danger "'
            update_ticker_sell_coinbase('coinbase',side2,price2,quantity2,symbol2)
          } else {
            table_class = ' class="table-success "'
            update_ticker_buy_coinbase('coinbase',side2,price2,quantity2,symbol2)
          }


          let template2 ='<tr><td'+table_class+'>'+symbol2+'</td><td'+table_class+'>'+price2+'</td><td'+table_class+'>'+quantity2+'</td><td'+table_class+'>'+side2+'</td></tr>'
          table2.innerHTML += template2
          /*table.prepend(template)*/
        }
      }
    }
  }
function Bitfinex_mkOrders() {

  let table = document.querySelector('#table_bitfinex')
  var URL = window.location.host
  let url = "wss://api-pub.bitfinex.com/ws/2"
  let side = 'ERRO'
  const chatSocket = new WebSocket(url)


  chatSocket.onopen = function () {
    console.log("Connected to Bitfinex Websocket");
    chatSocket.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}');
  }

  chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data)
    if (data[1] == 'te' || data[1] == 'tu') {
      let price = data[2][3]
      let quantity = data[2][2]*price
      let symbol = 'btcusd'
      if (quantity >= 15000 || quantity <= -15000 ){
        if (data[2][2] < 0){
          side = "sell";
          table_class = ' class="table-danger "'
          update_ticker_sell_bitfinex('bitfinex',side,price,quantity,symbol)
        } else {
          side = "buy";
          table_class = ' class="table-success "'
          update_ticker_buy_bitfinex('bitfinex',side,price,quantity,symbol)
        }


        let template ='<tr><td'+table_class+'>'+symbol+'</td><td'+table_class+'>'+price+'</td><td'+table_class+'>'+quantity+'</td><td'+table_class+'>'+side+'</td></tr>'
        table.innerHTML += template
        /*table.prepend(template)*/
      }
    }
  }
}
function Kraken_mkOrders(){
  let table = document.querySelector('#table_kraken')
  var URL = window.location.host
  let url = "wss://ws.kraken.com/"
  let side = 'ERRO'
  const chatSocket = new WebSocket(url)

  chatSocket.onopen = function () {
    console.log("Connected to Kraken Websocket");
    chatSocket.send('{"event":"subscribe", "subscription":{"name":"trade"}, "pair":["BTC/USD","XRP/USD","ETH/USD"]}');
  }

  chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data)

    if (data[2] == 'trade') {



      let price = data[1][0][0]
      let quantity = data[1][0][1] * price
      let symbol = data[3]

      if (quantity >= 15000){
        if (data[1][0][3] == 's'){
          side = "sell";
          table_class = ' class="table-danger "'
          update_ticker_sell_kraken('kraken',side,price,quantity,symbol)
        } else {
          side = "buy";
          table_class = ' class="table-success "'
          update_ticker_buy_kraken('kraken',side,price,quantity,symbol)
        }
        let template ='<tr><td'+table_class+'>'+symbol+'</td><td'+table_class+'>'+price+'</td><td'+table_class+'>'+quantity+'</td><td'+table_class+'>'+side+'</td></tr>'
        table.innerHTML += template
        /*table.prepend(template)*/
        }
      }
    }
  }
