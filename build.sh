pwd
ls -la *

## python is there
python --version

## install npm
NODE_VERSION=16
sudo yum install -y gcc-c++ make
curl -sL https://rpm.nodesource.com/setup_${NODE_VERSION}.x | sudo -E bash -
sudo yum install -y nodejs 
node -v
npm -v


npm install -g aws-cdk
cdk --version





echo $SRC_TOP
cd ${SRC_TOP}/activities/stream_consumer
sh build.sh

cd ${SRC_TOP}/infra/api/
sh ./build.sh
