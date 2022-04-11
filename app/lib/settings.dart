import 'package:flutter/material.dart';

class SettingsPage extends StatelessWidget {
  const SettingsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color(0xFF032B49),
      body: Container(
            child: Column(children: <Widget>[
              Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: const [
                  Icon(Icons.account_circle_outlined,
                      size: 250.0, semanticLabel: "User Profile",color: Colors.blueAccent),
                ],
              ),
              Column(
                children: [
                  Container(
                    padding: const EdgeInsets.all(15.0),
                    margin: const EdgeInsets.all(20.0),
                    height: 100,
                    width: 250,
                    decoration: BoxDecoration(
                        color: Colors.blue[200],
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: const [
                          BoxShadow(
                            color: Colors.blue,
                            offset: Offset(4, 4),
                            blurRadius: 10,
                            spreadRadius: 1,
                          )]
                    ),
                    child: FittedBox(
                      fit: BoxFit.scaleDown,
                      child: Text(
                        ('User Id: 264867'),
                        style: TextStyle(
                          color: Colors.grey[900],
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ),
                Container(
                    padding: const EdgeInsets.all(15.0),
                    margin: const EdgeInsets.all(20.0),
                    height: 100,
                    width: 250,
                    decoration: BoxDecoration(
                        color: Colors.blue[200],
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: const [
                          BoxShadow(
                            color: Colors.blue,
                            offset: Offset(4, 4),
                            blurRadius: 10,
                            spreadRadius: 1,
                          )]
                    ),
                    child: FittedBox(
                      fit: BoxFit.scaleDown,
                      child: Text(
                        ('User Name: AbcdWxyz'),
                        style: TextStyle(
                          color: Colors.grey[900],
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                ),
                ]
              ),
            ],)
      )
    );
  }
}
