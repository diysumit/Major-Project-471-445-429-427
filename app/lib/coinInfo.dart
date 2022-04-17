import 'package:flutter/material.dart';
import 'package:app/coin.dart';
import 'package:syncfusion_flutter_charts/charts.dart';
import 'dart:async';
import 'dart:math' as math;
import 'coin.dart';
import 'coinCard.dart';
import 'coinInfo.dart';

class CoinInfo extends StatefulWidget {
  final Coin;

  // ignore: non_constant_identifier_names
  const CoinInfo({Key? key, @required this.Coin}) : super(key: key);
  @override
  State<CoinInfo> createState() => _CoinInfoState(Coin);
}

class _CoinInfoState extends State<CoinInfo>{
  @override
  String c;
  _CoinInfoState(this.c);
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Crypto Live',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(c),
    );
  }
}

class MyHomePage extends StatefulWidget {
  String coin;
  MyHomePage(this.coin);


  // final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late List<LiveData> chartData;
  late List<LiveData> chartDataTwo;

  late ChartSeriesController _chartSeriesController;
  late ChartSeriesController _chartSeriesControllerTwo;

  @override
  void initState() {
    chartData = getChartData();
    chartDataTwo = getChartData();
    // Timer.periodic(const Duration(seconds: 1), updateDataSource);
    // Timer.periodic(const Duration(seconds: 1), updateDataSourceTwo);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {


    return SafeArea(
        child: Scaffold(
          appBar: AppBar(
            title: Text(widget.coin),
          ),
          body: Image.asset('assets/images/graph.png'),
        )
    );
  }

  int time = 19;
  void updateDataSource(Timer timer) {
    var arr = [1, 20, 30, 40, 50];
    chartData.add(LiveData(time++, (math.Random().nextInt(60) + 30)));
    chartData.removeAt(0);
    _chartSeriesController.updateDataSource(
        addedDataIndex: chartData.length - 1, removedDataIndex: 0);
  }
  int times = 19;
  void updateDataSourceTwo(Timer timer) {
    chartDataTwo.add(LiveData(times++, (math.Random().nextInt(60) + 30)));
    chartDataTwo.removeAt(0);
    _chartSeriesControllerTwo.updateDataSource(
        addedDataIndex: chartDataTwo.length - 1, removedDataIndex: 0);
  }


  List<LiveData> getChartData() {
    return <LiveData>[
      LiveData(0, 42),
      LiveData(1, 47),
      LiveData(2, 43),
      LiveData(3, 49),
      LiveData(4, 54),
      LiveData(5, 41),
      LiveData(6, 58),
      LiveData(7, 51),
      LiveData(8, 98),
      LiveData(9, 41),
      LiveData(10, 53),
      LiveData(11, 72),
      LiveData(12, 86),
      LiveData(13, 52),
      LiveData(14, 94),
      LiveData(15, 92),
      LiveData(16, 86),
      LiveData(17, 72),
      LiveData(18, 94)
    ];
  }
}

class LiveData {
  LiveData(this.time, this.speed);
  final int time;
  final num speed;
}
