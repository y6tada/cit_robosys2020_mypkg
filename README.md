# cit_robosys2020_mypkg
2020年度開口「CITロボットシステム学」の課題2「ROSを使ったアプリケーションの実装」のリポジトリです。Space Navigatorという6DoFの入力デバイスのうち、X軸の直進とZ軸の回転の2要素だけを抜き出して、Turtlesimを動作させます。本成果物は、Space Navigatorの入力とTurtlesimの動作は既存のパッケージに任せ、相互のトピック通信の間を取り持つPythonスクリプトを独自に実装したものです。

Original Lecture: [ryuichiueda/robosys2020](https://github.com/ryuichiueda/robosys2020)

## Video
[![](https://img.youtube.com/vi/TDrd6Gbrdqw/0.jpg)](https://www.youtube.com/watch?v=TDrd6Gbrdqw)

## Operating environment
```
# Hardware
MacBook Pro 16-inch 2019(Model A2141)

# Virtual Desktop Software
Parallels Desktop 16 for Mac Version 16.1.2 (49151)

$ uname -a
Linux ubuntu 5.8.0-36-generic #40~20.04.1-Ubuntu SMP <time> x86_64 x86_64 x86_64 GNU/Linux

$ rosversion -d
noetic
```
## Install and execute
```
# ros-<version>-spacenav-node is required to execute this software
sudo apt install ros-noetic-spacenav-node

# clone
cd <your_catkin_ws>/src
git clone https://github.com/y6tada/cit_robosys2020_mypkg.git

# execute
chmod +x spacenav_turtlesim_teleop.py
roslaunch mypkg spacenav_turtlesim_teleop.launch
```

## Description
`rqt_graph`を実行すると、動作状態にある全ノードとトピックが可視化できる。独自に実装されたスクリプトは`spacenav_turtlesim_teleop`で、それ以外は提供されているパッケージをインストールしてそのままの状態で用いた。

<img width="800" alt="graph" src="https://user-images.githubusercontent.com/18658190/104603124-7664ec80-56bf-11eb-809f-8b7cc160efd0.png">

`rqt`を実行すると、ROSが提供する可視化ツールを自由にレイアウトして表示できる。`spacenav_node`はTwist以外にもJoyやOffset等の複数のトピックを持っていることがわかる。`spacenav/twist`には
```
float64 linear.x
float64 linear.y
float64 linear.z
float64 angular.x
float64 angular.y
float64 angular.z
```
の6DoF情報が含まれており、その値は(-1.0 ~ 0 ~ 1.0)となるよう実装されている。このうち`linear.x, angular-z`の2値をsubscribeし、Turtlesim nodeに投げる実装が`spacenav_turtlesim_teleop.py`に実装されている。
<img width="800" alt="rqt" src="https://user-images.githubusercontent.com/18658190/104604083-6994c880-56c0-11eb-8e5c-fbacb73786d0.png">


## License

*cit_robosys2020_mypkg* is under the BSD License. Please check [LICENSE](https://github.com/y6tada/cit_robosys2020_mypkg/blob/main/LICENSE)

