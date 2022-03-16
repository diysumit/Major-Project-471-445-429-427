class Coin {
  Coin(
      {required this.name, required this.symbol, required this.imageUrl, required this.price, required this.change, required this.changePercent,this.expanded=false});

  String name;
  String symbol;
  String imageUrl;
  num price;
  num change;
  num changePercent;
  bool expanded;

  factory Coin.fromJson(Map<String, dynamic> json) {
    return Coin(
      name: json['name'],
      symbol: json['symbol'],
      imageUrl: json['image'],
      price: json['current_price'],
      change: json['price_change_24h'],
      changePercent: json['price_change_percentage_24h'],
    );
  }
}
List<Coin> coinList = [];
