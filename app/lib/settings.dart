import 'package:flutter/material.dart';

class SettingsPage extends StatelessWidget {
  const SettingsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
            child: Column(children: <Widget>[
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: const [
                  Icon(Icons.account_circle_outlined,
                      size: 250.0, semanticLabel: "User Profile"),
                ],
              ),
              Row(
                children: [
                Container(
                   color: Colors.blue,
                   margin: const EdgeInsets.all(25.0),
                   child: const Text('User Id: 264867',)
                ),
                Container(
                   color: Colors.blue,
                   margin: const EdgeInsets.all(25.0),
                   child: const Text('User Id: 264867')
                ),
                ]
              ),
            ],)
      )
    );
  }
}
