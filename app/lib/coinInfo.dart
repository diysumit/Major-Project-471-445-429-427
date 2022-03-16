import 'package:flutter/material.dart';
import 'package:app/coin.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class CoinInfo extends StatefulWidget {
  // ignore: non_constant_identifier_names
  const CoinInfo({Key? key, required Coin Coin}) : super(key: key);

  @override
  State<CoinInfo> createState() => _CoinInfoState();
}

class _CoinInfoState extends State<CoinInfo>{
  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      backgroundColor: const Color(0xFF032B49),
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
          title: const Text('Crypto Live'),
          backgroundColor: const Color(0xFF134190)
      ),
      body:Center(
      ),
    );
  }
}
