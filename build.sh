pwd
ls -la *
echo $SRC_TOP

cd ${SRC_TOP}/activities/stream_consumer
sh build.sh

cd ${SRC_TOP}/infra/api/
sh ./build.sh