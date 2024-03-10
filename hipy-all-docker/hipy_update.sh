#!/bin/bash
echo 'hipy日常更新'
echo '本脚本测试环境为 wsl2-ubuntu22.04.3（LTS），其他linux环境根据自'
echo '清理旧数据库'
mv ./hipy-ui/dashboard/node_modules .
rm -rf ./postgres
rm -rf ./hipy-ui
mkdir -p bak
mkdir -p postgres/data
mv ./hipy-server/app/t4/files/txt ./bak
echo '开始从道长仓库更新 hipy-server 代码'
cd ./hipy-server
sleep 3
git pull
sleep 3
cd ..
rsync -av ./bak/txt ./hipy-server/app/t4/files
rm -rf ./bak
echo '开始从道长仓库更新 hipy-ui 代码'
git clone https://github.com/hjdhnx/hipy-ui.git
sleep 3
echo '复制替换打包脚本防止报错'
cp -Raf package.json  ./hipy-ui/dashboard
cp -Raf .env.staging ./hipy-ui/dashboard
mv ./node_modules ./hipy-ui/dashboard
sleep 3
echo '启动前端 UI 打包 node 容器'
docker run -itd -v /mnt/usb1_3_4-1/docker/hipy/hipy-ui/dashboard:/home/node -w /home/node --name hipy-node node
sleep 3
echo '开始打包前端 UI'
docker exec hipy-node npm i
ssleep 3
docker exec hipy-node npm run build:stage
echo '初始化数据'
docker exec hipy-server python3 initial_data.py
sleep 3
echo '重启所有容器'
docker restart $(docker ps -a -q)
echo '停止前端 UI 打包 node 容器'
docker stop -t=10 hipy-node
docker rm -f hipy-node
echo 'HIPY所有内容均已更新完成'
echo '感谢道长的HIPY项目'
sleep 3