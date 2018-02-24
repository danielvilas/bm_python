# bm_python
Benchmark Python
```sh
sudo apt-get update

Install python 3.6.4
Follow the example on (be careful is for 3.6.0)
https://gist.github.com/xslendix/fcb55ae06b49be557e3418cfa8af4534

sudo pip3 install numpy

sudo apt-get install swig
sudo apt-get install libfann2
sudo apt-get install libfann-dev
sudo ln -s /usr/lib/arm-linux-gnueabihf/libdoublefann.so /usr/lib/libdoublefann.so
sudo pip3 install fann2

sudo apt-get install libssl-dev
git clone https://github.com/eclipse/paho.mqtt.c.git
cd paho.mqtt.c
make
sudo make install
cd ..
sudo pip3 install paho-mqtt

sudo pip3 install kazoo
sudo pip3 install kazka
sudo pip3 install requests


git clone https://github.com/danielvilas/bm_python
cd bm_python

python3 main.py -d 0Initial -p KAFKA

```