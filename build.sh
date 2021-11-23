pwd
ls -la *

## python is there
python --version

## install npm
NODE_VERSION=16
yum install -y gcc-c++ make
curl -sL https://rpm.nodesource.com/setup_${NODE_VERSION}.x | bash -
yum install -y nodejs 

echo "Node version"
node -v

echo "NPM Version"
npm -v

echo "Install aws cdk"
cdk --version
npm install -g aws-cdk
cdk --version

echo $SRC_TOP
cd ${SRC_TOP}/activities/stream_consumer
sh build.sh

cd ${SRC_TOP}/infra/api/
sh ./build.sh
