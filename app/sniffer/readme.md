### linux系统安装selenium-需要python3.8环境

```shell
apt update
apt install libxss1 libappindicator1 libindicator7  # 安装软件依赖
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  # 下载最新版chrome
dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
# 如果提示缺少某些依赖无法安装，可以试一下 apt install -f
google-chrome --version  # 查看当前chrome版本 123.0.6312 太新了没区别
# 90.0.4430.24 有驱动
# https://vikyd.github.io/download-chromium-history-version/#/
# https://www.slimjet.com/chrome/google-chrome-old-version.php
wget -O google-chrome-90.deb -c https://www.slimjet.com/chrome/download-chrome.php?file=files%2F90.0.4430.72%2Fgoogle-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
```