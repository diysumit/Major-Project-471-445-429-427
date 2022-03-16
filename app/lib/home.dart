import 'package:flutter/material.dart';
import 'coin.dart';
import 'coinCard.dart';
import 'coinInfo.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      // Center is a layout widget. It takes a single child and positions it
      // in the middle of the parent.
        scrollDirection: Axis.vertical,
        itemCount: coinList.length,
        itemBuilder: (context, index) {
          return InkWell(
            onTap: () {
              Navigator.of(context).push(MaterialPageRoute(
                  builder: (context) => CoinInfo(Coin: coinList[index])));
            },
            child: CoinCard(
              name: coinList[index].name,
              symbol: coinList[index].symbol,
              imageUrl: coinList[index].imageUrl,
              price: coinList[index].price.toDouble(),
              change: coinList[index].change.toDouble(),
              changePercent: coinList[index].changePercent.toDouble(),
            ),
          );
        }
    );
  } // This trailing comma makes auto-formatting nicer for build methods.
}
